class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        scoreToIndex = {0: -1}
        valToScore = {0: -1, 1: +1}
        score = 0
        best = 0
        for i, val in enumerate(nums):
            score += valToScore[val]
            if score in scoreToIndex:
                start_index = scoreToIndex[score]
                length = i - start_index
                best = max(best, length)

            else:
                scoreToIndex[score] = i
        
        return best
