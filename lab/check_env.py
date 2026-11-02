"""环境自检：不联网，只验证 smolagents 能导入、API 签名对不对。

跑法：uv run python check_env.py
"""

from smolagents import CodeAgent, OpenAIServerModel, tool


@tool
def gym_count(city: str) -> str:
    """查询某个城市有多少家健身房。

    Args:
        city: 城市名，例如 深圳
    """
    data = {"深圳": 741, "广州": 506, "上海": 623}
    return f"{city}有 {data.get(city, '没有数据')} 家健身房"


def main() -> None:
    model = OpenAIServerModel(
        model_id="glm-4-flash",
        api_base="https://open.bigmodel.cn/api/paas/v4",
        api_key="占位符-不会真的发请求",
    )
    agent = CodeAgent(tools=[gym_count], model=model, add_base_tools=False)

    print("smolagents 导入成功")
    print("agent 类型:", type(agent).__name__)
    print("工具名:", gym_count.name)
    print("工具说明第一行:", gym_count.description.splitlines()[0])
    print("工具入参:", list(gym_count.inputs.keys()))


if __name__ == "__main__":
    main()
