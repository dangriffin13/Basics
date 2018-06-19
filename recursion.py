

def nested_dictionary(d): 
    for key, value in d.items():
        if isinstance(value, dict):
            print(key,":")
            nested_dictionary(value)
        else:
            print('{0}: {1}'.format(key, value))




if __name__ == '__main__':
    print('Recursive functions are available')