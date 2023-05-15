### Solution
- Use a hash map to count Top K Frequeny Elements
- Convert the hash map into tuples 
- Sort the list of tuples by the value and have it reversed
- Return the sliced index while looking at the first elem of the tuple

### O(n) solution
- Bucket sort
 - Use a sorting array of the size of the input array
 - We will use the indexes of the array of the counts of each value
 - Stores the numbers as a list inside of the list
 - Still use the hashmap for the count
 - Index backward to get the k elems and also check if the size
 of res = k
