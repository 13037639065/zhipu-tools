#!/usr/bin/python3
from zhipuai import ZhipuAI
import os
import sys

# 初始化 ZhipuAI 客户端
client = ZhipuAI(api_key=os.getenv("zhipu_token"))

def translate_text(text, target_language):
    """
    使用 ZhipuAI 进行文本翻译

    参数:
    text (str): 要翻译的文本
    target_language (str): 目标语言代码，例如 "en" 表示英语

    返回:
    str: 翻译后的文本
    """
    # 构建请求参数
    request_data = {
        "model": "glm-4",
        "messages": [
            {"role": "system", "content": "你是一个翻译工具"},
            {"role": "user", "content": f"请将以下文本翻译成{target_language}语言: {text}"}
        ]
    }

    # 发送请求并获取响应
    response = client.chat.completions.create(**request_data)
    
    # 提取翻译结果
    translated_text = response.choices[0].message.content
    
    return translated_text

if __name__ == "__main__":
    # 如果参数不够打印 help 信息
    if len(sys.argv) < 2:
        print(f"Usage: {sys.argv} <text>")
        sys.exit(1)
    
    translated_text = translate_text(sys.argv[1], "en")
    print(translated_text)
    exit(0)
