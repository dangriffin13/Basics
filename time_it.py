
import timeit

def loop_without_args():
    return [i for i in range(10)]

def loop_timing(n):
    return [i for i in range(n)]


def wrapper(func, *args, **kwargs):
    def wrapped():
        return func(*args, **kwargs)
    return wrapped



if __name__ == "__main__":
    print("Timeit functions available")
    
    print(timeit.timeit(loop_without_args))

    rng = 50
    wrapped = wrapper(loop_timing, rng)
    print(timeit.timeit(wrapped))
