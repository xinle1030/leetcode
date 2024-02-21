from typing import List
# https://leetcode.com/problems/largest-number/solutions/53298/python-different-solutions-bubble-insertion-selection-merge-quick-sorts/

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        sorted_nums = self.merge_sort(nums)
        # convert to int first, then str to handle case "00"
        return str(int(''.join(map(str, sorted_nums))))

    def compare(self, n1, n2):
        return str(n1) + str(n2) > str(n2) + str(n1)
        
    def merge_sort(self, arr):
        if len(arr) > 1:
            mid = len(arr) // 2

            arr1 = self.merge_sort(arr[:mid])
            arr2 = self.merge_sort(arr[mid:])

            return self.merge(arr1, arr2)
        else:
            return arr

    def merge(self, arr1, arr2):
        i = 0
        j = 0
        res = []

        while i < len(arr1) and j < len(arr2):
            if self.compare(arr1[i], arr2[j]):
                res.append(arr1[i])
                i += 1
            else:
                res.append(arr2[j])
                j += 1
        
        if i < len(arr1):
            res += arr1[i:]
        elif j < len(arr2):
            res += arr2[j:]
        
        return res
    
mySol = Solution()

nums = [10,2]
print(mySol.largestNumber(nums))

nums = [3,30,34,5,9]
print(mySol.largestNumber(nums))

nums = [0, 0]
print(mySol.largestNumber(nums)) 