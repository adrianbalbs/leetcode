# Notes

- Time Taken: 20 Minutes

### Solution

- Use a stack to store the numbers and append every token that's a number
- Only pop when we see an operator token, and then push the result to the stack
- For division, truncation can be handled with `math.trunc()`

### Time Complexity

- O(n) as we are scanning through each token
- O(n) space complexity as we maintain a stack which could contain up to O(n) elements
