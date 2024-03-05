import requests
from bs4 import BeautifulSoup
import pandas as pd

# 抓取網頁內容
url = "https://vipmbr.cpc.com.tw/mbwebs/ShowHistoryPrice_oil.aspx"
response = requests.get(url)

# 解析網頁內容
soup = BeautifulSoup(response.text, 'html.parser')

# 找到所有的表格元素
tables = soup.find_all('table')

# 將每個表格轉換為 DataFrame
df1 = pd.read_html(str(tables[0]))[0]
df2 = pd.read_html(str(tables[1]))[0]

# 印出 dataframe 


print(df1)
print(df2)

# 將 dataframe 寫入 csv 檔案
df2.to_csv("C:/Users/USER/Desketop/oil.csv", index=False)
#df2=df2.iloc[:,:2]
df2=df2.iloc[:,:5]

#df2=df2.dropna(subset=[df2.columns[1]])

df2[df2.columns[0]]=pd.to_datetime(df2[df2.columns[0]])

print(df2)

import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif']=['arial unicode ms']
plt.plot(df2[df2.columns[0]], df2[df2.columns[1]],label='92無鉛汽油')
plt.plot(df2[df2.columns[0]], df2[df2.columns[2]],label='95無鉛汽油')
plt.plot(df2[df2.columns[0]], df2[df2.columns[3]],label='98無鉛汽油')
plt.plot(df2[df2.columns[0]], df2[df2.columns[4]],label='超級柴油')
plt.legend(loc='upper left')
plt.show()