class Twitter:
    # What if you keep feed and unfollow the user
    # self.follows = {followerId: []} the list of followeeId
    # self.timestamp = 0 increment whe postTweet
    # self.posts = [{timestamp, userId, tweetId}]
    # self.feeds = {userId: []} the list of posts

    # unfollow: O(2n) O(n): delete from follows, O(n): delete from feeds
    # follow: O(n): add to feeds and O(nlogn) for soft
    # get news feed 
    # post: add to posts, adds to feed

    # posts can be {userId: post}
    # feeds = {userId: doublyLinkedList}
    # add to feeds easy
    # remove from feeds. you get the list of posts and apply it to all followers (Unrealistic)
    # common question to speed up search
    # you need indexes. 
    def __init__(self):
        self.follows = {}
        self.timestamp = 0
        self.posts = {}
        self.feeds = {}

    def postTweet(self, userId: int, tweetId: int) -> None:
        posts = self.posts.get(userId, [])
        self.timestamp -= 1
        post = {"userId": userId, "tweetId": tweetId, "timestamp": self.timestamp}
        heapq.heappush(posts, (self.timestamp, post))
        self.posts[userId] = posts
        

    def getNewsFeed(self, userId: int) -> List[int]:
        followees = self.follows.get(userId, set())
        feed = []
        feed_heap = []
        users = []
        users.append(userId)
        users.extend(followees)
        for user in users:
            post_heap = self.posts.get(user)
            if post_heap:
                feed_heap.extend(post_heap)
        heapq.heapify(feed_heap)
        while feed_heap:
            timestamp, post = heapq.heappop(feed_heap)
            feed.append(post["tweetId"])
            if len(feed) == 10:
                return feed
        return feed
            

        
        

    def follow(self, followerId: int, followeeId: int) -> None:
        followees = self.follows.get(followerId, set())
        followees.add(followeeId)
        self.follows[followerId] = followees

    def unfollow(self, followerId: int, followeeId: int) -> None:
        followees = self.follows.get(followerId, set())
        if followeeId in followees:
            followees.remove(followeeId)



# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)