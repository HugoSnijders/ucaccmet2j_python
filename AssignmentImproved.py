
import json

with open('precipitation.json') as json_data:
    data = json.load(json_data)
    
monthlyPRCP = [0] * 12
for i in data:
    if i['station'] == 'GHCND:US1WAKG0038':
      month = int(i['date'][5:7]) 
      monthlyPRCP[month-1] += i['value']
      
print(monthlyPRCP)      
      
      