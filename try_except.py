
def zero_division(dividend, divisor):
    try:
        result = dividend/divisor
    except ZeroDivisionError as e:
        print("You're attempting to divide by zero")


def end_of_file(file):



def key_error(key, data=None):
    if data is None:
        data = {'test':'passed', 1:'chocolate', 3:'vanilla'}
    try:
        val = data[key]
    except KeyError as e:
        print("That key is not in your data")




def type_error_date(string):



def type_error_int(number):




if __name__ == "__main__":
    print("Try...Except is available")