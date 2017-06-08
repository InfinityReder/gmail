#coding=utf-8

from gmail import getIdeaUrlsFromEmail

from GetHtml import getHtml

from GetTxtFromHtmls import getTxtFromHtml

def main():
    urlObjs =  getIdeaUrlsFromEmail()
    for i in urlObjs:
        html = getHtml(i[0])
        print getTxtFromHtml(html)
    

if __name__ == '__main__':
    main()
    