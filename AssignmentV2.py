import json

with open('precipitation.json') as json_data:
    data = json.load(json_data)
  
# Monthly totals    
january = [] 
for i in data: 
    if i['station'] == 'GHCND:US1WAKG0038' and '2010-01-' in i['date']: 
      january.append(i['value'])
            
a=sum(january)
print(a)

febuary = [] 
for i in data: 
    if i['station'] == 'GHCND:US1WAKG0038' and '2010-02-' in i['date']: 
      febuary.append(i['value'])
            
b=sum(febuary)
print(b)

march = [] 
for i in data: 
    if i['station'] == 'GHCND:US1WAKG0038' and '2010-03-' in i['date']: 
      march.append(i['value'])
            
c=sum(march)
print(c)

   
april = [] 
for i in data: 
    if i['station'] == 'GHCND:US1WAKG0038' and '2010-04-' in i['date']: 
      april.append(i['value'])
            
d=sum(april)
print(d)


may = [] 
for i in data: 
    if i['station'] == 'GHCND:US1WAKG0038' and '2010-05-' in i['date']: 
      may.append(i['value'])
           
e=sum(may)
print(e)


june = [] 
for i in data: 
    if i['station'] == 'GHCND:US1WAKG0038' and '2010-06-' in i['date']: 
      june.append(i['value'])
            
f=sum(june)
print(f)

july = [] 
for i in data: 
    if i['station'] == 'GHCND:US1WAKG0038' and '2010-07-' in i['date']: 
      july.append(i['value'])
            
g=sum(july)
print(g)

august = [] 
for i in data: 
    if i['station'] == 'GHCND:US1WAKG0038' and '2010-08-' in i['date']: 
      august.append(i['value'])
          
h=sum(august)
print(h)

september = [] 
for i in data: 
    if i['station'] == 'GHCND:US1WAKG0038' and '2010-09-' in i['date']: 
      september.append(i['value'])
            
x=sum(september)
print(x)

october = [] 
for i in data: 
    if i['station'] == 'GHCND:US1WAKG0038' and '2010-10-' in i['date']: 
      october.append(i['value'])
            
j=sum(october)
print(j)

november = [] 
for i in data: 
    if i['station'] == 'GHCND:US1WAKG0038' and '2010-11-' in i['date']: 
      november.append(i['value'])
          
k=sum(november)
print(k)

december = [] 
for i in data: 
    if i['station'] == 'GHCND:US1WAKG0038' and '2010-12-' in i['date']: 
      december.append(i['value'])
          
l=sum(december)
print(l)

assignment = a, b, c, d, e, f, g, h, x, j, k, l
with open('Assignment2.txt', 'w') as outfile:
    json.dump(assignment, outfile)


# Yearly total
monthlyPRCP = [a, b, c, d, e, f, g, h, x, j, k, l]
total = sum(monthlyPRCP)
print('TOTAL:', total)  

# Monthly Percentages
print('January:', round(a*100/total, 2), "%")
print('Febuary:', round(b*100/total, 2), "%")
print('March:', round(c*100/total, 2), "%")
print('April:', round(d*100/total, 2), "%")
print('May:', round(e*100/total, 2), "%")
print('June:', round(f*100/total, 2), "%")
print('July:', round(g*100/total, 2), "%")
print('August:', round(h*100/total, 2), "%")
print('September:', round(x*100/total, 2), "%")
print('October:', round(j*100/total, 2), "%")
print('November:', round(k*100/total, 2), "%")
print('December:', round(l*100/total, 2), "%")