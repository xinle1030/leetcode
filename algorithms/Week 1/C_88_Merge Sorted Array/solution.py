from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = m - 1
        j = n -1
        k = m + n - 1

        while j >= 0 and i >= 0:
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1 
            k -= 1
        
        # all elements in nums1 will be in correct place
        # put any elements in nums2 that had not been placed into nums1
        if j >= 0:
            nums1[:k+1] = nums2[:j+1]

mySol = Solution()
nums1 = [2,0]
m = 1
nums2 = [1]
n = 1
mySol.merge(nums1, m, nums2, n)
print(nums1)

nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3
mySol.merge(nums1, m, nums2, n)
print(nums1)

nums1 = [1]
m = 1
nums2 = []
n = 0
mySol.merge(nums1, m, nums2, n)
print(nums1)

nums1 = [0]
m = 0
nums2 = [1]
n = 1
mySol.merge(nums1, m, nums2, n)
print(nums1)