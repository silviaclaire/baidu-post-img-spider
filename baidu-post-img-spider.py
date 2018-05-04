import urllib.request
import re

class getBdPostImage:
    def __init__(self,baseurl,seeLZ):
        self.baseURL=baseurl
        self.seeLZ='?see_lz='+str(seeLZ)
    def getPage(self,pageNum):
        url=self.baseURL+self.seeLZ+'&pn='+str(pageNum)
        request=urllib.request.Request(url)
        response=urllib.request.urlopen(request)
        return response.read().decode('utf-8','ignore')
    def getPageNum(self,page):
        pattern = re.compile('<li class="l_reply_num.*?</span>.*?<span.*?>(.*?)</span>',re.S)
        result = re.search(pattern,page)
        if result:
        #print result.group(1)  #测试输出
            return result.group(1).strip()
        else:
            return None
    def getIMG(self,page,x):
        pattern=re.compile('<img class="BDE_Image".*?src="(.*?)"',re.S)
        img=re.findall(pattern,page)
        for i in img:
            urllib.request.urlretrieve(i,'%s.jpg' %x)
            x+=1
        return x
    def start(self):
        indexPage = self.getPage(1)
        pageNum = self.getPageNum(indexPage)
        if pageNum == None:
            print("URL has expired, please try again.")
            return
        print("This post has" + str(pageNum) + "page(s).")
        x=1
        for i in range(1,int(pageNum)+1):
            print("Saving images in" + str(i) + "page.")
            page = self.getPage(i)
            x=self.getIMG(page,x)
        print(u"Task Completed.")
print(u"Enter the post code:")
baseURL = 'http://tieba.baidu.com/p/' + str(input(u'http://tieba.baidu.com/p/'))
seeLZ = input("Only get images uploaded by poster? If YES input 1，otherwise 0.\n")
bdImgSpider=getBdPostImage(baseURL,seeLZ)
bdImgSpider.start()