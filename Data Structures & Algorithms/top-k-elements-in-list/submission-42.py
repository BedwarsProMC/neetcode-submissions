class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # buckets = [[] * (len(nums)+1)]

        buckets = [[] for i in range(len(nums) + 1)]
        # print(buckets)

        freq = {}

        for i in range(len(nums)):
            freq[nums[i]] = 1 + freq.get(nums[i], 0)

        for value,frequency in freq.items():
            buckets[frequency].append(value)
        
        output = []
        for i in range(len(buckets) -1, -1, -1):
            curr = buckets[i]

            j = 0
            while len(output) < k and j < len(curr):
                output.append(curr[j])
                j += 1

        return output

