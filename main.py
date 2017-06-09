#coding=utf-8

from gmail import getIdeaUrlsFromEmail

from GetHtml import getHtml

from GetTxtFromHtmls import getTxtFromHtml

from db_ideas import getIdeas

def main():
    urlObjs =  getIdeaUrlsFromEmail()
    for i in urlObjs:
        html,idea_id = getHtml(i[0])
        print getTxtFromHtml(html)
        print '---------'
        print idea_id
    cc = getIdeas()
    print cc.contents

if __name__ == '__main__':
    main()
