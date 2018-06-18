import csv
import json
import requests

def read_from_text(filename):
    f = open(filename, 'r')
    #f = open('read_text.txt', 'r')
    #all_at_once = f.read()
    #one_line_at_a_time = f.readline()
    all_lines_delimited = f.readlines()
    return all_lines_delimited
    f.close()

def write_to_text(filename, content):
    f = open(filename, 'w')
    f.writelines(content)

    #f = open('file_to_write.txt', 'w')
    #lines = ['Row1\n', 'Row2\n','Row3|Row3.1|Row3.2\n','Row4\n']
    #f.writelines(lines)
    f.close

def append_to_text(filename, content):
    f = open(filename, 'a')
    f.writelines(content)

    #f = open('file_to_write.txt', 'a')
    #f.writelines(['row5\n','row6\n'])
    f.close()


json_data = {
        "teams":[
            {
                "city": "New York",
                "mascot": "Yankees"
            },
            {
                "city": "Boston",
                "mascot": "Red Sox"
            }
        ]
}


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


def write_json(data):
    with open('json_practice.json', 'w') as write_file:
        json.dump(data, write_file)


def read_json(filename):
    #filename = 'json_practice.json'
    with open(filename, 'r') as read_file:
        data = json.load(read_file)
    return data


def write_json_to_text(filename, content):
    pass


if __name__ == "__main__":
    print("Read/Write Operations are available")

    #values_read = read_from_text('read_text.txt')
    #print('Read from read_text.txt: ',values_read)

    print('Write dictionary to json file')
    write_json(json_data)

    print('Pull JSON from Quandl API')
    crude_oil = quandl_api_wrapper('CME','CLH2018')


    

