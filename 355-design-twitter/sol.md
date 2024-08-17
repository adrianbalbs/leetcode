# Solution

- Use dict for storing key of follower to followees
- Used stack to maintain (tweetId, userId)
- Not optimal as this is O(n), can optimise by using min-heap with global count
  to keep track of time posted
  - Also store tweets in a map (user, list[tweetId])
  - Heap to store the time, tweetId, followeeId and next index
