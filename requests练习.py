import requests
import json

if __name__ == '__main__':

    
    # url = 'https://www.sogou.com/'
    # response = requests.get(url=url)
    # page_text = response.text
    # xiangyin = response
    # print(xiangyin)

    # with open('./sogou.html','w',encoding='utf-8') as fp:
    #     fp.write(page_text)
    # print('爬取数据结束')


    # headers = {
    # 'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36 Edg/90.0.818.66'
    # }
    # url = 'https://www.sogou.com/web'
    # kw = input('Enter a word:')
    # param = {'query':kw}
    # response = requests.get(url, headers = headers, params = param)
    # page_text = response.text
    # fileName = kw + '.html'
    # with open(fileName,'w',encoding ='utf-8') as fp:
    #     fp.write(page_text)
    # print(fileName,'保存成功！！')







    #百度翻译
    post_url = 'https://fanyi.baidu.com/sug'
    headers = {
    'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36 Edg/90.0.818.66'
    }
    word = input('Enter a word:\n')
    dict = {'kw': word}
    response = requests.post(url = post_url, data=dict, headers=headers)
    dict_obj = response.json()
    print (dict_obj)
    filename =word  + '.json'
    fp = open(filename,'w' ,encoding="utf-8")
    json.dump(dict_obj, fp, ensure_ascii= False)
    print ('Over!')