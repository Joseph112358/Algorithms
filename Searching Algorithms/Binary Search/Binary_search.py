def binary_search(arr,item):
    start_index = 0
    end_index = len(arr)-1

    while start_index <= end_index:
        midpoint = start_index + (end_index - start_index) // 2
        midpoint_value = arr[midpoint]
        if midpoint_value == item:
            return midpoint
        elif item < midpoint_value:
            end_index = midpoint - 1
        else:
            start_index = midpoint + 1
    return None

arr = [1,2,4,5,8,12,18]
print(binary_search(arr,12))

     
