import requests
from bs4 import BeautifulSoup
import bs4

# 获取网页额内容
def getHTMLText(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""


# 提取网页内容中信息到合适的数据结构
def fillList(ulist, html):
    soup = BeautifulSoup(html, "html.parser")
    for tr in soup.find("tbody").children:
        if isinstance(tr, bs4.element.Tag):
            tds = tr('td')
            ulist.append([tds[0].string, tds[1].string, tds[4].string])



# 利用数据结构展示并输出结果
def printList(ulist, num):
    tplt = "{0:{3}^10}\t{1:{3}^10}\t{2:^10}" #{3}使用中文空格来填充
    print(tplt.format("排名", "学校名称", "总分", chr(12288)))
    for i in range(num):
        u = ulist[i]
        print(tplt.format(u[0], u[1], u[2], chr(12288)))


def main():
    unifo = []
    url = "http://www.zuihaodaxue.com/zuihaodaxuepaiming2020.html"
    html = getHTMLText(url)
    fillList(unifo, html)
    printList(unifo, 20)  # 20 univs


main()