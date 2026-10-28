# Sort with last-10 slicing: simple, correct, O(n log n). Good to get working first.
# Sort: it’s 10 × n items, so O(10n log 10n), where n is the number of followees. Drop the constants and you get O(n log n).

# Heap with heapify: O(n + k log n). This is the version worth knowing properly, because it’s Merge K Sorted Lists, which comes up repeatedly.
# You start with at most one tweet per followee, and every time you pop one, you push at most one back (the next older tweet from that same person). So the size can only stay the same or shrink.

class Twitter:

    def __init__(self):
        self.count = 0 # increments on each tweet creation. allows us to find 10 most recent
        self.followMap = defaultdict(set) # userId -> set of followeeId
        self.tweetMap = defaultdict(list) # userId -> list of (count, tweetId) 

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append( (self.count, tweetId) )
        self.count += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        tweets = [] # 10 most recent tweets of userId and ALL followees of userId
        
        if userId in self.tweetMap:
            tweets.extend(self.tweetMap[userId][-10:])

        for followeeId in self.followMap[userId]:
            if followeeId in self.tweetMap:
                tweets.extend(self.tweetMap[followeeId][-10:])

        # sort by count
        tweets.sort(key = lambda x: -x[0])
        
        return [tweet[1] for tweet in tweets[0:10]]

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId:
            return
        
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)









