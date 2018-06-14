

def simple_generator(n):
    for i in range(n):
        yield i


#jeff knupp example

def select_primes(values): #receive pre-existing list and return all primes
    return [n for n in values if is_prime(n)]

def gen_primes(n): #generate primes one at a time to preserve space
    while True: #the while loop continuously increments n and yields if prime
        if is_prime(n):
            yield n
        n += 1

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


def euler_10(n): #sum all primes >= n, <= 2,000,000
    total = 2
    for next_prime in gen_primes(n):
        if next_prime < 2000000:
            total += next_prime
        else:
            return total #return ends the for loop and the while in the generator

#pass a value to a generator
def primes_gt_successive_values(iterations, base):
    prime_generator = gen_primes_from_base(base)
    prime_generator.send(None) #initiate generator
    for power in range(iterations):
        print(prime_generator.send(base ** power))


def gen_primes_from_base(n):
    while True:
        if is_prime(n):
            n = yield n #this line receives the next value
        n += 1

if __name__ == "__main__":
    print('Generators are ready to yield')
    print('Create generator object: gen = simple_generator(10)')
    gen = simple_generator(10)
    print('Iterate generator:')
    print('next(gen): ', next(gen))
    print('next(gen): ', next(gen))
    print('next(gen): ', next(gen))
    
