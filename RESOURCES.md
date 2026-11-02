# AI Agent 工程（smolagents 实战）Resources

## Knowledge

- **smolagents 官方中文文档**（primary source）
  本地副本：`reference-repos/smolagents/docs/source/zh/`（导览 / 5 个 tutorial / 2 个概念指南 / 4 个 example）。
  Use for: 每一课的概念定义与正确用法。在线版挂在 huggingface.co，**本机打不开，一律读本地副本**。
  阅读顺序照 `docs/source/zh/_toctree.yml`：导览 → building_good_agents → inspect_runs → tools → secure_code_execution → memory → intro_agents → react。
- **smolagents 源码 v1.27.0**（本地 `reference-repos/smolagents/`）
  核心循环只在 `src/smolagents/agents.py`；工具在 `tools.py`，记忆在 `memory.py`，模型适配在 `models.py`。
  Use for: 第 3 周起逐行读循环；查任何 API 的真实签名（不要靠记忆或网上旧教程）。
- **smolagents 官方 examples**（`reference-repos/smolagents/examples/`）
  `rag.py`、`text_to_sql.py`、`open_deep_research/`、`multiple_tools.py`。
  Use for: 抄结构、找项目灵感。注意 `rag.py` 依赖 langchain + HF datasets，本机网络跑不了，只看思路。
- [Anthropic: Building effective agents](https://www.anthropic.com/engineering/building-effective-agents)
  agent 设计模式的一手资料，业内普遍引用的分类：workflow 与 agent 的区别，以及「什么时候不该上 agent」。
  Use for: 判断某个需求到底值不值得用 agent，避免一上来就套框架。
- [智谱开放平台文档](https://docs.bigmodel.cn/)（控制台 <https://open.bigmodel.cn/>）
  国产 OpenAI 兼容接口，GLM-4-Flash 有免费额度。Use for: 0 预算下拿到第一个可用的模型 key。
- [硅基流动文档](https://docs.siliconflow.cn/)
  同样 OpenAI 兼容，注册送额度，可选 Qwen2.5-7B-Instruct / Qwen2.5-Coder。
  Use for: 智谱限流或效果不好时的备选；代码能力比智谱略强。

## Wisdom (Communities)

- **smolagents GitHub Issues / Discussions**
  库作者与真实用户的问答。Use for: 报错排查、确认某个写法是不是推荐做法。
  限制：本机 github.com 不通，需在手机或公司网络查看，把结论贴回来。
- **HuggingFace Discord #smolagents 频道**（英文）
  官方社区。Use for: 提问、看别人的 agent 设计。
- John 暂未加入任何社区，不必每课强推；等他做出第一个项目后，再建议发到 Discussions 收反馈。

## Gaps

- 缺一份**中文**的「LLM 应用评测（eval）」系统教程 → 第 5 周前必须补上，这是整个路径里最值钱也最缺资料的一环。
- 缺 RAG 评测的高质量中文一手资料 → 补。
- 缺 smolagents 的中文视频/图文实战讲解（本机打不开 YouTube/B 站长视频时不好用）→ 补。
