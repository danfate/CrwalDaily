import requests,sys,re
from urllib.parse import urljoin
from bs4 import BeautifulSoup


class RelativeSession(requests.Session):
    def __init__(self, base_url):
        super(RelativeSession, self).__init__()
        self.__base_url = base_url

    def request(self, method, url, **kwargs):
        url = urljoin(self.__base_url, url)
        return super(RelativeSession, self).request(method, url, **kwargs)

class SingleDay(object):
    def __init__(self,main_url):
        self.main_url=main_url
        self.urls=[]

    def get_urls(self,origin_urls):
        r=requests.get(origin_urls)
        r.raise_for_status()
        c=r.content
        soup=BeautifulSoup(c,"html.parser")
        t=soup.select('a.right_title-name')
        pageList=soup.find_all(id="pageLink",a=True)
        self.urls=[i.get('href') for i in pageList]



if __name__=="__main__":
    main_url="http://paper.people.com.cn/rmrb/html/2018-09/26/nbs.D110000renmrb_01.htm"
    s=SingleDay(main_url)
    s.get_urls(s.main_url)
    print(s.urls)