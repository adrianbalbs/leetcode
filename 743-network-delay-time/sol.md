# Solution

- Just use Dijkstra's, transform list to adj list
  the minimum time is the longest path in the dist array
- If the longest path is INF, then we have an unreachable node
- `O(V + ElogV)` since we are using min-heap implementation
