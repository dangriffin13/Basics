

def percent_method(string):
    print("This prints your string - %s - using the percentage method." % string)

def format_method(string):
    print("This prints your string - {} - using the percentage method.".format(string))

def f_method(string):
    print(f"This prints your string - {string} - using the f-string method.")


def f_method_with_dictionary(*args,**kwargs):
    for kwarg in kwargs:
        print(kwarg, kwargs[kwarg])

    print(f"The user {user}'s status is {status}")


if __name__ == "__main__":
    string = input('Enter a string: ')

    percent_method(string)
    format_method(string)
    f_method(string)
