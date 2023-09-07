# Notes

- Haven't properly solved
- I know it's a BFS question
- Add cells that are 0s to the queue, but if its not 0, set it to infinity
- For each cell in the queue check if in bounds, and also check the adjacent position value > current position value + 1
  - If true, set new cell value to curr position value + 1 and add it to the queue
