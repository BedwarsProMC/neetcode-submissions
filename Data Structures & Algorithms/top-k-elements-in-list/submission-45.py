class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count = {} # val -> freq count
        for num in nums:
            count[num] = 1 + count.get(num, 0)
        
        freq = [[] for _ in range(len(nums) + 1)] # each index is frequency of the items at that index
        for val, cnt in count.items():
            freq[cnt].append(val)
        
        res = []
        for bucket in range(len(nums), 0, -1):
            for item in freq[bucket]:
                res.append(item)

                if len(res) == k:
                    return res

        return res