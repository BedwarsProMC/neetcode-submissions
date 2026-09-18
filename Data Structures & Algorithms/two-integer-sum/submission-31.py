class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        seenMap = {}

        for i in range(len(nums)):
            diff = target - nums[i]

            if diff in seenMap:
                return [seenMap.get(diff), i]

            seenMap[nums[i]] = i