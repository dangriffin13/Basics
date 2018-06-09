

def linear_search(arr, value): #O(n)
    cnt = 0
    while cnt < len(arr):
        if value == arr[cnt]:
            return cnt
        cnt += 1
    return "Value not found."


def binary_search(arr, value): #O(log n)
    if not arr:
        return "You didn't provide any values to search."
    lower, upper = 0, len(arr) - 1
    while lower <= upper:
        mid = (upper + lower)//2

        if arr[mid] == value:
            return f"{value} is at position {mid}"
        elif arr[mid] > value:
            upper = mid - 1
        elif arr[mid] < value:
            lower = mid + 1
        else:
            return f"{value} not found."




def bubble_sort(arr):
    for i in range(len(arr)):
        j = 0
        while j < len(arr)-i-1:
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
            j += 1

    #confirmation
    while i < len(arr):
        if arr[i] <= arr[i+1]:
            i+=1
        else:
            raise Exception("Not in ascending order (position", i, ")")


def insertion_sort(arr):
    for i in range(1, len(arr)):
        val = arr[i]
        position = i
        while position > 0 and arr[position-1] > val:
            arr[position] = arr[position - 1] #swap with prior value
            position = position - 1
        arr[position] = val


def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        left = arr[:mid]
        right = arr[mid:]

        merge_sort(left)
        merge_sort(right)

        l_idx = 0 #left pointer
        r_idx = 0 #right pointer
        arr_idx = 0 #total array pointer

        while l_idx < len(left) and r_idx < len(right):
            if left[l_idx] < right[r_idx]:
                arr[arr_idx] = left[l_idx]
                l_idx += 1
            else:
                arr[arr_idx] = right[r_idx]
                r_idx += 1
            arr_idx += 1

        while l_idx < len(left):
            arr[arr_idx] = left[l_idx]
            l_idx += 1
            arr_idx += 1

        while r_idx < len(right):
            arr[arr_idx] = right[r_idx]
            r_idx += 1
            arr_idx += 1


def quick_sort(arr):


def tim_sort(arr):








if __name__ == "__main__":
    print("Sort and Search algos are available")