class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0
        
        mp = {}
        bad_pairs = 0

        for i, val in enumerate(nums):
            key = i - val
            good_matches = mp.get(key, 0)
            bad_pairs += (i - good_matches)
            mp[key] = 1 + mp.get(key, 0)

        return bad_pairs
