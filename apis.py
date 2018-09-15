
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


def get_weather(woeid):
    query = f'select item.condition from weather.forecast where woeid={woeid}&format=json'
    url = f'{y_base_url}={query}'
    response = requests.get(url).json()
    conditions = response['query']['results']['channel']['item']['condition']
    return conditions

def get_nyc_weather():
    query = f'select item.condition from weather.forecast where woeid={manhattan_woeid}&format=json'
    url = f'{y_base_url}={query}'
    response = requests.get(url).json()
    conditions = response['query']['results']['channel']['item']['condition']
    return conditions

def get_nyc_forecast():
    query = f'select * from weather.forecast where woeid={manhattan_woeid}&format=json'
    url = f'{y_base_url}={query}'
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


def quandl_api_start_date(database_code, dataset_code, start_date): #CME, CLH2018
    #start date must be yyyy-mm-dd
    quote_url = f'https://www.quandl.com/api/v3/datasets/' \
        '{database_code}/{dataset_code}.json?start_date={start_date}'

    response = requests.get(quote_url + quandl_api_key)
    return response.json()


murl = f'https://www.quandl.com/api/v3/datasets/CME/CLH2018.json?start_date=2018-01-04&api_key=pWjXmxamqHYAMueDfPUE'

#start_date={start_date}'

#Census

"""
Population Estimates and Community Survey URL:
https://api.census.gov/data/YYYY/DATASET_CODE/
    ?get=VARIABLE_1/...VARIABLE_n

Time Series URL:
https://api.census.gov/data/timeseries/
    DATAESET_CODE_1/...DATSET_CODE_n/?get=VARIABLE_1,...VARIABLE_n
    &YEAR=YYYY&MONTH=MM

Example, Housing Vacancies:
https://api.census.gov/data/timeseries/eits/hv/?get=
    cell_value,data_type_code,time_slot_id,error_data,category_code,seasonally_adj
    &time=2016-Q1
"""

#Census American Community Survey
census_base_url = 'https://api.census.gov/data'

census_query = '?get='



def append_dataset_codes(*args): #forward slash delimited
    codes = ''.join(["/" + arg for arg in args])
    return codes

def append_dataset_variables(*args): #comma delimited
    variables = ','.join([arg for arg in args])
    return variables

def set_dataset_parameters(*args):
    pass

#dataset_parameters = set_dataset_parameters()

#query_url = census_base_url + dataset_parameters + census_query


if __name__ == "__main__":
    print('APIs are ready')
    conditions = get_nyc_weather()
    print(conditions['text'], conditions['temp'])
