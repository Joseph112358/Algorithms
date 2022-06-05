def bubble_sort(arr):
    n = len(arr)
    # Traverse through all elements in array
    for i in range(n-1):
        for j in range(0,n-i-1):
            if arr[j] > arr[j+1]:
                #this statment just swaps the elements.
                arr[j], arr[j+1] = arr[j+1], arr[j] 
        

arr_test = [2,4,3,1,5,4]
bubble_sort(arr_test)
print(arr_test)

