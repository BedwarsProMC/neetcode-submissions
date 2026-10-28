# Sort with last-10 slicing: simple, correct, O(F log F). Good to get working first.
# Sort: it’s 10 × F items, so O(10F log 10F), where F is the number of followees. Drop the constants and you get O(F log F).

# F is number of users this person follows. Collecting Tweets is 10 per person * F = O(10F) = O(F). Then sorting 10*F items is O(10 F log 10F) = O(FlogF)

# Time: getNewsFeed O(F log F), all other methods O(1)
#   F = number of users this person follows (followees)

# Space: O(N * m + N * M)
#   N = total userIds, m = max tweets by any user, M = max followees for any user

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
        
        # F is number of users this person follows.
        # Collecting Tweets is 10 per person * F = O(10F) = O(F).
        if userId in self.tweetMap:
            tweets.extend(self.tweetMap[userId][-10:])

        for followeeId in self.followMap[userId]: # O (F
            if followeeId in self.tweetMap:
                tweets.extend(self.tweetMap[followeeId][-10:]) # x 10)

        # sort by count Then sorting 10*F items is O(10 F log 10F) = O(FlogF)
        tweets.sort(key = lambda x: -x[0]) # REVERSE it to have most recent fist (largest count first)
        
        return [tweet[1] for tweet in tweets[0:10]]

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId:
            return
        
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)









