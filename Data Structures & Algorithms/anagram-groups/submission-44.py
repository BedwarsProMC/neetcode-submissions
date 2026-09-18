class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        count = defaultdict(list) # freq array -> str array

        for s in strs:
            freq = [0] * 26
            for c in s:
                freq[ord(c) - ord('a')] += 1
            count[tuple(freq)].append(s)

        return list(count.values())
        