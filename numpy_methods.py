import numpy as np


arr_zeroes = np.zeros(5) #five zeroes
arr_ones = np.ones(5) #fives ones


odds = np.arange(1,11,2) #integers, start, stop, step
evens = np.arange(1,10,2)


#linear values, start, stop, number of values
lin1 = np.linspace(0,10,10)
lin2 = np.linspace(0,10,9)
lin3 = np.linspace(1,10,10)
lin4 = np.linspace(0,11,10)


#identity matrix
id_matrix_3 = np.eye(3)
id_martix_8 = np.eye(8)


#random values, uniformly [0-1)
arr_rand = np.random.rand(10)
mx_rand = np.random.rand(3,3)

#random normal dist
def gen_random_normal_dist(n):
    return np.random.rand(n)

if __name__ == "__main__":
    print("Numpy operations available")

    print(lin1)
    print(lin2)
    print(lin3)
    print(lin4)

    bell_curve = gen_random_normal_dist(50)