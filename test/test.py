from zhipuai import ZhipuAI
import os
client = ZhipuAI(api_key=os.getenv("zhipu_token"))

response = client.chat.completions.create(
    model="glm-4-plus",  # 请填写您要调用的模型名称
    messages=[
        {"role": "system", "content": "你是一个乐于回答各种问题的小助手，你的任务是提供专业、准确、有洞察力的建议。"},
        {"role": "user", "content": ""},
    ],
    stream=True,
)

# print(type(response))
for chunk in response:
    print(chunk.choices[0].delta.content, end="")