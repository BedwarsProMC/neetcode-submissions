class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []

        for i in range(len(num)):
            while stack and stack[-1] > num[i] and k > 0:
                stack.pop()
                k -= 1
            
            stack.append(num[i])

        # if we didn't use all removals, the largest digits are at the end
        stack = stack[:len(stack) - k]

        res = ''.join(stack)
        # remove any leading 0s
        res = res.lstrip('0')

        if res:
            return res
        else:
            # empty string or 0
            return "0"