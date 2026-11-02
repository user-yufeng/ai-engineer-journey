"""Lesson 1 · Step 3：跑通你的第一个 agent（硅基流动版）。

跑法：uv run python hello_agent.py
"""

import os

from dotenv import load_dotenv
from smolagents import CodeAgent, OpenAIServerModel

load_dotenv()

model = OpenAIServerModel(
    model_id="Qwen/Qwen2.5-7B-Instruct",
    api_base="https://api.siliconflow.cn/v1",
    api_key=os.environ["SILICONFLOW_API_KEY"],
)

agent = CodeAgent(tools=[], model=model, add_base_tools=False)

if __name__ == "__main__":
    agent.run("第 118 个斐波那契数是多少？")
