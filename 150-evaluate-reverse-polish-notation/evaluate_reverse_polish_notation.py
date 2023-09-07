from typing import List
from collections import deque
import math

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stack = deque()
        for token in tokens:
            if token == "+":
                val1, val2 = self.stackValues(stack)
                stack.appendleft(val1 + val2)
            elif token == "-":
                val1, val2 = self.stackValues(stack)
                stack.appendleft(val1 - val2)
            elif token == "*":
                val1, val2 = self.stackValues(stack)
                stack.appendleft(val1 * val2)
            elif token == "/":
                val1, val2 = self.stackValues(stack)
                stack.appendleft(math.trunc(val1 / val2))
            else:
                stack.appendleft(int(token))
        return stack.popleft()


    def stackValues(self, stack):
        val2 = stack.popleft()
        val1 = stack.popleft()
        return (val1, val2)


solution = Solution()
print(solution.evalRPN(["2","1","+","3","*"]))
print(solution.evalRPN(["4","13","5","/","+"]))
print(solution.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))
