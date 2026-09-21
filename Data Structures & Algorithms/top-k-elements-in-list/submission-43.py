class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count = {} # value: freq
        for num in nums:
            count[num] = 1 + count.get(num, 0)

        freq = [[] for _ in range(len(nums) + 1)]

        for value, cnt in count.items():
            freq[cnt].append(value)

        res = []
        for i in range(len(nums), 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res