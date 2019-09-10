import math

# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements
    # TO-DO

    for i in range(0, len(merged_arr)):
        if i <= len(arrA) - 1:
            merged_arr[i] = arrA[i]
        elif i > len(arrA) - 1:
            merged_arr[i] = arrB[i - len(arrA)]
    
    return merged_arr

print(merge([3, 2, 1], [0, 2, 6]))
# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    arr1 = []
    arr2 = []
    sorted_arr = []
    length = len(arr)/2


    if len(arr) > 1:
        if len(arr) % 2 != 0:
            arr1 = arr[0:math.ceil(length)]
            arr2 = arr[math.floor(length)+1:]
        
        if len(arr) % 2 == 0:
            arr1 = arr[:round(length)]
            arr2 = arr[round(length):]

    if(len(arr1) > 1 and len(arr2) == 1):
        sorted_arr = arr2[0]

    if(len(arr1) == 1 and len(arr2) == 1):
        if arr1[0] > arr2[0]:
            sorted_arr = merge(arr2, arr1)
        else:
            sorted_arr = merge(arr1, arr2)

    if len(arr1) > 1:
        print(merge_sort(arr1))

    if len(arr2) > 1:
        print(merge_sort(arr2))


   


    # if len(arr2) > 1:
    #     print(merge_sort(arr2))


    # if len(arr2) > 1:
    #     print(merge_sort(arr2))

    # if(len(arr2) == 1):
    #     if arr1[0] > arr2[0]:
    #         sorted_arr2 = [arr2[0], arr1[0]]
    #     else:
    #         sorted_arr2 = [arr1[0], arr2[0]]



    return('splitted arrays', sorted_arr)

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
