from typing import List

class Solution:
    def isPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s) - 1

        while i < j:
            if not s[i].isalnum():
                i += 1
            elif not s[j].isalnum():
                j -= 1
            elif s[i].lower() == s[j].lower():
                i += 1
                j -= 1
            else:
                return False

        return True

mySol = Solution()

s = "A man, a plan, a canal: Panama"
print(mySol.isPalindrome(s))

s = "race a car"
print(mySol.isPalindrome(s))

s = " "
print(mySol.isPalindrome(s))

s = "0P"
print(mySol.isPalindrome(s))

s = "a."
print(mySol.isPalindrome(s))

s = ".,"
print(mySol.isPalindrome(s))