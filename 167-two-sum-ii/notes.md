# Notes

- Time Elapsed: 15 Minutes

### Solution

- Two pointers, one at the start, one at the end
- If the pointers add to the target, return indices
- Else if the sum is larger, decrease the right pointer (reduces the sum as array is sorted)
- Else if the sum is smaller, increase left pointer (increases the sum)

### Time Complexity

- We can iterate through at most n - 1 elements for the two pointers, so O(n) in the worst case
- Constant space as we are not allocating data structures
