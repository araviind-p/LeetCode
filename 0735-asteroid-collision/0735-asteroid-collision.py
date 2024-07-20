from typing import List

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for val in asteroids:
            while stack and stack[-1] > 0 and val < 0:
                diff = val + stack[-1]
                if diff < 0:
                    stack.pop()
                elif diff > 0:
                    val=0
                else:
                    val=0
                    stack.pop()
            if val:
                stack.append(val)
        return stack
