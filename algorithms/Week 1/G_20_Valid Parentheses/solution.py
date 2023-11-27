from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()
        brackets = {
            '(': ')',
            '{': '}',
            '[': ']'
        }

        for ch in s:
            # current string is open bracket
            if ch in brackets.keys():
                stack.append(ch)
            # current string is closed bracket which needs to be checked
            else:
                if len(stack) > 0:
                    item = stack.pop()
                    closeBracket = brackets[item]
                else:
                    closeBracket = "#"
                if ch != closeBracket:
                    return False
        
        return len(stack) == 0

mySol = Solution()
s = "()"
print(mySol.isValid(s))

s = "()[]{}"
print(mySol.isValid(s))

s = "(]"
print(mySol.isValid(s))

s = "]"
print(mySol.isValid(s))
