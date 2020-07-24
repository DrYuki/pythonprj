import pandas as pd

df = pd.DataFrame()
url_list = ['http://202.114.204.36/right/getList.do?viewPage=10&myticket=ff808081733fb2e00173762c2d1b28fd']
for i in range(2, 32):
    # %s 表示把URL变量转换为字符串
    url = 'http://202.114.204.36/right/getList.do?viewPage=%s&myticket=ff808081733fb2e00173762c2d1b28fd' % i
    url_list.append(url)
    # 遍历网页中的table读取网页表格数据

flag = True
for url in url_list:
    info = pd.read_html(url)
    info = info[3]
    if flag:
        flag = False
        df = df.append(info, ignore_index=True)
    else:
        df = df.append(info[1:], ignore_index=True)

    # 列表解析：遍历 dataframe 第3列并且用$开头
df.to_csv("ttt3.csv")


# df = df[[x.startswith('$') for x in df[3]]]
# df.to_csv('Salary.csv', header=['RK', 'NAME', 'TEAM', 'SALARY'], index=False)
