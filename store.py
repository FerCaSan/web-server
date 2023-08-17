
"""Accediendo y obteniendo datos de una API"""

import requests


def get_categories():
    r = requests.get('https://api.escuelajs.co/api/v1/categories')

    #get request state
    print(r.status_code)
    #Output: 200

    #View request
    print(r.text)
    #Output: [{"id":1,"name":"Clothes","image":"https://picsum.photos/640/640?r=5831"
    #           ,"creationAt":"2023-08-15T18:04:12.000Z","updatedAt":"2023-08-15T18:04:12.000Z"}
    #           ,{"id":2,"name":"New name of category","image":"https://picsum.photos/640/640?r=7890"
    #           ,"creationAt":"2023-08-15T18:04:12.000Z","updatedAt":"2023-08-15T19:49:45.000Z"},...

    print(type(r.text))

    #Read in json format
    categories = r.json()
    for category in categories:
        print(category['name'])


