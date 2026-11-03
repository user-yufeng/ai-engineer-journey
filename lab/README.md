# lab/ · 可运行的 smolagents 示例

从零学 agent 时**亲手写、亲手跑通**的代码。每个文件都能直接执行，顺序就是学习顺序：先让 agent 跑起来，再给它装工具，最后让工具拥有记忆。

## 准备（一次性）

1. 装 [uv](https://docs.astral.sh/uv/)（替代 pip 的包管理器，每个项目独立环境）
2. 在 `lab/` 目录下新建 `.env`，写入模型 key：

   ```
   SILICONFLOW_API_KEY=sk-xxxx
   ```

   免费额度申请：https://cloud.siliconflow.cn/ ，用的模型是 `Qwen/Qwen2.5-7B-Instruct`
3. 装依赖：`uv sync`

## 示例清单

| 文件 | 演示什么 | 跑法 |
|---|---|---|
| `hello_agent.py` | 第一个 agent：模型**自己写代码、自己执行** | `uv run python hello_agent.py` |
| `gym.py` | `@tool` 把普通函数变成 agent 能调用的工具 | `uv run python gym.py` |
| `mcp_time.py` | 接一个现成的 MCP 服务器，白捡两个工具 | `uv run python mcp_time.py` |
| `Score_Store.py` | 用 Tool 类写一个**有记忆**的工具（跨调用存状态） | `uv run python Score_Store.py` |
| `check_env.py` | 环境自检：包能导入、agent 能建、工具能注册 | `uv run python check_env.py` |

## 这几个例子想说清的事（面试常问）

- **agent 没有记忆，工具可以有**：两次 `agent.run()` 之间模型是全新的；状态只能活在工具对象里（`Score_Store` 的 `self.records` 就是这么活下来的）。
- **工具说明书决定模型调不调**：docstring 含糊，模型就乱来甚至编造答案——这是真实踩过的坑，不是理论。
- **进工具箱的东西要知道它依赖什么**：`add_base_tools=False` 关掉要联网的官方工具，避免本机网络不通时报错。

> 配套讲义在仓库根目录 `lessons/`（HTML，浏览器直接打开）。
