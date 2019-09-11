import math

# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge( arrA, arrB ):
 
    merged_arr = []
    a_index = 0
    b_index = 0
    # TO-DO

    while a_index < len(arrA) and b_index < len(arrB):
        if arrA[a_index] < arrB[b_index]:
            merged_arr.append(arrA[a_index])
            a_index +=1
        else:
            merged_arr.append(arrB[b_index])
            b_index +=1

    merged_arr.extend(arrB[b_index:])
    merged_arr.extend(arrA[a_index:])

    return merged_arr

print(merge([1, 2, 3, 10], [0, 2, 6, 8]))
# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):

    if len(arr) <= 1:
        return arr

    middle = int(len(arr) / 2)
    
    left = merge_sort(arr[:middle])
    right = merge_sort(arr[middle:])

    return merge(left, right)
   


print(merge_sort([38, 27, 43, 3, 9, 82, 10]))

# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr


# 1. Step one:

# Pass an array to the merge sort function, then I want to check for the length of array, so it is bigger than 1, so if it'so
# bigger than 1, I want to split array into two halfs.

# And If first half's length is bigger than one, I want to call merge sort function again and split 
# arr1 into two halfs etc until my arr1 and arr2
# will be of length 1