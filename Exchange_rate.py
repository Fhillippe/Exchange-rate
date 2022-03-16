import  requests
import json


url = "https://currency-converter5.p.rapidapi.com/currency/list"

headers = {
    'x-rapidapi-host': "currency-converter5.p.rapidapi.com",
    'x-rapidapi-key':
    }




def exchange_rate(from_currency: str,to_currency: str) ->float:
    

    api_requests = requests.get(url, headers=headers, params = querystring)

    api = json.loads(api_requests.content)




    return api["rates"][to_currency]["rate"]


def currency_list() :
    
    api_requests = requests.get(url, headers=headers)

    api = json.loads(api_requests.content)




    return api['currencies']

