
#creates trello card
# initial poc version mika.nokka1@gmail.com Dec 2021
# Requires env variables TOKEN,KEY and LISTID for Trello authorization
# See comments below how to find them from Trelloboard
#
# In Linux one can do file which exports these variables when sourced. Do not store them to Github


import requests
import os 
import sys
import sys, logging
import argparse

__version__ = u"0.1"

logging.basicConfig(level=logging.DEBUG) # IF calling from Groovy, this must be set logging level DEBUG in Groovy side order these to be written out



def main(argv):


    parser = argparse.ArgumentParser(description="Create Trello card",
    
    
    epilog="""
    
    Requires env variables for Trello authentication to exists:
    
    TOKEN (set in trello account settings)
    
    KEY (https://trello.com/app-key)
    
    LISTID (the id for your list, add .json end of trello  url and find list: id:)
    
    
    EXAMPLE:
    
    CreateCard.py  -n CARDNAME"""

    
    )



    parser.add_argument('-v', help='Show version&author and exit', action='version',version="Version:{0}   mika.nokka1@gmail.com".format(__version__) )  
    parser.add_argument("-n",help='<Name of the new Trello Card>',metavar="cardname")

    args = parser.parse_args()
       
    CARDNAME = args.n or ''
  

    #logging.info("CARDNAME:{0}".format(CARDNAME))
    
    # quick old-school way to check needed parameters
    if (CARDNAME==''):
        logging.error("\n---> MISSING ARGUMENTS!!\n ")
        parser.print_help()
        sys.exit(2)


    #Get env variables from file (do not store to Github)
    token=GetEnvVar("TOKEN") # set in trello account settings
<<<<<<< HEAD
    key=GetEnvVar("KEY") #https://trello.com/app-key
=======
    key=GetEnvVar("KEY") #h ttps://trello.com/app-key
>>>>>>> 98ccc88d8b1f2b185b6a9c01f9e47458891b0260
    list_id=GetEnvVar("LISTID") # the id for your list, add .json end of trello  url and find list: id:
 


    url = f"https://api.trello.com/1/cards"
    querystring = {"name": CARDNAME, "idList": list_id, "key": key, "token": token} # full restapi: https://developer.atlassian.com/cloud/trello/rest/api-group-cards/#api-cards-post
    response = requests.request("POST", url, params=querystring)
    # todo: handle erros (401,404 etc)
    print ("response: {0}".format(response))
    print ("Got full json: {0}".format(response.json()))
 

 

def GetEnvVar(variable):

    if (variable in os.environ):
        #value=os.environ[variable]
        value=os.environ.get(variable)
        print("OK.Env variable {0} found. Value:{1}".format(variable,value))
        return str(value)
    else:
        print("Error.Env variable {0} NOT found.EXITING!!".format(variable))
        parser.print_help()
        sys.exit(5)
   
    
    
if __name__ == "__main__":
    main(sys.argv[1:]) 