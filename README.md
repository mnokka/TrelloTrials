# TrelloTrials
POC how to use REST API for Trello card creations

Porgram creates one Trello card as an exmaple "howto"
It requires following env variables to exists. Variables are defining Trelloboard and authorization tokens

TOKEN  --> set in trello account settings

KEY --> https://trello.com/app-key

LISTID --> the id for your list, add .json end of trello  url and find list: id: from the json list.



In Linux one can have env setting file which exports  (when sourced to shell) these values to env variables. Do not store this file to Github. If one gives these values via command args, they can be observed from shell history. Python also offers some key storage libs.

 
 USAGE:
 
 python3 CreateCard.py -n "name of the new Trello card"
 
    
