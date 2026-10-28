# heap version, using the same F (number of followees) and k = 10:

# Time: getNewsFeed O(F + k log F) = O(F) since k = 10, all other methods O(1)
#   F = number of users this person follows (followees), k = feed size (10)
# Space: O(N * m + N * M)
#   N = total userIds, m = max tweets by any user, M = max followees for any user

# You start with at most one tweet per followee, and every time you pop one, you push at most one back (the next older tweet from that same person). So the size can only stay the same or shrink.

from collections import defaultdict
import heapq

class Twitter:

    def __init__(self):
        self.count = 0 # increment on tweet. highest count is most recently created tweet
        self.followMap = defaultdict(set) # userId -> set of followee Ids
        self.tweetMap = defaultdict(list) # userId -> list of (count, tweetIds) for user Id. highest count is most recent

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append( (self.count, tweetId) )
        self.count += 1
        
    def getNewsFeed(self, userId: int) -> List[int]:
        minHeap = []
        
        # add top most recent tweet from all followees and user
        for followeeId in self.followMap[userId] | {userId}:
            if followeeId in self.tweetMap:
                index = len(self.tweetMap[followeeId]) - 1
                count, tweetId = self.tweetMap[followeeId][index]
                minHeap.append( (-count, tweetId, followeeId, index) )

        # apply heap property
        heapq.heapify(minHeap)
        res = []
        while minHeap and len(res) < 10: # stop when heap empty or 10items
            _, tweetId, followeeId, index = heapq.heappop(minHeap)
            res.append(tweetId)

            if index > 0:
                # add next most recent tweet for this followee to the heap
                index -= 1
                count, tweetId = self.tweetMap[followeeId][index]
                heapq.heappush(minHeap, (-count, tweetId, followeeId, index))

        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId:
            return
        self.followMap[followerId].add(followeeId)
        
    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)
        



