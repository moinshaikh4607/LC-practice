from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoLists(list1: Optional[ListNode], list2: Optional[ListNode]) -> list:
    
    # list3:Optional[ListNode] = []
    list3 = []
    
    
    while list1 is not None :
        list3.append(list1.val)    
        list1 = list1.next
        
    while list2 is not None :
        list3.append(list2.val)    
        list2 = list2.next
        
    list3.sort()
    
    result = ListNode()
    temp = result
    for i in list3:
        temp.next = ListNode(i)
        temp = temp.next
        

    return result.next


list1 = ListNode(1) 
list1.next = ListNode(2)
list1.next.next = ListNode(3)

list2 = ListNode(1) 
list2.next = ListNode(5)
list2.next.next = ListNode(4)

print(mergeTwoLists(list1,list2))