class Solution:


    def encode(self, strs: List[str]) -> str:
        res = []
        for  s in strs:
            res.append(str(len(s)))
            res.append('#')
            res.append(s)
        return "".join(res)

    def decode(self, s: str) -> List[str]:
        res = []

        i = j = 0
        while j < len(s):

            while s[j] != '#':
                j += 1
            
            length = int(s[i:j])
            i = j + 1
            j = j + length
            word = s[i:j + 1]
            res.append(word)
            j = j + 1
            i = j

        return res


