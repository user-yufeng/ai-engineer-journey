"""Lesson 2 · MCP 示例：接一个现成的 MCP 服务器，白捡两个时间工具。

跑法：uv run python mcp_time.py
"""
import os
from dotenv import load_dotenv
from mcp import StdioServerParameters
from smolagents import CodeAgent, OpenAIServerModel, ToolCollection

load_dotenv()

model = OpenAIServerModel(
    model_id="Qwen/Qwen2.5-7B-Instruct",
    api_base="https://api.siliconflow.cn/v1",
    api_key=os.environ["SILICONFLOW_API_KEY"],
)

server_params = StdioServerParameters(command="uvx", args=["mcp-server-time"])

with ToolCollection.from_mcp(server_params, trust_remote_code=True) as tools:
    print("从 MCP 服务器拿到了:", [t.name for t in tools.tools])
    agent = CodeAgent(tools=[*tools.tools], model=model, add_base_tools=False)
    agent.run("现在上海几点？转化成纽约时间。")
    # print(agent.memory.steps[-1])