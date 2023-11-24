from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        current = head # 1

        while current is not None:
            forward = current.next # 2
            current.next = prev # 1 -> None
            prev = current
            current = forward
        
        return prev
    
listNode5 = ListNode(5)
listNode4 = ListNode(4)
listNode3 = ListNode(3)
listNode2 = ListNode(2)
listNode1 = ListNode(1)

listNode1.next = listNode2
listNode2.next = listNode3
listNode3.next = listNode4
listNode4.next = listNode5

head = listNode1
mySol = Solution()
ret = mySol.reverseList(head)
while ret is not None:
    print(ret.val)
    ret = ret.next