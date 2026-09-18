class Solution:

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        map = {} # value: index

        for i in range(len(nums)):
            difference = target - nums[i]

            # check if already seen the number we trying to find
            if difference in map:
                firstIndex = map[difference]
                return [firstIndex, i]
            else:
                # add value to map
                map[nums[i]] = i
            
        return []