# Notes

- Time Spent: Too Long

### Solution

- Heap Based Solution
  - Basically make a min heap storing a tuple of the distance and point and pop from the heap k time
  - Python automatically sorts by the first element of the tuple
  - O(nlog(k)) as we insert all points into heap, and pop k times which is a logn operation
- Quick Select
  - It doesn't work well with leetcode as there is a test case with duplicate elements + sorted,
    so it will perform at O(n^2) in the worst case
  - _Expected Time_ complexity is O(n) using a randomised pivot, can make it O(n) worst case by finding
    the median of medians (don't actually do this in an interview it's not worth)
