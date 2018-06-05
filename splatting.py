
tri_args = ['first','second','third']
tri_kwargs = {'1':'first','2':'second','3':'third'}

def receive_three_splatted_args(arg1, arg2, arg3):
    print('arg1: ', arg1)
    print('arg3: ', arg3)

def receive_three_splatted_kwargs(kwarg1, kwarg2, kwarg3):
    print('kwarg1: ', kwarg1)
    print('kwarg3: ', kwarg3)

def receive_unsplatted_args(*args):
    for arg in args:
        print(arg)

def receive_unsplatted_kwargs(**kwargs):
    for key, val in kwargs:
        print(key, value)





if __name__ == "__main__":
    print("Splat operations up and running")
    print('tri_args: ', tri_args)
    print('splat tri_args: ')
    receive_three_splatted_args(*tri_args)
    print('tri_kwargs: ', tri_kwargs)
    print('splat tri kwargs: ')
    receive_three_splatted_kwargs(**tri_kwargs)
