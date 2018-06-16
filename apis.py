
import urllib, urllib.request
import json
import requests


#Yahoo

#client ID
consumer_key = 'dj0yJmk9V05KSmFNTGhXb0REJmQ9WVdrOVRrcHBRVmQwTkdrbWNHbzlNQS0tJnM9Y29uc3VtZXJzZWNyZXQmeD03ZA--'

#client secret
#consumer_secret

y_base_url = "https://query.yahooapis.com/v1/public/yql?q"

manhattan_woeid = 12761355
nyc_woeid = 2459115


def get_nyc_weather(baseurl, manhattan_woeid):
    query = f'select item.condition from weather.forecast where woeid={manhattan_woeid}&format=json'
    url = f'{baseurl}={query}'
    #return url
    response = requests.get(url)
    response = response.json()
    conditions = response['query']['results']['channel']['item']['condition']
    return conditions

def get_nyc_forecast(baseurl, manhattan_woeid):
    query = f'select * from weather.forecast where woeid={manhattan_woeid}&format=json'
    url = f'{baseurl}={query}'
    #return url
    response = requests.get(url)
    return response.json()



#Quandl


quandl_api_key = '&api_key=pWjXmxamqHYAMueDfPUE'



"""
Call URL: 
https://www.quandl.com/api/v3/datasets/DATABASE_CODE
    /DATASET_CODE.csv?api_key=YOUR_API_KEY_HERE

Example:
https://www.quandl.com/api/v3/datasets/CME
    /CLH2018.json?start_date=2018-01-01&api_key=pWjXmxamqHYAMueDfPUE
"""


def quandl_api_wrapper(database_code, dataset_code): #CME, CLH2018
    quote_url = f'https://www.quandl.com/api/v3/datasets/{database_code}/{dataset_code}.json?'

    response = requests.get(quote_url + quandl_api_key)
    return response.json()


#Census


#Census American Community Survey
census_base_url = 'https://api.census.gov/data'

census_query = '?get='

def append_dataset_parameters(*args)
    dataset_parameters = ''.join(["/" + arg for arg in args])

query_url = base_url + dataset_parameters + census_query


if __name__ == "__main__":
    print('APIs are ready')
    conditions = get_nyc_weather(y_base_url, manhattan_woeid)
    print(conditions['text'], conditions['temp'])
