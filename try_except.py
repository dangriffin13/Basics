
import datetime

def zero_division(dividend, divisor):
    try:
        result = dividend/divisor
        return result
    except ZeroDivisionError:
        print("You're attempting to divide by zero")

    except Exception as e:
        print('This function failed due to: ', e)
    


def end_of_file(file):
    pass


def key_error(key, data=None):
    if data is None:
        data = {'test':'passed', 1:'chocolate', 3:'vanilla'}
    try:
        val = data[key]
        return val
    except KeyError:
        print("That key is not in your data")
    


def assert_error_number_positive(number):
    try:
        assert number > 0
        print('Your number is positive')

    except AssertionError:
        print('You did not enter a positive number')

    except Exception as e:
        print('This function failed due to: ', e)




def type_error_date(*args):
    try:
        saved_date = datetime.date(*args)
        return saved_date

    except TypeError:
        print("Your input cannot be converted into a date")

    #syntax error occurs before runtime
    #saved_date = eval('datetime.date({})'.format(','.join(args)))
    #except SyntaxError:
        #for arg in args:
            #if str(arg)[:1] == '0':
                #print('You cannot use leading zeros on your numbers')
            #else:
                #print('Unknown Syntax Error')
    

def type_error_int(number):
    try:
        n = int(number)
        return n
    except TypeError:
        print("Your input cannot be converted into an integer")



def two_exception_same_handler(number):
    try: #convert number to char using ascii code
        letter = chr(number)
        print(number, letter)

    except (ValueError, TypeError) as e:
        print("Invalid input.  You need a number between 0 and 1,114,111")



if __name__ == "__main__":
    print("Try...Except is available")
