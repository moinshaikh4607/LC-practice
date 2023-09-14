from typing import List


def searchInsert(nums: List[int], target: int) -> int:
        
    for i in range(len(nums)-1) :
        if nums[i] == target :
            return i

    nums.append(target)
    nums = sorted(nums)
    return searchInsert(nums,target)
    
print(searchInsert([1,3,5,6],5))
print(searchInsert([1,3,5,6],2))