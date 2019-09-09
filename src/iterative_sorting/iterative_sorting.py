# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j
                print ('smalles value', arr[j])

        # TO-DO: swap
        arr[cur_index], arr[smallest_index] = arr[smallest_index], arr[cur_index]



    return arr

print(selection_sort([0, 20, 10, 3, 5, 1]))

# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):

    for i in range (0, len(arr) - 1):
        current_index = i
        current_smaller_indx = current_index 

        for j in range (i + 1, len(arr)):
            if arr[current_smaller_indx] > arr[j]:
                current_smaller_indx = j

        arr[current_index], arr[current_smaller_indx] = arr[current_smaller_indx], arr[current_index]

    return arr


print(bubble_sort([3, 1, 5, 2]))

# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr