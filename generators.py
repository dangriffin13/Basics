

def simple_generator(n):
    for i in range(n):
        yield i


#jeff knupp example

def is_prime(n):
    if n > 1:
        if n ==2:
            return True
        if number % 2 == 0:
            return False
        for i in range(3, int(n**.5 + 1), 2)
            if n % i == 0:
                return False
        return True
    else:
        return False

if __name__ == "__main__":
    print('Generators are ready to yield')
    print('Create generator object: gen = simple_generator(10)')
    gen = simple_generator(10)
    print('Iterate generator:')
    print('next(gen): ', next(gen))
    print('next(gen): ', next(gen))
    print('next(gen): ', next(gen))
    
