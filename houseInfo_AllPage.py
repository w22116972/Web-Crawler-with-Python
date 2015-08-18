import requests
from bs4 import BeautifulSoup
import re
import json

for i in range(5):
    row = i * 20
    # find what the variable is based on paged, which is "firstRow" in this example
    # the way to find it is to go to either "XHR" or "Documents" in "Network" in Developer tool in Google Chrome 
    res = requests.get('http://rent.591.com.tw/index.php?module=search&action=rslist&is_new_list=1&type=1&searchtype=1&region=4&orderType=desc&listview=img&firstRow=%d&totalRows=2088'%(row))
    data = json.loads(res.text) # data['main']
    #print data['main']
    soup = BeautifulSoup(data['main'])
    for item in soup.select('.shInfo') :
        print item.select('.title')[0].text, item.select('.fc-org')[0].text
        
'''
巨城旁Mycity飯店式管理採光套房黃金曝光 

12,500元


大樓公寓,1個月出租費收15000元。黃金曝光 

15,000元


近園區獨立生活小空間(芬蘭行館)黃金曝光 

7,000元


房東自租★對外頻寬1G★中央熱水24小時黃金曝光 

6,500元


清大商圈優質社區溫馨套房黃金曝光 

8,000元


[巨城台大]全淨水套房/獨立洗衣機木地板黃金曝光 

7,900元


~巨城百貨商圈~『角間店面』稀有出租黃金曝光 

170,000元


近交流道~竹科~交大~清大~交通便利黃金曝光 

5,500元


'''
