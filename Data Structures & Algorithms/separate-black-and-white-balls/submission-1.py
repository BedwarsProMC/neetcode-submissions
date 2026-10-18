class Solution:
    def minimumSteps(self, s: str) -> int:
        ones_seen = 0 # each zero has to move past this many oens
        swaps = 0 # each 0 we move towards left
        for c in s:
            if c == '1':
                ones_seen += 1
            else:
                # its a zero and we need to move past all 1s
                # so increment swaps by number of 1s in the way
                swaps += ones_seen
            
        return swaps