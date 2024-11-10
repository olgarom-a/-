# Ольга Ромашова, 23А когорта - дипломный проект
import configuration
import requests
import data

def post_order(order):
    return requests.post(configuration.URL_SERVICE + configuration.CREATING_AN_ORDER,
        json = order,
        headers = data.headers)

response = post_order(data.creating_an_order)
print(response.status_code)
print(response.json())

def get_order(track):
    return requests.get(configuration.URL_SERVICE + configuration.RECEIVING_AN_ORDER + str(track))

print(response.status_code)
