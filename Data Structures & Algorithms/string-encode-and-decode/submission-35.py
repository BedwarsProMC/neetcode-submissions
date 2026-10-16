class Solution:

    def encode(self, strs: List[str]) -> str:
        output = []
        for s in strs:
            output.append(f"{len(s)}#{s}")
        return ''.join(output)

    def decode(self, s: str) -> List[str]:
        output = []
        i = j = 0
        while j < len(s):
            
            while s[j] != '#':
                j += 1
            
            length = int(s[i:j])
            j += 1
            i = j
            j += length
            output.append(s[i:j])
            i = j

        return output