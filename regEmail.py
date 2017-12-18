import re
# html = '''


# <html>
# <body>
# Dear InfinityReder,<br/>
# <p>


# <a href='https://www.tradingview.com/u/IvanLabrie/?utm_source=notification_email&amp;utm_medium=email&amp;utm_campaign=notification_follower_idea_update'>IvanLabrie</a> you follow published new update for idea&nbsp;<a href='https://www.tradingview.com/chart/XAUUSD/K0wZDCTb-Gold-Long-term-buy-plan/?utm_source=notification_email&amp;utm_medium=email&amp;utm_campaign=notification_follower_idea_update'>Gold: Long term buy plan</a>.



# </p>

# TradingView Team<br/>
# <a href="https://www.tradingview.com/?utm_source=activation_email&utm_medium=email&utm_campaign=notification_follower_idea_update">www.tradingview.com</a><br/><br/>

# <p>
# <hr/>
# You are receiving this email because you are subscribed to get notifications from TradingView.To manage your subscription options or to unsubscribe go to&nbsp;<a href='https://www.tradingview.com/u/InfinityReder/?utm_source=notification_email&amp;utm_medium=email&amp;utm_campaign=notification_base#notifications'>your profile</a>. To unsubscribe from all email notifications&nbsp;<a href='https://www.tradingview.com/accounts/unsubscribe/ORcBehjvUmVZ8sbX/?utm_source=notification_email&amp;utm_medium=email&amp;utm_campaign=notification_base'>click here</a>.
# </p>
# </body>
# </html>
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


def findIdeaUrlInHtml(html):
    return findIdeaUrl( regEmail(html) )

# print findIdeaUrl( regEmail(html) )