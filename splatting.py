
tri_args = ['first','second','third']
tri_kwargs = {'one':'first','two':'second','three':'third'}

def receive_three_named_args(arg1, arg2, arg3):
    print('arg1: ', arg1)
    print('arg3: ', arg3)

def receive_three_named_kwargs(one,two,three):
    print('kwarg one: ', one)
    print('kwarg three: ', three)

def receive_splatted_args(*args):
    for arg in args:
        print(arg)


def receive_splatted_kwargs(**kwargs):
    for key, val in kwargs.items():
        print(key, val)





if __name__ == "__main__":
    print("Splat operations up and running")
    print('tri_args: ', tri_args)
    print('splat pre-named tri_args: ')
    receive_three_named_args(*tri_args)
    print('send list and splat in function: ')
    receive_splatted_args(*tri_args)
    print('____')
    print('tri_kwargs: ', tri_kwargs)
    print('send splatted dict to pre-named vars: ')
    receive_three_named_kwargs(**tri_kwargs)
    print('send tri_kwargs dict and splat in function: ')
    receive_splatted_kwargs(**tri_kwargs)
    print('send key:val pairs individually: ')
    receive_splatted_kwargs(test1='first_val',test2='second_val')


