# Solution

- This is just activity selection
- We remove endpoints by the latest ending time (sort by ending time)
- Use two pointers to keep track of the prev interval that is kept
- We want the biggest subset with non-overlapping intervals
- `O(nlogn)` time complexity because of sorting
