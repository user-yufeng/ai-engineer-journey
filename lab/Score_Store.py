import os
from dotenv import load_dotenv
from smolagents import CodeAgent, OpenAIServerModel,Tool

load_dotenv()
model = OpenAIServerModel(
    model_id="Qwen/Qwen2.5-7B-Instruct",
    api_base="https://api.siliconflow.cn/v1",
    api_key=os.environ["SILICONFLOW_API_KEY"],
)

# class ScoreStore(Tool):
#     name = "score_store"
#     description = "记录并查询学员的练习分数。存过就能查，没存过返回无记录。"
#     inputs = {
#         "action": {"type": "string", "description": "动作：save1 或 nosave"},
#         "name": {"type": "string", "description": "学员姓名"},
#         "score": {"type": "integer", "description": "分数", "nullable": True},
#     }
#     output_type = "string"

#     def __init__(self):
#         super().__init__()
#         self.records = {}          # 这就是类的优势：跨调用的内部状态

#     def forward(self, action: str, name: str, score: int | None = None) -> str:
#         if action == "save1":
#             self.records[name] = score
#             return f"已记录 {name}: {score}"
#         return f"{name}: {self.records.get(name, '无记录')}"
    
# ss = ScoreStore()
# agent = CodeAgent(tools=[ss], model=model, add_base_tools=False)
# agent.run("把王五的分数记成99分")
# agent.run("王五考了多少分？")

class ScoreStore(Tool):
    name = "score_store"
    description = (
        "查询或记录学生的考试分数。"
        "查分数用 action='get'（不需要 score）；"
        "存分数用 action='save' 并给出 score。"
        "之前存过的分数一定能查到，回答分数问题前必须先用本工具查询，禁止猜测。"
    )
    inputs = {
        "action": {"type": "string", "description": "动作：get（查分数）或 save（存分数）"},
        "name": {"type": "string", "description": "学生姓名，例如：张三"},
        "score": {"type": "integer", "description": "分数，仅 action='save' 时需要", "nullable": True},
    }
    output_type = "string"

    def __init__(self):
        super().__init__()
        self.records = {}  # 内部状态，跨调用

    def forward(self, action, name, score=None):
        if action == "get":
            return f"{name} 的分数: {self.records.get(name, '无记录')}"
        if action == "save" and score is not None:
            self.records[name] = score
            return f"已记录 {name}: {score}"
        return f"无法处理动作 '{action}'，请用 get（查分数）或 save（存分数）"

ss=ScoreStore()
agent = CodeAgent(tools=[ss],model=model,add_base_tools=False)
agent.run("把张三的分数记成100分")
agent.run("张三考了多少分？")
print("这轮转了", len(agent.memory.steps), "圈")
