'''
    Longest continues increasing subsequcens
'''

def findLengthOfLCIS(nums: list[int]) -> int:
    
    if len(nums) == 0 or len(nums) == 1:
        return len(nums)
    
    cur_len = 1
    max_len = 1
    
    for i in range(1,len(nums)):
        if nums[i] > nums[i-1]:
            cur_len += 1
            max_len = max(max_len,cur_len)
        else:
            cur_len = 1
            
    return max_len

print(findLengthOfLCIS([1,3,5,4,7]))
print(findLengthOfLCIS([2,2,2,2,2]))
print(findLengthOfLCIS([1,3,5,7]))
print(findLengthOfLCIS([1,3,5,4,2,3,4]))