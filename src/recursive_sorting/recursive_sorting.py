# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    merged_arr = []
    # TO-DO
        # create an index to increment
    left_index = 0
    right_index = 0
    while len(arrA) > left_index and right_index < len(arrB):
        # compare first element with the next element to see witch is smaller
        if arrA[left_index] < arrB[right_index]:
            merged_arr.append(arrA[left_index])
            left_index += 1
        else:
            merged_arr.append(arrB[right_index])
            right_index += 1
            # swap if first smaller is true

    merged_arr += arrA[left_index:] + arrB[right_index:]

    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    
    if len(arr) <= 1:
        return arr

    midpoint = len(arr) // 2
    left_arr = merge_sort(arr[:midpoint])
    right_arr = merge_sort(arr[midpoint:])

    return merge(left_arr, right_arr)


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
