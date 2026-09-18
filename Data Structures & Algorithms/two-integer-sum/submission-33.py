class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        valToIndex = {} # value: index

        for i, num in enumerate(nums):
            diff = target - num

            if diff in valToIndex:
                # good
                return [valToIndex.get(diff), i]
            else:
                valToIndex[num] = i

        