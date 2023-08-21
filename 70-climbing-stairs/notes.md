# Notes

- Time Elapsed: 20 Mins

### Solution

- DP Solution Bottom Up
- We have two cases on how we can climb stairs
- Recurrence opt(i) = opt(i - 1) + opt(i - 2)
- Base case: when i = 0 or 1, opt(i) = 1
