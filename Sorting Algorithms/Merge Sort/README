#H1 Here is an implementation of Merge sort in Python.
- Merge sort has a time complexity of O(n*logn)
- Merge sort has a space complexity of O(n)

#H2 The way this algorithm works:
1. First our array is split in half recursively until each element/item is in an array of its own.
2. We then compare array pairs, putting them in order at the point of merge.

#H3 So for example, if we had an array arr, with these values: [6,3,2,1].
Following along the code, we would first recursively split until each item is in its own array.
*is arr greater than 1?: Yes*
[6,3,2,1] -> left_arr = [6,3], right_arr = [2,1]
merge_sort(left_arr)
merge_sort(right_arr)
#H3 Now lets just follow the left_arr.
*is left_arr greater than 1?: Yes*
[6,3] -> left_arr = [6], right_arr = [3]
merge_sort(left_arr)
merge_sort(right_arr)
*is left_arr greater than 1?: No*
