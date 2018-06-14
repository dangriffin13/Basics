import csv, json

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


def json_api_wrapper(): #let's pull actual json of the web to practice
    pass

def read_json(data):
    pass

def write_json_to_text(filename, content):
    pass

if __name__ == "__main__":
    print("Read/Write Operations are available")

    values_read = read_from_text('read_text.txt')
    print('Read from read_text.txt: ',values_read)