from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or k == 1:
            return head
        
        current = head
        count = 0

        while current is not None and count < k:
            current = current.next
            count += 1

        # Not enough nodes to reverse
        if count < k:
            return head
        
        """
        reverse within k number of elements
        """
        prev = None
        current = head
        
        for i in range(k):
            forward = current.next
            current.next = prev
            prev = current
            current = forward
        """
        reverse within k number of elements
        """

        # reverse the remaining groups starting from current
        head.next = self.reverseKGroup(current, k)

        # 'prev' is now the new head of this group
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
k = 2
ret = mySol.reverseKGroup(head, k)
while ret is not None:
    print(ret.val)
    ret = ret.next