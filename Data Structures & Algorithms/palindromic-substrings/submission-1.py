class Solution:
    def countSubstrings(self, s: str) -> int:
        # brute force O(n^3) -  too inefficient
        # res = 0
        # for i in range(len(s)):
        #     for j in range(i, len(s)):
        #         l, r = i, j
        #         while l < r and s[l] == s[r]:
        #             l += 1
        #             r -= 1

        #         if l >= r:
        #             res += 1
                
        # return res

        # Two pointers: Time O(n^2)
        res = 0
        for i in range(len(s)):
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                res += 1
                l -= 1
                r += 1

            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                res += 1
                l -= 1
                r += 1

        return res
