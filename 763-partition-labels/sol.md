# Solution

- Use map to keep track of last occurence of char in string, iterate
  through string and greedily take the longest ending point of the char
- If we reach the ending point without changing end, then we have reached
  the end of a partition
- `O(n)` time complexity, `O(26)` space complexity
