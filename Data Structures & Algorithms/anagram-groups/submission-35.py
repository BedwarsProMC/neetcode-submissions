class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list) # [] freq array -> [] str array

        for s in strs:
            count = [0] * 26 # index is from 0 - 25 representing letters, value is frequency
            for c in s:
                count[ord(c) - ord('a')] += 1
            res[tuple(count)].append(s)

        return list(res.values())