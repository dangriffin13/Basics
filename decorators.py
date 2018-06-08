
def platonic_decorator(any_function):

    def wrapper():
        print("Our wrapper decorated the function")

        any_function()

    return wrapper


@platonic_decorator
def decorated_function():
    print("This function got decorated")
#run decorated_function() to see output

def without_syntactic_sugar():
    print("This function got decorated without pie syntax")

without_syntactic_sugar = platonic_decorator(without_syntactic_sugar)
#run without_syntactic_sugar() to see output


username = 'Tim'

def access_denied():
    print('You do not have entitlements for this screen')

def check_credentials(sensitive_function):

    def wrapper(*args, **kwargs):
        if username == 'Dan':
            sensitive_function()
        else:
            access_denied()

    return wrapper

@check_credentials
def view_company_balance_sheet():
    print('Assets: $5000')
    print('____')
    print('Liabilities: $3000')
    print('____')
    print('Equity: $2000')



if __name__ == "__main__":
    print('Decorators are available')