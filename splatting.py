

def receive_three_splatted_args(arg1, arg2, arg3):
    pass

def receive_three_splatted_kwargs(kwarg1, kwarg2, kwarg3):
    pass

def receive_unsplatted_args(*args):
    for arg in args:
        print(arg)

def receive_unsplatted_kwargs(**kwargs):
    for key, val in kwargs:
        print(key, value)





if __name__ == "__main__":
    print("Splat operations up and running")