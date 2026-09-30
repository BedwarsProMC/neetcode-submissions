class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {} # value -> frequency
        for num in nums:
            count[num] = 1 + count.get(num, 0)

        freq = [[] for i in range(len(nums) + 1)]
        
        for value, frequency in count.items():
            freq[frequency].append(value)

        res = []
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res

        return res

