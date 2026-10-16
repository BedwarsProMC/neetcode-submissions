class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        binToScore = {0: -1, 1: 1}
        longest = 0
        score = 0
        first_seen = {0: -1} # score -> first seen index
        for i, v in enumerate(nums):
            score += binToScore[v]
            if score in first_seen:
                length = i - first_seen[score]
                longest = max(longest, length)
            else:
                first_seen[score] = i
        return longest
