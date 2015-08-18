import requests
import re
import json
res = requests.get('http://www.oanda.com/currency/historical-rates/')
reg = re.search('("data":\[\[.*\]\])',res.text)

data = json.loads('{'+reg.group(1)+'}')
print data

'''

{u'data': [[1439856000000L, 0.9015], [1439769600000L, 0.8998], [1439683200000L, 0.8998], [1439596800000L, 0.8974], [1439510400000L, 0.898], [1439424000000L, 0.8996], [1439337600000L, 0.9072], [1439251200000L, 0.9112], [1439164800000L, 0.9116], [1439078400000L, 0.9116], [1438992000000L, 0.9148], [1438905600000L, 0.9166], [1438819200000L, 0.9193], [1438732800000L, 0.9133], [1438646400000L, 0.9116], [1438560000000L, 0.9102], [1438473600000L, 0.9102], [1438387200000L, 0.9111], [1438300800000L, 0.9129], [1438214400000L, 0.9051], [1438128000000L, 0.9038], [1438041600000L, 0.905], [1437955200000L, 0.9099], [1437868800000L, 0.9099], [1437782400000L, 0.9116], [1437696000000L, 0.9119], [1437609600000L, 0.9153], [1437523200000L, 0.9201], [1437436800000L, 0.9226], [1437350400000L, 0.9232]]}

'''