# Mission: 从零基础到能独立造 AI Agent 的工程师

## Why

John 现在的简历上，所有 AI 经历都是「用 AI 工具干活」——用 AI 写测试用例、用 AI 做数据标注、用 AI 给客户搭知识库。面试 AI 工程师岗位时，他会被一句话问倒：「那你的系统准确率是多少？」

他要的不是再学一堆名词，而是**能独立从 0 造出一个带评测、能上线、能写出数字的 AI 系统**，把它变成 GitHub 上的公开作品集，用它换一份 AI 工程师的工作。

切入点选了 HuggingFace 的 `smolagents`：它是官方库、代码量小（核心只有一个 `agents.py` 循环）、且 agent 直接写 Python 代码调用工具——正好卡在他「会一点 Python」的最近发展区里。

## Success looks like

- 能读懂并改动 smolagents 源码，说清 agent 每一步在干什么
- 不依赖框架，从零写出一个可运行的 agent 循环（CodeAct / ReAct）
- GitHub 上有一个自己写的 agent 项目：有 README、有测试、有评测集和准确率数字
- 简历上能写系统级数字：准确率、召回率、每次调用成本、延迟

## Constraints

- **每天至少 2 小时**（2026-11-02 更正），单次专注不超过 40 分钟
- **0 预算**：所有工具和模型必须用免费额度
- **零基础**：Python 只会一点，没写过完整工程，没用过 pytest
- **中文学习，实战优先**：看 10 分钟理论必须落到代码上，否则不算学过
- **本机**：RTX 3050 Ti 4GB 显存，Python 3.13，uv 0.12.9，git 2.55，gh 2.102
- **网络受限（重要）**：`github.com` 与 `huggingface.co` 直连不通；`api.github.com`、`codeload.github.com`、PyPI、国内大模型 API 通。推代码和用模型都要按这个前提设计方案

## Out of scope

- 模型训练、微调（LoRA）、预训练
- 数学推导：反向传播、注意力公式推导
- 论文精读
- 前端 / 小程序 / 游戏开发（与主线无关）
