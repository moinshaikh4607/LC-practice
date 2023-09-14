from typing import List


def isPossible(batteries: List[int],time:int,computers:int) -> int:
        TotalBattery = 0
        for battery in batteries:
            if battery < time:
                TotalBattery += battery  
            else: 
                TotalBattery += time
        return TotalBattery >= time * computers


def maxRunTime(n: int, batteries: List[int]) -> int:
        
    maxTime = 0 
    low = 0 
    high = sum(batteries)

    while low<=high :
        mid = low + (high - low) // 2  #this will return value with floating point
        mid2 = low + (high - low) / 2 #this will return round integer value
        if isPossible(batteries,mid,n):
            maxTime = mid
            low = mid + 1
        else :
            high = mid -1

    return int(maxTime)
        
        
    

# print(maxRunTime(3,[10,10,5,3]))
# print(maxRunTime(4,[8, 1, 4, 8]))
# print(maxRunTime(2,[31,87,85,44,47,25]))        
print(maxRunTime(3,[10,10,3,5]))        