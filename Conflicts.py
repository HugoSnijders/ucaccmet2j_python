import json
import csv


with open('conflict_data_full_lined.json') as file:
    data = json.load(file)

with open('UCDPconflictdata.csv', 'w', newline='') as file:
    csvwriter = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_NONNUMERIC)
    
    csvwriter.writerow(['country', 'year', 'type_of_violence', 'dyad_name', 'latitude', 'longitude', 'region', 'deaths_a', 'deaths_b', 'best', 'high', 'low'])
    for line in data: 
       if int(line['year']) >= 2000 :  # Making the year lines into integers, and selecting for the last two decades
           csvwriter.writerow([line['country'], line['year'], line['type_of_violence'], line['dyad_name'], line['latitude'], line['longitude'], line['region'], line['deaths_a'], line['deaths_b'], line['best'], line['high'], line['low']]) 


  