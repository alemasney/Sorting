# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    for i in range(len(arr)):
       
        index = i
        for n in range(index, len(arr)):
            if arr[index] > arr[n]:
                index = n

        temp = arr[i]
        arr[i] = arr[index]
        arr[index] = temp


    return arr

print(selection_sort([1, 5, 8, 4, 2, 9, 6, 0, 3, 7]))

# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    swap = True

    while swap:
        swap = False
        for i in range(len(arr)-1):
            if arr[i] > arr[i+1]:
                temp = arr[i]
                arr[i] = arr[i+1]
                arr[i+1] = temp

                swap = True
        
    return arr

print(bubble_sort([1, 5, 8, 4, 2, 9, 6, 0, 3, 7]))


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr