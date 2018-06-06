
tri_args = ['first','second','third']
tri_kwargs = {'one':'first','two':'second','three':'third'}

def receive_three_splatted_args(arg1, arg2, arg3):
    print('arg1: ', arg1)
    print('arg3: ', arg3)

def receive_three_splatted_kwargs(one,two,three):
    print('kwarg1: ', 'one')
    print('kwarg3: ', 'three')

def receive_unsplatted_args(*args):
    for arg in args:
        print(arg)

def receive_splatted_kwargs(**kwargs):
    for key, val in kwargs.items():
        print(key, val)





if __name__ == "__main__":
    print("Splat operations up and running")
    print('tri_args: ', tri_args)
    print('splat tri_args: ')
    receive_three_splatted_args(*tri_args)
    print('tri_kwargs: ', tri_kwargs)
    print('send splatted tri kwargs: ')
    receive_three_splatted_kwargs(**tri_kwargs)
    print('send tri_kwargs dict and splat in function: ')
    receive_splatted_kwargs(**tri_kwargs)


