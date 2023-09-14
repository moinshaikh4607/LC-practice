from typing import List


def removeElement(nums: List[int], val: int) -> int:
        nums = [x for x in nums if x != val]
        print(nums,nums[:])
        return len(nums[:])
    
print(removeElement([3,2,2,3],3))
print(removeElement([0,1,2,2,3,0,4,2],2))