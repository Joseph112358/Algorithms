# Bubble sort is a sorting algorithm in which adjacent pairs of it are compared and swapped depending on which is bigger
- It has a time complexity of O(n^2) due to a nested for loop
- It has a space complexity of O(1) as no additional memory space is required

## Example: I will walk through the first j loop, but leave a trace table at the bottom for the rest as its quite long.
array = [2,4,3,1,5,4] \
bubble_sort(array) \
*length of array* n = 6 \
i = 0, j = 0 \
**For i in range(0, n-1) -> 0 to 5** \
  **For j in range(0,n-1-i)**
  *is arr[j] > arr[j+1]? -> is 2 > 4? no* \
[2,4,3,1,5,4] *j + 1 = 1* \
*is arr[j] > arr[j+1]? -> is 4 > 2? yes therefore swap* \
[2,3,4,1,5,4] *j + 1 = 2* \
*is arr[j] > arr[j+1]? -> is 4 > 1? yes therefore swap* \
[2,3,1,4,5,4] *j + 1 = 3* \
*is arr[j] > arr[j+1]? -> is 4 > 5? no* \
[2,3,1,4,5,4] *j + 1 = 4* \
*is arr[j] > arr[j+1]? -> is 5 > 4 ? yes therefore swap* \
[2,3,1,4,5,4] *j + 1 = 5* \
**j is now 5, so increment i -> i + 1 = 1** \
**This time, j's range will b 0 to n-1-i = 6-1-1 = 4, so only 4 loops (not 5 as previous)
