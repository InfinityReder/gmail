#coding=utf-8
import urllib
import re

def getHtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html

def getImg(html):
    reg = r'src="(.+?\.jpg)" pic_ext'
    imgre = re.compile(reg)
    imglist = re.findall(imgre,html)
    x = 0
    for imgurl in imglist:
        print imgurl
        # urllib.urlretrieve(imgurl,'%s.jpg' % x)
        x+=1



# html = getHtml("")
# # print html
# # print getImg(html)

# scriptRe = re.compile('<s*script[^>]*>[^<]*<s*/s*scripts*>',re.I)
# htmlRe = re.compile('<[^>]+>')
# blank_line = re.compile('n+')
# contentTxt = scriptRe.sub('',html) #  <[^>]+> delete all htmls
# contentTxt = htmlRe.sub('',contentTxt)
# contentTxt = blank_line.sub('',contentTxt)
# print contentTxt








##过滤HTML中的标签
#将HTML中标签等信息去掉
#@param htmlstr HTML字符串.
def filter_tags(htmlstr):
  #先过滤CDATA
  re_cdata=re.compile('//<!\[CDATA\[[^>]*//\]\]>',re.I) #匹配CDATA
  re_script=re.compile('<\s*script[^>]*>[^<]*<\s*/\s*script\s*>',re.I)#Script
  re_style=re.compile('<\s*style[^>]*>[^<]*<\s*/\s*style\s*>',re.I)#style
  re_br=re.compile('<br\s*?/?>')#处理换行
  re_h=re.compile('</?\w+[^>]*>')#HTML标签
  re_comment=re.compile('<!--[^>]*-->')#HTML注释
  s=re_cdata.sub('',htmlstr)#去掉CDATA
  s=re_script.sub('',s) #去掉SCRIPT
  s=re_style.sub('',s)#去掉style
  s=re_br.sub('\n',s)#将br转换为换行
  s=re_h.sub('',s) #去掉HTML 标签
  s=re_comment.sub('',s)#去掉HTML注释
  #去掉多余的空行
  blank_line=re.compile('\n+')
  s=blank_line.sub('\n',s)
  s=replaceCharEntity(s)#替换实体


  s = re.sub('\s{3,}',' ',s)
  return s
##替换常用HTML字符实体.
#使用正常的字符替换HTML中特殊的字符实体.
#你可以添加新的实体字符到CHAR_ENTITIES中,处理更多HTML字符实体.
#@param htmlstr HTML字符串.
def replaceCharEntity(htmlstr):
  CHAR_ENTITIES={'nbsp':' ','160':' ',
        'lt':'<','60':'<',
        'gt':'>','62':'>',
        'amp':'&','38':'&',
        'quot':'"','34':'"',}
    
  re_charEntity=re.compile(r'&#?(?P<name>\w+);')
  sz=re_charEntity.search(htmlstr)
  while sz:
    entity=sz.group()#entity全称，如>
    key=sz.group('name')#去除&;后entity,如>为gt
    try:
      htmlstr=re_charEntity.sub(CHAR_ENTITIES[key],htmlstr,1)
      sz=re_charEntity.search(htmlstr)
    except KeyError:
      #以空串代替
      htmlstr=re_charEntity.sub('',htmlstr,1)
      sz=re_charEntity.search(htmlstr)
  return htmlstr
def repalce(s,re_exp,repl_string):
  return re_exp.sub(repl_string,s)





s=file('test.html').read()
news=filter_tags(s)
print news
