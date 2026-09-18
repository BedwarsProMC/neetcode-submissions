class Solution:

    def encode(self, strs: List[str]) -> str:
        output = ''
        for s in strs:
            output += str(len(s)) + '#' + s
        return output

    def decode(self, s: str) -> List[str]:
        output = []

        i = 0
        j = 0

        while j < len(s):

            while (s[j] != '#'):
                j += 1
            
            length = int(s[i:j])
            j += 1
            output.append(s[j:int(j+length)])

            j = j + length
            i = j

        return output

