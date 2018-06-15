
import urllib, urllib.request, json


#Yahoo

#client ID
consumer_key

#client secret
consumer_secret

baseurl = "https://query.yahooapis.com/v1/public/yql?"

manhattan_woeid = 12761355
nyc_woeid = 2459115



def get_nyc_weather():
    https://query.yahooapis.com/v1/public/yql?q=select%20item.condition%20from%20weather.forecast%20where%20woeid%20%3D%202487889&format=json&env=store%3A%2F%2Fdatatables.org%2Falltableswithkeys

def get_nyc_forecast(baseurl, manhattan_woeid):
    query = f'select * from weather.forecast where woeid={manhattan_woeid}&format=json'

    url = f'{baseurl}={query}'


    req = requests.get(url)


#"https://query.yahooapis.com/v1/public/yql?=select * from weather.forecast where woeid=2459115&format=json"


quandl_api_key = '&api_key=pWjXmxamqHYAMueDfPUE'

"""
Call URL: 
https://www.quandl.com/api/v3/datasets/DATABASE_CODE
    /DATASET_CODE.csv?api_key=YOUR_API_KEY_HERE

Example:
https://www.quandl.com/api/v3/datasets/CME
    /CLH2018.json?start_date=2018-01-01&api_key=pWjXmxamqHYAMueDfPUE
"""

def quandl_api_wrapper(database_code, dataset_code): #let's pull actual json off the web to practice
    
    quote_url = f'https://www.quandl.com/api/v3/datasets/{database_code}/{dataset_code}.json?'
    response = requests.get(quote_url + quandl_api_key)
    return response.json()


if __name__ == "__main__":
    print('APIs are ready')