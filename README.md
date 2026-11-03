# AI 工程师成长记录 · 以 smolagents 为主线

这是我（董亚星）从「会用 AI 工具」到「能独立造 AI 系统」的完整学习记录。每天至少两小时，实战优先，所有产出都在这个仓库里。

**主线**：吃透 [smolagents](https://github.com/huggingface/smolagents) —— HuggingFace 官方的 agent 库，核心循环只有 `agents.py` 一个文件，agent 直接写 Python 调用工具，可读性好，适合从源码学起。

## 为什么这么学

我之前的经历都是「用 AI 干活」：用 AI 写测试用例、做数据标注自动化、给客户搭知识库。这些能证明我会用工具，但证明不了我能造系统——面试官问「你的系统准确率是多少」时答不上来。

所以这个仓库的目标不是学名词，是**造出带评测、能上线、能写出数字的东西**。

## 目录

| 目录                  | 内容                              |
| ------------------- | ------------------------------- |
| `lessons/`          | 每一课的讲义（HTML，直接在浏览器打开）           |
| `learning-records/` | 学到的关键洞察，类似开发里的架构决策记录            |
| `lab/`              | 实战代码：5 个可运行示例，看 `lab/README.md` |
| `reference-repos/`  | smolagents 完整源码（本地副本，离线可读）      |
| `tools/`            | 工具脚本（本机直连 GitHub 不通，用 API 提交）   |

`MISSION.md` 是总目标，`RESOURCES.md` 是资料清单，`NOTES.md` 是学习偏好。

## 怎么跑起来

需要 Python 3.13 和 [uv](https://docs.astral.sh/uv/)。

```bash
cd lab
uv sync
uv run python check_env.py
```

## 进度

- [x] 第 1 课 · 跑通第一个 agent
- [x] 第 2 课 · 工具系统深挖与 MCP
- [ ] 第 3 课 · 逐行读 agent 循环
- [ ] 第 4 课 · 从零手写一个 agent
- [ ] 第 5 课 · 给 agent 做评测（最关键的一课）
- [ ] 第 6 课 · 部署与成本

## 环境说明

本机网络有限制：`github.com` 与 `huggingface.co` 直连不通，所以源码走 codeload 下载、提交走 GitHub API、模型用国产免费额度。这些约束都记在 `NOTES.md` 里。
