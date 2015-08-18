import requests
import re
import json
res = requests.get('http://www.oanda.com/currency/historical-rates/')
reg = re.search('("data":\[\[.*\]\])',res.text)

data = json.loads('{'+reg.group(1)+'}')
print data
