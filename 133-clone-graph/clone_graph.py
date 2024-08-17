"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # Handle empty case
        if not node:
            return node

        # Hash table to store nodes (also can be used to determine visited) 
        nodeTable = {}

        # BFS queue
        queue = []

        # BFS to obtain all of the nodes and create a copy to store in table (without neighbors)
        queue.append(node)
        nodeTable[node] = Node(node.val)
        while queue:
            currentNode = queue.pop()
            for nodeNeighbor in currentNode.neighbors:
                if nodeNeighbor not in nodeTable:
                    queue.append(nodeNeighbor)
                    nodeTable[nodeNeighbor] = Node(nodeNeighbor.val)

        # Iterate through hash table and connect neighbors (by iterating through the old node's neighbors)
        for oldNode, newNode in nodeTable.items():
            currNeighbors = newNode.neighbors
            for oldNeighbor in oldNode.neighbors:
                currNeighbors.append(nodeTable[oldNeighbor])

        return nodeTable[node]
