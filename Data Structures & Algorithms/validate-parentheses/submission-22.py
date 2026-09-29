class Solution:
    def isValid(self, s: str) -> bool:
        
        closeToOpen = {
            "}": "{",
            "]": "[",
            ")": "("
        }

        stack = []
        for i in range(len(s)):
            if s[i] in closeToOpen: # closing bracket
                
                if not stack:
                    return False
                if closeToOpen[s[i]] != stack.pop():
                    return False

            else: # opening bracket
                stack.append(s[i])

        return not stack