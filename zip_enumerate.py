
def enumerate_inputs(data):
    enumerated = enumerate(data)
    print('Printing enumerated items...')
    for item in enumerated:
        print(item)


def zip_two_inputs(iterable1, iterable2):
    zipped = zip(iterable1, iterable2)
    print('Printing zipped items...')
    for item in zipped:
        print(item)



if __name__ == "__main__":
    print('Zip and enumerate functions are ready')

    arr1 = ['a','b','c','d','e']
    arr2 = ['alpha','beta', 'gamma', 'delta', 'epsilon']

    print('list 1 (variable name arr1): ', arr1)
    print('list 2 (variable name arr2): ', arr2)

    enumerate_inputs(arr1)
    zip_two_inputs(arr1,arr2)
