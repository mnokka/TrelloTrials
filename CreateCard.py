
#creates trello card
# initial poc version mika.nokka1@gmail.com Dec 2021

import requests


#log into trello and find following values (do not store to github):
list_id = "" #the id for your list, add .json end of trello  url and find list: id:
key = "" #https://trello.com/app-key
token = "" # in trello account settings, https://trello.com/1/authorize?expiration=never&scope=read,write,account&response_type=token&name=Server%20Token&key=05025e2c8015308b5601ac75c9fb60ce


card_name="kissa-testi"

url = f"https://api.trello.com/1/cards"
querystring = {"name": card_name, "idList": list_id, "key": key, "token": token} # full restapi: https://developer.atlassian.com/cloud/trello/rest/api-group-cards/#api-cards-post
response = requests.request("POST", url, params=querystring)
card_id = response.json()["id"]
print ("Got full json: {0}".format(response.json()))
print ("Card id: {0}".format(card_id))


