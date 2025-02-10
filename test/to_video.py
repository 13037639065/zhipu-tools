from zhipuai import ZhipuAI
import os
client = ZhipuAI(api_key=os.getenv("zhipu_token"))

response = client.videos.generations(
    model="CogVideoX-Flash",
    prompt="比得兔开小汽车，游走在马路上，脸上的表情充满开心喜悦。",
    quality="quality",  # 输出模式，"quality"为质量优先，"speed"为速度优先
    with_audio=True,
    size="1920x1080",  # 视频分辨率，支持最高4K（如: "3840x2160"）
    fps=30,  # 帧率，可选为30或60
)
print(response)
