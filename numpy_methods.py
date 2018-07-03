import numpy as np
import matplotlib.pyplot as plt


arr_zeroes = np.zeros(5) #five zeroes
arr_ones = np.ones(5) #fives ones


odds = np.arange(1,11,2) #integers, start, stop, step
evens = np.arange(1,10,2)


#linear values, start, stop, number of values
lin1 = [round(i, 3) for i in np.linspace(0,10,10)]
lin2 = np.linspace(0,10,9)
lin3 = np.linspace(1,10,10)
#lin4 = [round(i, 3) for i in np.linspace(0,11,10)]


#matrix
mx_2x3 = np.ones((2,3)) #2 rows of 3 values
mx_5x2 = np.ones((5,2)) #5 rows of 2 values

#identity matrix
id_matrix_3 = np.eye(3)
id_martix_8 = np.eye(8)


#random values, uniformly [0-1)
arr_rand = np.random.rand(10)
mx_rand = np.random.rand(3,3)

#random values with range [low, high): low, high, n
arr_randint = np.random.randint(0,100,30)


#change shape of matrix; must have correct number of elements
arr_reshape = arr_randint.reshape(3, 10)

#find shape
shape_of_reshape = np.shape(arr_reshape) #(3,10)

#random normal dist
def gen_random_normal_dist(n):
    return np.random.randn(n)


def plot_bell_curve():
    plt.hist(gen_random_normal_dist(200), bins=7, ec='black')
    plt.show()

if __name__ == "__main__":
    print("Numpy operations available")

    print(lin1)
    print(lin2)
    print(lin3)

    bell_curve = gen_random_normal_dist(200)
    

