#  爬蟲學習筆記
> Web Scraping with Python by Ryan Mitchell

---

# Scraping JavaScript

## Ajax

#### 當看到的頁面和抓回來的source code不一樣

1. Ajax傳送或接收server的資訊時, 並不需要重新載入頁面或發送另一個頁面的請求
2. 或是被重新導向到別的網站

#### solution

1. scrapy content directly from JavaScript (without python)
2. use Python package to execute js then scrapy
    - e.g. selenium

## Selenium

install selenium
```bash
pip install selenium
```

use [**Phantom JS**](http://phantomjs.org/download.html) to run quietly in background
1. load website into memory
2. execute js on the page
3. no any graphic rendering of the website to the user 


