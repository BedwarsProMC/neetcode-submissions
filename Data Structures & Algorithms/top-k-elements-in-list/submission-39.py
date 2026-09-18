class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {} # val -> freq
        for n in nums:
            count[n] = 1 + count.get(n, 0);

        buckets = [[] for i in range(len(nums) + 1)]

        for n, f in count.items():
            buckets[f].append(n)

        res = []
        for i in range(len(buckets) - 1, 0, -1):

            for item in buckets[i]:
                res.append(item)

                if len(res) == k:
                    return res