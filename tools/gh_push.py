"""用 GitHub API 把本目录推到 GitHub。

为什么需要这个脚本：本机直连 github.com 不通（git push / git clone 都会超时或被重置），
但 api.github.com 是通的。所以绕过 git 协议，直接用 GitHub 的 Git Database API 写提交。

用法（在仓库根目录）：
    python tools/gh_push.py <owner/repo> "提交说明"

首次使用前：
    1. 在 GitHub 生成 Personal Access Token（勾 repo 权限）
    2. set GITHUB_TOKEN=你的token        （cmd）
       $env:GITHUB_TOKEN="你的token"     （PowerShell）

依赖：requests（项目里已装）。
"""

import base64
import os
import sys
from pathlib import Path

import requests

ROOT = Path(__file__).resolve().parent.parent
API = "https://api.github.com"
IGNORE = {
    ".venv",
    "__pycache__",
    ".git",
    ".workbuddy",
    ".pytest_cache",
    "reference-repos",
    "_inbox",
    "node_modules",
}
IGNORE_FILES = {".env"}  # 含密钥，永远不推


def collect_files() -> list[str]:
    files = []
    for path in ROOT.rglob("*"):
        if not path.is_file():
            continue
        rel = path.relative_to(ROOT)
        if rel.name in IGNORE_FILES or any(part in IGNORE for part in rel.parts):
            continue
        files.append(rel.as_posix())
    return sorted(files)


def make_blobs(session, repo: str, files: list[str]) -> list[dict]:
    tree = []
    for rel in files:
        data = (ROOT / rel).read_bytes()
        r = session.post(
            f"{API}/repos/{repo}/git/blobs",
            json={"content": base64.b64encode(data).decode(), "encoding": "base64"},
        )
        r.raise_for_status()
        tree.append({"path": rel, "mode": "100644", "type": "blob", "sha": r.json()["sha"]})
    print(f"  已上传 {len(tree)} 个文件")
    return tree


def build_tree(session, repo: str, tree: list[dict], base_tree: str | None) -> str:
    sha = base_tree
    for i in range(0, len(tree), 100):
        payload = {"tree": tree[i : i + 100]}
        if sha:
            payload["base_tree"] = sha
        r = session.post(f"{API}/repos/{repo}/git/trees", json=payload)
        r.raise_for_status()
        sha = r.json()["sha"]
    return sha


def main() -> None:
    if len(sys.argv) < 3:
        print('用法: python tools/gh_push.py <owner/repo> "提交说明"')
        sys.exit(1)

    repo, message = sys.argv[1], sys.argv[2]
    token = os.environ.get("GITHUB_TOKEN")
    if not token:
        print("缺少 GITHUB_TOKEN 环境变量")
        sys.exit(1)

    session = requests.Session()
    session.headers.update(
        {
            "Authorization": f"Bearer {token}",
            "Accept": "application/vnd.github+json",
            "X-GitHub-Api-Version": "2022-11-28",
        }
    )

    print(f"目标仓库: {repo}")
    files = collect_files()
    print(f"待提交文件: {len(files)}")

    r = session.get(f"{API}/repos/{repo}")
    r.raise_for_status()
    branch = r.json()["default_branch"]

    ref = session.get(f"{API}/repos/{repo}/git/ref/heads/{branch}")
    parent = ref.json()["object"]["sha"] if ref.status_code == 200 else None

    tree_sha = build_tree(session, repo, make_blobs(session, repo, files), None)

    payload = {"message": message, "tree": tree_sha}
    if parent:
        payload["parents"] = [parent]
    r = session.post(f"{API}/repos/{repo}/git/commits", json=payload)
    r.raise_for_status()
    commit_sha = r.json()["sha"]

    if parent:
        r = session.patch(f"{API}/repos/{repo}/git/refs/heads/{branch}", json={"sha": commit_sha})
    else:
        r = session.post(
            f"{API}/repos/{repo}/git/refs", json={"ref": f"refs/heads/{branch}", "sha": commit_sha}
        )
    r.raise_for_status()

    print(f"完成: {commit_sha[:8]} -> {branch}")


if __name__ == "__main__":
    main()
