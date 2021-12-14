
#creates trello card
# initial poc version mika.nokka1@gmail.com Dec 2021

  #print ("Card id: {0}".format(card_id))

import requests
import os 
import sys


def main(argv):

    #Get env variables from file (do not store to Github)
    token=GetEnvVar("TOKEN") # set in trello account settin
    key=GetEnvVar("KEY") #h ttps://trello.com/app-key
    list_id=GetEnvVar("LISTID") # the id for your list, add .json end of trello  url and find list: id:
 
    
    card_name="kissa-testi"

    url = f"https://api.trello.com/1/cards"
    querystring = {"name": card_name, "idList": list_id, "key": key, "token": token} # full restapi: https://developer.atlassian.com/cloud/trello/rest/api-group-cards/#api-cards-post
    response = requests.request("POST", url, params=querystring)
    print ("response: {0}".format(response))
    #print ("Got full json: {0}".format(response.json()))
 

 

def GetEnvVar(variable):

    if (variable in os.environ):
        #value=os.environ[variable]
        value=os.environ.get(variable)
        print("OK.Env variable {0} found. Value:{1}".format(variable,value))
        return str(value)
    else:
        print("Error.Env variable {0} NOT found.EXITING!!".format(variable))
        sys.exit(5)
   
    
    
if __name__ == "__main__":
    main(sys.argv[1:]) 