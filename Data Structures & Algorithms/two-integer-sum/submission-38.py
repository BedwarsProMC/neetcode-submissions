class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mp = {} # value -> index

        for i, val in enumerate(nums):
            diff = target - val
            if diff in mp:
                return [mp[diff], i]
            mp[val] = i