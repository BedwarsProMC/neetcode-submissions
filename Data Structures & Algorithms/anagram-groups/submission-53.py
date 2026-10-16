class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # freq array as key, to list of anagrams
        freq = defaultdict(list) # tuple([1,0,3,0.. 0]) -> ['aa', 'aa']

        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            freq[tuple(count)].append(s)

        return list(freq.values())
