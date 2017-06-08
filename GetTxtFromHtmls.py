#coding=utf-8

from bs4 import BeautifulSoup
import re
# help: http://cuiqingcai.com/1319.html
# soup = BeautifulSoup(open('test.html'),'lxml') #html5lib慢成狗……不知道支不支持canvas

# print soup.prettify()

# print soup.title.string



# lists =  soup.find_all('div',class_ = 'tv-chart-updates__body')
# lists = soup.select('.tv-chart-updates__body')
# for i in lists:
#     print i.get_text()

# 到目前为止这部分是抓取文本
# 后续还需要做的是抓取图片/canvas


def getTxtFromHtmlFile(fileName):
    return getTxtFromHtml( open(fileName) )

def getTxtFromHtml(html,patlib = 'lxml'):
    soup = BeautifulSoup(html,patlib)
    lists = soup.select('.tv-chart-updates__body')
    txts = []
    for i in lists:
        txt = replaceCharEntity( i.get_text() )
        txts.append(txt)
    return txts


def replaceCharEntity(htmlStr):
    # blank_line = re.compile('\n+')
    # htmlStr = blank_line.sub('\n',htmlStr)
    # more_tap = re.compile('\t+')
    # htmlStr = more_tap.sub('\t',htmlStr)
    blank_line = re.compile('[\r|\n|\t]*\n[\r\n\t]*')
    htmlStr = blank_line.sub('    \n    ',htmlStr)
    more_space = re.compile('\xa0+')
    htmlStr = more_space.sub(' ',htmlStr)
    return htmlStr