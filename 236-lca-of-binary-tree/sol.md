# Solution

- Base case root is null or node is p or q
- Recursive Case: if the left and right are not null then we found LCA
- Otherwise return either the left or the right if either is not null (LCA exists lower)
- `O(n)` Time Complexity and Space (recursion stack)
