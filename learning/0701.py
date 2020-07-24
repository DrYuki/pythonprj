import requests
import os

#  模拟浏览器
# kv = {'user-agent':'Mozilla/5.0'}
# url = "https://www.amazon.cn/dp/B01GNVF8BK/"
# r = requests.get(url, headers=kv)
# print(r. status_code)
# print(r.text[1000:2000])

# 百度/360自动搜索关键字
# keyword = "python"
# try:
#     kv = {'wd':keyword}
#     r = requests.get("http://www.baidu.com/s", params=kv)
#     print(r.request.url)
#     r.raise_for_status()
#     print(len(r.text))
#     print(r.text)
# except:
#     print("爬取失败")

# 网络爬取图片并存取
# url = "http://image.ngchina.com.cn/2020/0701/20200701010912613.jpg"
# root = "D://pics//"
# path = root + url.split('/')[-1]
# try:
#     if not os.path.exists(root):
#         os.mkdir(root)
#     if not os.path.exists(path):
#         r = requests.get(url)
#         with open(path, 'wb') as f:
#             f.write(r.content)
#             f.close()
#             print("文件保存成功")
#     else:
#         print("文件已存在")
# except:
#     print("爬取失败")

# IP地址归属地自动查询(失败)
# ip138
# url ="http://www.ip138.com/iplookup.asp?ip="
# try:
#     print(url + '202.204.80.112')
#     r = requests.get(url + '202.204.80.112')
#
#     print(r.request.url)
#     r.raise_for_status()
#     r.encoding = r.apparent_encoding
#     print(r.text[-500:])
# except:
#     print("爬取失败")

