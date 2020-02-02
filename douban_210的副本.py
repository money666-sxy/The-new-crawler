import urllib.request
import urllib.parse
from bs4 import BeautifulSoup
import time
import jieba
import wordcloud


def get_html(url):
    headers = {
        # 'Cookie': 你的cookie,
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36 OPR/26.0.1656.60',
        'Referer': 'https: // movie.douban.com / subject / 20427187 / comments?status = P',
        'Connection': 'keep-alive'
    }
    req = urllib.request.Request(url=url, headers=headers)
    req = urllib.request.urlopen(req)
    content = req.read().decode('utf-8')
    return content


def get_comment(url):
    html = get_html(url)
    soupComment = BeautifulSoup(html, 'html.parser')

    comments = soupComment.findAll('span', 'short')
    time = soupComment.select(
        '.comment-item > div > h3 > .comment-info > span:nth-of-type(2)')
    name = soupComment.select(
        '.comment-item > div > h3 > .comment-info > a')
    f = open('/Users/money666/Desktop/code/爬虫/看见.txt', 'w', encoding='utf-8')

    Alltime = []
    for one_time in time:
        Alltime.append(one_time.getText()+'\n')
    print(Alltime)

    AllComments = []
    for one_comment in comments:
        AllComments.append(one_comment.getText()+'\n')
    print(AllComments)

    Allnames = []
    for one_name in name:
        Allnames.append(one_name.getText()+'\n')
    print(Allnames)

    for k in Allnames:
        return k
    for j in AllComments:
        return j

    num = 1
    for i in Alltime:
        f.write(str(num))
        f.write('.')
        f.write(i)
        num += 1
        f.write(k)
        f.write(j)


get_comment('https://book.douban.com/subject/20427187/comments/hot?p=1')
