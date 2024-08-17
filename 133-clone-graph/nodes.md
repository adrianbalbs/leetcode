# Notes

- Time Elapsed: 15 Minutes

### Solution

- Create hash table with old nodes as key and new nodes as values
- Perform BFS on the graph to get all nodes and insert key values in hash table
- Traverse hash table and traverse the old node's neighbors for each entry, and
  append the corresponding new node entry as a neighbor for the current node

### Time Complexity

- BFS is O(V + E) as we are using adjacency list
- Second traversal is also O(V + E) as we visit each node and the neighbors
- Overall O(V + E)
- Space Complexity is O(V) as we are storing all nodes as an entry
