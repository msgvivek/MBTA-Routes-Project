import requests
import pprint
import data

x= data.b.get('data')

for element in x:
  # finding long_name
  if 'attributes' in element.keys():
    print(element.get('attributes').get('long_name'))
