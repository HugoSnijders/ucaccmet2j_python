import json

with open('precipitation.json') as json_data:
    data = json.load(json_data)
    #print(data)
    
january = [] 
for i in data: 
    if i['station'] == 'GHCND:US1WAKG0038' and '2010-01-' in i['date']: 
      january.append(i['value'])
      
#print(january)      
a=sum(january)
print(a)

febuary = [] 
for i in data: 
    if i['station'] == 'GHCND:US1WAKG0038' and '2010-02-' in i['date']: 
      febuary.append(i['value'])
      
#print(febuary)      
b=sum(febuary)
print(b)

march = [] 
for i in data: 
    if i['station'] == 'GHCND:US1WAKG0038' and '2010-03-' in i['date']: 
      march.append(i['value'])
      
#print(march)      
c=sum(march)
print(c)

   
april = [] 
for i in data: 
    if i['station'] == 'GHCND:US1WAKG0038' and '2010-04-' in i['date']: 
      april.append(i['value'])
      
#print(april)      
d=sum(april)
print(d)


may = [] 
for i in data: 
    if i['station'] == 'GHCND:US1WAKG0038' and '2010-05-' in i['date']: 
      may.append(i['value'])
      
#print(may)      
e=sum(may)
print(e)


june = [] 
for i in data: 
    if i['station'] == 'GHCND:US1WAKG0038' and '2010-06-' in i['date']: 
      june.append(i['value'])
      
#print(june)      
f=sum(june)
print(f)

july = [] 
for i in data: 
    if i['station'] == 'GHCND:US1WAKG0038' and '2010-07-' in i['date']: 
      july.append(i['value'])
      
#print(july)      
g=sum(july)
print(g)

august = [] 
for i in data: 
    if i['station'] == 'GHCND:US1WAKG0038' and '2010-08-' in i['date']: 
      august.append(i['value'])
      
#print(august)      
h=sum(august)
print(h)

september = [] 
for i in data: 
    if i['station'] == 'GHCND:US1WAKG0038' and '2010-09-' in i['date']: 
      september.append(i['value'])
      
#print(september)      
x=sum(september)
print(x)

october = [] 
for i in data: 
    if i['station'] == 'GHCND:US1WAKG0038' and '2010-10-' in i['date']: 
      october.append(i['value'])
      
#print(october)      
j=sum(october)
print(j)

november = [] 
for i in data: 
    if i['station'] == 'GHCND:US1WAKG0038' and '2010-11-' in i['date']: 
      november.append(i['value'])
      
#print(november)      
k=sum(november)
print(k)

december = [] 
for i in data: 
    if i['station'] == 'GHCND:US1WAKG0038' and '2010-12-' in i['date']: 
      december.append(i['value'])
      
#print(december)      
l=sum(december)
print(l)

assignment = a, b, c, d, e, f, g, h, x, j, k, l
with open('Assignment2.txt', 'w') as outfile:
    json.dump(assignment, outfile)