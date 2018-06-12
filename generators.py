

def simple_generator(n):
    for i in range(n):
        yield i



if __name__ == "__main__":
    print('Generators are ready to yield')
    print('Create generator object: gen = simple_generator(10)')
    gen = simple_generator(10)
    print('Iterate generator:')
    print('next(gen): ', next(gen))
    print('next(gen): ', next(gen))
    print('next(gen): ', next(gen))
    print('next(gen): ', next(gen))
