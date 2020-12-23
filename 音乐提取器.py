import requests

url = 'https://y.qq.com/portal/search.html#page=1&searchid=1&remoteplace=txt.yqq.top&t=song&w=麻雀'
#url = 'https://www.baidu.com/'
headers = {
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36 Edg/87.0.664.57'
}

html = requests.get(url,headers = headers,allow_redirects=False)#发送请求后面加参数,allow_redirects=False 禁用重定向处理
html.encoding = 'utf-8' #源码解析

































#获取状态码
#print(html.status_code)

#获得响应头信息
#print(html.headers) 
# print(html.headers['Content-Type'])
# print(html.headers.get('Content-Length'))

#获取cookies信息
# print(html.cookies)
# print(html.cookies['bid'])

# print(html.history) #
# print(html.url) #获取url
#新建保存文件
# n = open('yuanma.txt','w')
# n.write(html.text)
# n.close()

