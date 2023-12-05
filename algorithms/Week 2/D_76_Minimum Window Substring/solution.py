class Solution:

    def getIdx(self, char: chr) -> int:
        if char.islower():
            idx = ord(char) - ord('a') + 26
        else:
            idx = ord(char) - ord('A')
        return idx
        
    def minWindow(self, s: str, t: str) -> str:
        s_count = [0] * 52
        t_count = [0] * 52

        if len(t) > len(s):
            return ""
        
        for i in range(len(t)):
            t_idx = self.getIdx(t[i])
            t_count[t_idx] += 1
        
        minLen = float('inf')
        count = 0
        startIdx = -1
        start = 0

        for i in range(len(s)):
            s_count[self.getIdx(s[i])] += 1

            # if such character in s is found in the pattern t
            if s_count[self.getIdx(s[i])] <= t_count[self.getIdx(s[i])]:
                count += 1
            
            # if all the pattern characters are found
            if count == len(t):

                # we need to minimize window by eliminating those characters that are not required in the window
                while (s_count[self.getIdx(s[start])] > 
                       t_count[self.getIdx(s[start])] or 
                       t_count[self.getIdx(s[start])] == 0):
                    
                    if (s_count[self.getIdx(s[start])] > 
                        t_count[self.getIdx(s[start])]):
                        s_count[self.getIdx(s[start])] -= 1
                    
                    start += 1
                
                tempLen = i - start + 1
                if tempLen < minLen:
                    minLen = tempLen
                    startIdx = start
                
        if startIdx == -1:
            return ""
        else:
            return s[startIdx:startIdx+minLen]


mySol = Solution()

s = "ADOBECODEBANC"
t = "ABC"
print(mySol.minWindow(s, t))

s = "a"
t = "a"
print(mySol.minWindow(s, t))

s = "a"
t = "aa"
print(mySol.minWindow(s, t))