
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


"https://query.yahooapis.com/v1/public/yql?=select * from weather.forecast where woeid=2459115&format=json"

if __name__ == "__main__":
    print('APIs are ready')