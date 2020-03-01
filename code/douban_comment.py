# 2020.2.14
import urllib.request
import urllib.parse
from bs4 import BeautifulSoup
import time
import jieba
import wordcloud
import crawler_tools


def creat_url(num):
    urls = []
    for page in range(1, 20):
        url = 'https://book.douban.com/subject/' + \
            str(num)+'/comments/hot?p='+str(page)+''
        urls.append(url)
    print(urls)
    return urls


def get_html(urls):
    headers = {
        # 'Cookie': 你的cookie,
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36 OPR/26.0.1656.60',
        'Connection': 'keep-alive'
    }
    for url in urls:
        print('正在爬取：'+url)
        req = urllib.request.Request(url=url, headers=headers)
        req = urllib.request.urlopen(req)
        content = req.read().decode('utf-8')
        time.sleep(10)
    return content


def get_comment(num):
    a = creat_url(num)
    html = get_html(a)
    soupComment = BeautifulSoup(html, 'html.parser')
    comments = soupComment.findAll('span', 'short')
    onePageComments = []
    for comment in comments:
        # print(comment.getText()+'\n')
        onePageComments.append(comment.getText()+'\n')
    print(onePageComments)
    f = open('数据.txt', 'a', encoding='utf-8')
    for sentence in onePageComments:
        f.write(sentence)
    f.close()


raw_str = crawler_tools.get_content('看见', '读书')
sid = crawler_tools.find_sid(raw_str)
print('sid:'+sid)
get_comment(sid)
