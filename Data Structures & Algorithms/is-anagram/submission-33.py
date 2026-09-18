class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False

        map_s = {} # 'a' -> 1
        map_t = {}

        for letter in s:
            if letter in map_s:
                map_s[letter] = map_s[letter] + 1
            else:
                map_s[letter] = 1


        for letter in t:
            if letter in map_t:
                map_t[letter] = map_t[letter] + 1
            else:
                map_t[letter] = 1

        if map_s == map_t:
            return True
            
        return False