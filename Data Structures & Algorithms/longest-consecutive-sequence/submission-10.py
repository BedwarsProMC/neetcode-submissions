class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        nums_set = set()
        for num in nums:
            nums_set.add(num)

        maxLength = 0

        for i in range(len(nums)):

            if nums[i] - 1 not in nums_set:
                # start a sequence
                length = 1
                number = nums[i] + 1

                while number in nums_set:
                    length += 1
                    number += 1

                maxLength = max(maxLength, length)


        return maxLength