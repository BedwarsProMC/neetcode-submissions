class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()

        boats = 0
        l, r = 0, len(people) - 1

        while l <= r:

            # each iteration we adding the right most
            # the heaviest to a boat
            # if the lightest (l) fits then also add to
            # same boat
            if l < r and people[l] + people[r] <= limit:
                l += 1

            boats += 1
            r -= 1

        return boats
