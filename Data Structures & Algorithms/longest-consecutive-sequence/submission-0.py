class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)

        longest: int = 0;
        for num in nums:

            # check if this is start of a sequence
            if not (num - 1) in s:

                length: int = 0
                while (num + length in s):
                    length += 1
                longest = max(longest, length)
        return longest

        