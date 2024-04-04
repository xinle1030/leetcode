from typing import List
import random
import heapq

class Solution:
    """
    Method 1: Quick Select

    Time Complexity: 
    Best and Average Case: O(N)
    Worst Case: O(N^2)
    The average performance is linear. However, in the worst case (very rare, especially with randomized pivot), the algorithm can degrade to O(N^2).
    
    Space Complexity: O(1)
    The space used is constant. The algorithm modifies the original list in place and doesn't utilize any significant additional data structures. 
    The recursive stack calls (in the worst case) are also bounded by the depth of the list, making it O(log⁡ N), but this is typically considered as O(1) space complexity in QuickSelect.
    """
    def findKthLargest(self, nums: List[int], k: int) -> int:
        low = 0
        high = len(nums)

        while True:
            p = random.randint(low, high - 1)
            m, pi = self.partition(nums, low, high, p)
            if m < k <= pi:    # from m th largest to i th largest they are the same, and k is among them
                return nums[m]
            elif k <= m:
                high = m
            elif k > pi:
                low = pi
    
    def partition(self, arr, low, high, p):
        pivot = arr[p]

        # pointer for greater element
        i = low + 1

        arr[p], arr[low] = arr[low], arr[p]

        # traverse through all elements
        # compare each element with pivot
        while i < high:
            if arr[i] > pivot:
                arr[i], arr[low] = arr[low], arr[i]
                i += 1
                low += 1
            elif arr[i] == pivot:
                i += 1
            else:
                high -= 1
                arr[i], arr[high] = arr[high], arr[i]
        
        # low, ..., i
        return low, i

    """
    Method 2: Min Heap
    Time Complexity: O(n log⁡ k)
    Each of the n elements is processed once. However, heap operations take O(log ⁡k) time, leading to an overall complexity of O(n log⁡ k).
    
    Space Complexity: O(k)
    The solution uses a heap with a maximum of k elements.
    
    k largest element is at minimum of min heap which always maintains the k largest elements seen so far
    """
    def findKthLargest2(self, nums: List[int], k: int) -> int:
        minHeap = nums[:k] # do this for space complexity = O(k)
        heapq.heapify(minHeap)

        for num in nums[k:]:
            # maintains the k largest elements seen so far
            if num > minHeap[0]:
                heapq.heappop(minHeap)
                heapq.heappush(minHeap, num)
        
        return minHeap[0]
 

mySol = Solution()
nums = [3,2,1,5,6,4]
k = 2
print(mySol.findKthLargest(nums, k))
print(mySol.findKthLargest2(nums, k))

nums = [3,2,3,1,2,4,5,5,6]
k = 4
print(mySol.findKthLargest(nums, k))
print(mySol.findKthLargest2(nums, k))

nums = [1]
k = 1
print(mySol.findKthLargest(nums, k))
print(mySol.findKthLargest2(nums, k))
