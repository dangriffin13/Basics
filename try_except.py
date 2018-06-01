
import datetime

def zero_division(dividend, divisor):
    try:
        result = dividend/divisor
        return result
    except ZeroDivisionError as e:
        print("You're attempting to divide by zero")
    


def end_of_file(file):
    pass


def key_error(key, data=None):
    if data is None:
        data = {'test':'passed', 1:'chocolate', 3:'vanilla'}
    try:
        val = data[key]
        return val
    except KeyError as e:
        print("That key is not in your data")
    


def assertion_error():
    pass



def type_error_date(*args):
    try:
        saved_date = datetime.date(*args)
        return saved_date
    except TypeError:
        print("Your input cannot be converted into a date")

    for arg in args:
        if str(arg)[:1] == '0':
            print('You cannot use leading zeros on your numbers')
    

def type_error_int(number):
    try:
        n = int(number)
        return n
    except TypeError:
        print("Your input cannot be converted into an integer")


    


def two_exception_check(data):
    pass



if __name__ == "__main__":
    print("Try...Except is available")
