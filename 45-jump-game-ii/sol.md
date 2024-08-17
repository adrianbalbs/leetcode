# Solution

- Maximise `i + nums[i]`, keep track of current end. If i exceeds current end,
  set the current end to the farthest jump, once the current end exceeds the
  end, break
- `O(n)` time complexity
