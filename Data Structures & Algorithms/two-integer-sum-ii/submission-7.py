class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) - 1

        while l < r:

            if numbers[l] + numbers[r] == target:
                return [l + 1, r + 1]       
            elif numbers[l] + numbers[r] > target:
                # biggest element + smallest is still to big so move down array one
                r -= 1
            else:
                # if smallest + biggest still too small, move smallest up one
                l += 1

        return []
        