from zhipuai import ZhipuAI
import os
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

# 示例用法
text_to_translate = "很抱歉，我无法直接访问互联网，包括 Wikipedia。不过，我可以根据我的训练数据回答关于金圆券的问题。金圆券是中华民国在 1948 年发行的一种货币，取代了之前的法币。金圆券的发行背景是当时的通货膨胀和货币贬值。然而，金圆券本身也很快失去了价值，导致经济状况进一步恶化。如果你有关于金圆券的具体问题，我会尽力帮助你解答。"
translated_text = translate_text(text_to_translate, "en")
print(translated_text)
