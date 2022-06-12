def containsDuplicate( nums) -> bool:
    hashset = set()

    for n in nums:
        if n in hashset:
            return True
        
        hashset.add(n)
    return False


array1 = [1,2,4,6,1]
array2 = [1,2,3]
print(containsDuplicate(array1))
print(containsDuplicate(array2))

        
