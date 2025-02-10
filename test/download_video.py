from zhipuai import ZhipuAI
import requests
import os

client = ZhipuAI(api_key=os.getenv("zhipu_token"))

response = client.videos.retrieve_videos_result(
    id="25801739163292484-8980747580860869178"
)
print(response)

if response.task_status == "SUCCESS":
    # 获取视频 URL
    video_url = response.video_result[0]

    # 发送 HTTP 请求下载视频
    video_result = requests.get(video_url.url, stream=True)
    cover_image = requests.get(video_url.cover_image_url, stream=True)
    
    # 确保目录存在
    os.makedirs("results", exist_ok=True)
    
    # 保存图片
    cover_image_path = os.path.join("results", "cover_image.jpg")
    with open(cover_image_path, "wb") as file:
        for chunk in cover_image.iter_content(chunk_size=1024):
            if chunk:
                file.write(chunk)

    # 保存视频文件
    video_path = os.path.join("results", "downloaded_video.mp4")
    with open(video_path, "wb") as file:
        for chunk in video_result.iter_content(chunk_size=1024):
            if chunk:
                file.write(chunk)

    print(f"视频已保存到 {video_path}")
else:
    print("视频处理失败")