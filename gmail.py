# -*- coding: utf-8 -*-
from __future__ import print_function
import httplib2
import os

import re

from apiclient import discovery
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage


from ListMessages import ListMessages
from GetMessage import GetMimeMessage

from regEmail import findIdeaUrlInHtml

try:
    import argparse
    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
    flags = None

# If modifying these scopes, delete your previously saved credentials
# at ~/.credentials/gmail-python-quickstart.json
SCOPES = 'https://www.googleapis.com/auth/gmail.readonly'
CLIENT_SECRET_FILE = 'client_secret.json'
APPLICATION_NAME = 'Gmail API Python Quickstart'





def get_credentials():
    """Gets valid user credentials from storage.

    If nothing has been stored, or if the stored credentials are invalid,
    the OAuth2 flow is completed to obtain the new credentials.

    Returns:
        Credentials, the obtained credential.
    """
    home_dir = './ignore' #os.path.expanduser('./')
    credential_dir = os.path.join(home_dir, '.credentials')
    if not os.path.exists(credential_dir):
        os.makedirs(credential_dir)
    credential_path = os.path.join(credential_dir,
                                   'gmail-python-quickstart.json')

    store = Storage(credential_path)
    credentials = store.get()
    if not credentials or credentials.invalid:
        flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
        flow.user_agent = APPLICATION_NAME
        if flags:
            credentials = tools.run_flow(flow, store, flags)
        else: # Needed only for compatibility with Python 2.6
            credentials = tools.run(flow, store)
        print('Storing credentials to ' + credential_path)
    return credentials

def getIdeaUrlsFromEmail():
    """Shows basic usage of the Gmail API.

    Creates a Gmail API service object and outputs a list of label names
    of the user's Gmail account.
    """
    credentials = get_credentials()
    http = credentials.authorize(httplib2.Http())
    service = discovery.build('gmail', 'v1', http=http)


    lists,nextPageToken = ListMessages(service,user_id = 'me',q='subject:tradingview')
    # print (lists)
    mes,mes_str = GetMimeMessage(service,user_id = 'me',msg_id = lists[0]['id'])
    # print (mes)
    j = 0
    urls = []
    for part in mes.walk():  
        j = j + 1  
        fileName = part.get_filename()  
        contentType = part.get_content_type()  
        mycode=part.get_content_charset();  
        # 保存附件  
        if fileName:
            print ('保存邮件附件……TODO?')
        elif contentType == 'text/html':  #or contentType == 'text/plain'  
            #保存正文  
            data = part.get_payload(decode=True)  
            content=str(data);  
            # if mycode=='gb2312':  
            #     content= mbs_to_utf8(content)  
            #end if      
            # nPos = content.find('降息')  
            # print("nPos is %d"%(nPos))  
            # print >> f, data  
            # 正则替换掉所有非 <a></a>的标签  <[^>|a]+>
            # reg = re.compile('<[^>|a]+>')
            url,title = findIdeaUrlInHtml(content)
            urls.append((url,title))
            # print (url,title)
        #     contentTxt = re.compile('<[^>|a]+>').sub('',content)
        #     print (reg.sub('',content))
        # #end if  

    return urls

# if __name__ == '__main__':
#     main()
