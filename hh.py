import requests
import pprint
import json


url = 'https://api.hh.ru/vacancies'

where = input('Где искать вакансию?')
query_string = input('Строка запроса?')

params = {
    'text': 'NAME:("python developer")',
    "id":"1",
    "parent_id":"113",
    "name":"Москва",
    "areas":[],
    'page': 1
}

result = requests.get(url, params=params).json()


items = result['items']

all_vacancies=result['found']

first = items[1]

requirements={}
requirements['keywords']='python developer'
requirements['count']=all_vacancies
requirements['requirements']=[]

list_1=[]

for i in items:
    for n, y in i['snippet'].items():
        y1=str(y).split('. ')
        y1 = list(y1)
        list_1.append(y1)


for i in list_1:
    for n in i:
        requirements['requirements'].append({
            'name': n,
            'count':str(list_1).count(n),
            'persent': round(str(list_1).count(n)/all_vacancies*100,2)
     })

pprint.pprint(requirements)

with open('data.txt', 'w') as outfile:
    json.dump(requirements, outfile)



