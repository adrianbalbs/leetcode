# Solution

- We know that if sum(gas) < sum(cost) then there exists no solution
- We also know that if we start at a and get stuck at b, then we cannot reach
  town b from any town in between a and b.
- Take the differences for each pos and note that we do not want to start at a
  position with a negative difference
- Our greedy heuristic is picking the first instance where a position is positive
- `O(n)` time complexity
