class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = 0 # start
        j = 0 # move pointer
        maxLen = 0
        charIndices = [-1] * 128

        for j in range(len(s)):
            # check if the current character has occurred within the current substring by comparing its index in charIndex with i.
            if charIndices[ord(s[j])] >= i:
                # move i to the index after the occurrence of repeated character
                i = charIndices[ord(s[j])] + 1
            charIndices[ord(s[j])] = j

            # length of the current window (right - left + 1)
            maxLen = max(maxLen, j - i + 1)

        return maxLen

mySol = Solution()

s = "abcabcbb"
print(mySol.lengthOfLongestSubstring(s))

s = "bbbbb"
print(mySol.lengthOfLongestSubstring(s))

s = "pwwkew"
print(mySol.lengthOfLongestSubstring(s))

s = " "
print(mySol.lengthOfLongestSubstring(s))

s = "dvdf"
print(mySol.lengthOfLongestSubstring(s))