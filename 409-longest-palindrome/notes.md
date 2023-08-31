# Notes

- Time Elapsed: 10 Minutes

### Solution
- This is a greedy problem where we want to take as much as possible to find the length of the max palindrome
- Consider the count of the characters, we can always take evens, and we can take odd because it can be in the middle
- If we find another count of letters that is odd, then we can only add up to the greatest even amount (oddNum - 1)

### Time Complexity
- O(n) for counter dict preprocessing, O(n) for traversing the counter, therefore overall O(n)
- Space Complexity, O(n) as we are using a Counter Hash Table.
