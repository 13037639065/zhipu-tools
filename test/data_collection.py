import requests
from bs4 import BeautifulSoup

# 抓取新闻
def fetch_news(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # 假设新闻标题在<h1>标签中
        news_title = soup.find('h1').text
        print(f"新闻标题: {news_title}")
        
        # 你可以根据需要抓取更多信息，如新闻内容等
    except requests.RequestException as e:
        print(f"请求新闻页面时出错: {e}")

# 抓取政府红头文件
def fetch_gov_documents(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # 假设政府文件标题在<h2>标签中
        doc_title = soup.find('h2').text
        print(f"政府文件标题: {doc_title}")
        
        # 你可以根据需要抓取更多信息，如文件内容等
    except requests.RequestException as e:
        print(f"请求政府文件页面时出错: {e}")

# 示例URL，你需要替换为实际的新闻和政府文件页面URL
news_url = 'https://news.cctv.com/china/'
gov_doc_url = 'https://www.gov.cn/'

# fetch_news(news_url)
fetch_gov_documents(gov_doc_url)
