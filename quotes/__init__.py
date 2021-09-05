'''
    Module to handle quote requests
'''
import requests
import json
# Function to fetch a random quote


def get_quote() -> str:
    '''
        Returns a random quote from the quote API
    '''
    response = requests.get("https://www.zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + " - " + json_data[0]['a']
    return quote
