import requests

url = 'http://localhost:5000/results'
r = requests.post(url,json={'Name':7, 'Location':8, 'Year':2015,'Kilometers_Driven':69140,
'Fuel_Type':1,'Transmission':1,'Car_age':7,'Owner_Type':0,'Mileage':20.46,'Engine':1461.000000,'Power':
83.800000,'Seats':5.0})

print(r.json())
