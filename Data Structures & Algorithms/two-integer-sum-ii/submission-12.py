class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) - 1

        while l < r:
            currentSum = numbers[l] + numbers[r]

            if currentSum > target:
                # too big so decrement right
                r -= 1
            elif currentSum < target:
                l += 1
            else:
                # equal
                return [l + 1, r + 1]

        return []