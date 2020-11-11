import requests,bs4,re,os,threading
 
 
 
class MeiNvTu:
 
    def __init__(self):
 
        self.url_main='https://网址保密,不能乱发哈哈/pw/'
 
        self.url=f'{self.url_main}thread.php?fid='
 
    def getPageMax(self,typeID=14):
 
        try:
 
            res = requests.get(f'{self.url}{typeID}')
 
            res.encoding = 'utf-8'
 
            soup = bs4.BeautifulSoup(res.text, 'lxml')
 
            pageNum = soup.select('#main > div > span.fl > div.pages.cc > span')
 
            pageNum = int(re.search('/(.*?)Go', str(pageNum)).group(1))
 
            return pageNum
 
        except:
 
            return 0
 
    def getTitleList(self,typeID=14,page=1):
 
        '''
 
        爬取栏目里某一页的列表,网络错误返回False
 
        :param typeID:
 
        :param page:
 
        :return:
 
        '''
 
        try:
 
            res=requests.get(f'{self.url}{typeID}&page={page}')
 
            res.encoding= 'utf-8'
 
            soup=bs4.BeautifulSoup(res.text,'lxml')
 
            listTitle=soup.select('tr > td > h3')
 
            lists=[]
 
            for item in listTitle:
 
                if 'html_data' in item.a['href'] :
 
                    d={}
 
                    d['href']=self.url_main+item.a['href']
 
                    d['title']=item.a.text
 
                    lists.append(d)
 
            return lists
 
        except:
 
            return False
 
    def downImg(self,url,path):
 
        '''
 
        下载一整个页面的图片
 
        :param url:
 
        :param path:
 
        :return:
 
        '''
 
        global pool_sema
 
        res = requests.get(url)
 
        res.encoding = 'utf-8'
 
        soup = bs4.BeautifulSoup(res.text, 'lxml')
 
        imgs=soup.select('#read_tpc > img')
 
        lists=[]
 
        try:
 
            for i,item in enumerate(imgs):
 
 
 
                imgUrl=re.search("window.open\('(.*?)'\);", str(item['onclick'])).group(1)
 
                imgData=requests.get(imgUrl).content
 
                typ=imgUrl.split('.')[-1]
 
                with open(f'{path}{i}.{typ}','wb')as f:
 
                    f.write(imgData)
 
        except:
 
            print('\033[31m[下载失败!网络异常] ' + path)
 
            pool_sema.release()
 
            return
 
 
 
        #将下载好的情况记录下来,下次可以跳过
 
        textpath=''
 
        for item in path.split('\\')[0:3]:
 
            textpath=textpath+item+'\\'
 
        mutex.acquire()
 
        try:
 
            with open(textpath+'log.txt','a')as f:
 
               f.writelines(path.split('\\')[3]+'\n\r')
 
        except:
 
            pass
 
        mutex.release()
 
        # 完成后线程池记录-1
 
        print('\033[31m[完成下载] '+path)
 
        pool_sema.release()
 
    def get_typeTitle(self,id):
 
        '''
 
        返回类型的标题
 
        :param id:
 
        :return:
 
        '''
 
        if id==14:
 
            return '唯美写真'
 
        if id==15:
 
            return '网友马赛克'
 
        if id==16:
 
            return '露出马赛克'
 
        if id==49:
 
            return '街拍马赛克'
 
        if id==21:
 
            return '丝袜美腿'
 
        if id==114:
 
            return '欧美马赛克'
 
    def downloadthe(self,title,path):
 
        '''
 
        判断是否已经下载过,下载过返回True,没下载过返回False
 
        :param title:
 
        :param path:
 
        :return:
 
        '''
 
 
 
        try:
 
            with open(path+'log.txt', 'r')as f:
 
                text = f.read()
 
            if title in text:
 
                return True
 
            else:
 
                return False
 
        except:
 
            return False
 
    def get_Page_History(self,path):
 
        '''
 
        读取上一次结束 的页码
 
        :param path:
 
        :return:
 
        '''
 
        try:
 
            with open(path+'pagelog.ini','r')as f:
 
                return int(f.read())
 
        except:
 
            return 0
 
if __name__ == '__main__':
 
    # 限制线程数量
 
    pool_sema = threading.BoundedSemaphore(70)
 
    # 创建互斥体
 
    mutex = threading.Lock()
 
    #创建爬取对象
 
    mnt=MeiNvTu()
 
    #栏目id
 
    typeID=21
 
    #获得最大页数
 
    page_max=mnt.getPageMax(typeID)
 
    if page_max==0:
 
        print('\033[31m网络错误!,总页数为0')
 
    else:
 
        path_main= f"D:\\爬取的网站图片\\{mnt.get_typeTitle(typeID)}\\"
 
        if os.path.isdir(path_main) != True:
 
            os.makedirs(path_main, mode=0o777)
 
        #爬取某页的列表
 
        page_History=mnt.get_Page_History(path_main)
 
        for i in range(page_max):
 
            #跳过之前下载过的页码
 
            if i+1<page_History:
 
                print(f'\033[37m跳过页码:{i + 1}')
 
                continue
 
            #记录下来页码
 
            with open(path_main+'pagelog.ini','w')as f:
 
                f.write(str(i+1))
 
            print(f'\033[37m当前页码:{i+1}')
 
            titleList = mnt.getTitleList(typeID, i + 1)
 
            if titleList==False:
 
                print('\033[31m网络错误!,列表获取失败!')
 
                break
 
            for item in titleList:
 
                title=item['title'].replace(' ','').replace(':','').replace('！','').replace('?','').replace('*','').replace('"','')
 
                path = path_main + title + "\\"
 
                #判断是否有这个目录,没有的话就建立
 
                if os.path.isdir(path) != True:
 
                    os.makedirs(path, mode=0o777)
 
                if mnt.downloadthe(title,path_main)==False:
 
                    # 线程池记录+1
 
                    pool_sema.acquire()
 
                    print('\033[37m[开始下载] '+path)
 
                    # 爬取某个标题中的所有图片
 
                    t=threading.Thread(target=mnt.downImg,args=(item['href'], path))
 
                    t.setDaemon(True)
 
                    t.start()
 
                else:
 
                    print('\033[35m发现下载过的:',title,' 已经智能跳过!')