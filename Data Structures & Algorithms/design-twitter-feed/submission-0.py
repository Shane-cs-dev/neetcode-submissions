from collections import defaultdict
import heapq
from typing import List

class Twitter:

    def __init__(self):
        # Define a count to track the total post
        self.time = 0

        # Define a dict of set to track the user's follow ID
        self.follow_map = defaultdict(set)
        self.tweet_map = defaultdict(list) # Track the time and the tweetID
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        # Store current and given tweetId to the tweet_map
        self.tweet_map[userId].append((self.time, tweetId))
        self.time -= 1 # The smaller the time, the latest the tweet post
        return

    def getNewsFeed(self, userId: int) -> List[int]:
        # Define a res to store the top10 tweet
        # Define a min_heap to store all tweets from all the user's followee
        res, min_heap = [], []
        users = set(self.follow_map[userId])
        users.add(userId)
        for followee_id in users:
            if followee_id in self.tweet_map and self.tweet_map[followee_id]: # Check if the followee tweets
                # get the information from that tweet and store the information into the min heap
                idx = len(self.tweet_map[followee_id]) - 1 # Get the index of that tweet
                time_stamp, tweet_id = self.tweet_map[followee_id][idx]
                heapq.heappush(min_heap, (time_stamp, followee_id, tweet_id, idx))
        
        # Add top10 post's tweet_id into the list
        while min_heap and len(res) < 10:
            time_stamp, followee_id, tweet_id, cur_idx = heapq.heappop(min_heap)
            res.append(tweet_id)
            cur_idx -= 1
            # Update the the min_heap if the user has older tweet
            if cur_idx >= 0:
                time_stamp, tweet_id = self.tweet_map[followee_id][cur_idx]
                heapq.heappush(min_heap, (time_stamp, followee_id, tweet_id, cur_idx))
        
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.follow_map[followerId].add(followeeId)
        return

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.follow_map[followerId].discard(followeeId)
        return
