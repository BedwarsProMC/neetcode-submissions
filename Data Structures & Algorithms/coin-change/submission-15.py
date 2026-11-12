class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0

        q = deque([amount])
        visited = {amount}
        coinsUsed = 0

        while q:
            coinsUsed += 1
            for _ in range(len(q)):
                rem = q.popleft()

                for c in coins:
                    nxt = rem - c

                    if nxt == 0:
                        return coinsUsed
                    
                    if nxt > 0 and nxt not in visited:
                        q.append(nxt)
                        visited.add(nxt) # say we explored, so this prunes treee so each one explored once.

        return -1