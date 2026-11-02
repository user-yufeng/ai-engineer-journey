import os
from dotenv import load_dotenv
from smolagents import CodeAgent, OpenAIServerModel, tool

load_dotenv()

model = OpenAIServerModel(
    model_id="Qwen/Qwen2.5-7B-Instruct",
    api_base="https://api.siliconflow.cn/v1",
    api_key=os.environ["SILICONFLOW_API_KEY"],
)


@tool
def gym_count(name: str) -> str:
    """查询公司的手机号。
    Args:
        name: 姓名，例如 Jhon
    """
    data = {"Jhon": 18849314469, "曹中南": 18731342629, "沈公子": 19945265578}
    return f"{name}的手机号是{data.get(name, '没有数据')} "


agent = CodeAgent(tools=[gym_count], model=model, add_base_tools=False)

agent.run("老曹的手机号是多少？")
print(agent.memory.steps[-1])