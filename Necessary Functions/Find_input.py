# Code to output the link of the most relavant search
import pprint
from pydoc import describe
from re import S
import requests
# To Get Search Result we search the query o wiki data search box utilise the most relevant search
API_ENDPOINT = "https://www.wikidata.org/w/api.php"
query = input('Search Here ')

params = {
    'action': 'wbsearchentities',
    'format': 'json',
    'language': 'en',
    'search': query
}

r = requests.get(API_ENDPOINT, params = params)
Data = r.json()['search'][0]
print(r.json()['search'][0])
# Note : its just a function