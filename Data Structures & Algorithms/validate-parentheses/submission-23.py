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

                if stack and stack[-1] == closeToOpen[s[i]]:
                    stack.pop()
                else:
                    return False

            else: # opening bracket
                stack.append(s[i])

        return not stack