import re
# html = '''


# '''



# reg = re.compile('<a.*?href=["|\'](.+?)[\'|"].*?>(.*?)</a>')
# ret = reg.search(html)
# # print ret.groups()
# for x in ret.groups():
#     print '--------'
#     print x

# print ret



# email = "tony@tiremove_thisger.net"
# m = re.search("remove_this", email)
# print m.start()
# print email[:m.start()] + email[m.end():]


# ret = re.search('<a.*?href=["|\'](.+?)[\'|"].*?>(.*?)</a>',html)
# print ret.end()



# reg = re.compile('<a.*?href=["|\'](.+?)[\'|"].*?>(.*?)</a>')
# ret = reg.findall(html)
# print len(ret)

def regHtml(html = ''):
    """
    delete all htmls except <a>
    ... TODO : I think i need delete all htmls ... 
    """
    contentTxt = re.compile('<[^>|a]+>').sub('',content) #  <[^>]+> delete all htmls
    return contentTxt

def regEmail(html = ''):
    '''
    reg email to find the A link urls
    '''
    reg = re.compile('<a.*?href=["|\'](.+?)[\'|"].*?>(.*?)</a>')
    ret = reg.findall(html)
    return ret

def findIdeaUrl(list):
    '''
    find the idea url and the idea title
    '''
    for url,txt in list:
        if(~url.find('chart')):
            return url,txt
    return None

# print findIdeaUrl( regEmail(html) )