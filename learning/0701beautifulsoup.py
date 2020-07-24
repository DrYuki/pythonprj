import requests
import os
import re

from bs4 import BeautifulSoup

# pip install beautifulsoup4
#url = "http://202.114.204.36/right/getList.do?entityObject=ViewTBookPass&myticket=ff80808173122f460173135aaf030610"
# r = requests.get("http://python123.io/ws/demo.html")
url = "http://www.zuihaodaxue.com/zuihaodaxuepaiming2020.html"
r = requests.get(url)
demo = r.text
soup = BeautifulSoup(demo, "html.parser")
print(soup.prettify())
# for tag in soup.find_all('table'):
#     print(tag)
