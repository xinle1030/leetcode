from typing import Optional

"""
Detect loop in a linked list using Floyd’s Cycle-Finding Algorithm:
It uses two pointers one moving twice as fast as the other one. 
- The faster one is called the faster pointer.
- The other one is called the slow pointer.

Time Complexity: O(N)
Space Complexity: O(1)

why this algo works: https://www.geeksforgeeks.org/floyds-cycle-finding-algorithm/
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow_pointer = head
        fast_pointer = head

        while fast_pointer and fast_pointer.next:
            slow_pointer = slow_pointer.next
            fast_pointer = fast_pointer.next.next

            # if fast_pointer catch up with slow pointer, there is a cycle
            if slow_pointer is fast_pointer:
                # reset slow pointer to head
                slow_pointer = head
                # make both pointers move at same pace - where they meet is the node where cycle occurs
                while slow_pointer != fast_pointer:
                    slow_pointer = slow_pointer.next
                    fast_pointer = fast_pointer.next
                return slow_pointer
        
        return None

listNode4 = ListNode(-4)
listNode3 = ListNode(0)
listNode2 = ListNode(2)
listNode1 = ListNode(1)

# head = [3,2,0,-4], pos = 1
# listNode1.next = listNode2
# listNode2.next = listNode3
# listNode3.next = listNode4
# listNode4.next = listNode2

# head = [1,2], pos = 0
# listNode1.next = listNode2
# listNode2.next = listNode1

# head = [1], pos = 0
listNode1.next = listNode1

head = listNode1
mySol = Solution()
ret = mySol.detectCycle(head)
print(ret.val)