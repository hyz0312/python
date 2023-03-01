import requests
from lxml import etree

headers = {
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.57"
}
url = ""
response = requests.get(url, headers=headers)
html = etree.HTML(response.text)
title = html.xpath('')
