# Notes

- Time Elapsed: 10 Minutes

# Solution

- Dynamic Programming Approach
  - Reccurrence opt(i) = max(opt(i - 1) + A[i], A[i])
  - We need to pick which subarray is the biggest, if one is bigger, then discard the other

# Time Complexity

- O(n) subproblems which take O(1) time to compute, therefore O(n)
- O(n) Space Complexity as we are creating an array of size n.
