# Solution

- 2D DP, if `s[i] == t[j]` then we can either include or exclude the `ith` char
- If chars don't match we need to delete i
- if t is empty then we have 1 way to make t from s.
- `O(nm)` time and space complexity
