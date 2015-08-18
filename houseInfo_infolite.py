import requests
from bs4 import BeautifulSoup
res = requests.get(http://www.cthouse.com.tw/BuyingHouse/)
soup = BeautifulSoup(res.text)
for item in soup.select('.search_list'):
    print item.select('.total_text')[0].text, item.select('h2')[0].text, item.select('.total_text3')[0].text
    
    
'''
3880萬 臺北市內湖區內湖路1段 坪數：67.81 坪
2880萬 臺北市內湖區南京東路6段 坪數：47.50 坪
6245萬 臺北市中山區八德路2段 坪數：78.42 坪
8580萬 臺北市中山區八德路2段 坪數：107.26 坪
2億3000萬 臺北市信義區松德路 坪數：181.71 坪
1880萬 臺北市內湖區金龍路 坪數：33.14 坪
1780萬 臺北市內湖區文湖街 坪數：31.26 坪
1680萬 臺北市內湖區文德路 坪數：25.17 坪
'''
