# Solution

- If len(nums) not divisible by group size, then we cannot make groups
- Sort and count frequency of nums and store in ordered dict
- while the dict isn't empty, get the lowest num, then check if
  nums in the range num, num + groupSize - 1 exist, if not we cannot make groups,
  otherwise extract them from the dict and continue this process
- `O(nlogn)` as a result of sorting, the while loop is `O(n)` since
  we pop at most n times
