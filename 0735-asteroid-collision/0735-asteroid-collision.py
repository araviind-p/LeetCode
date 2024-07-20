from typing import List

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for val in asteroids:
            while stack and stack[-1] > 0 and val < 0:
                if stack[-1] == -val:
                    stack.pop()
                    break
                elif stack[-1] > -val:
                    break
                else:
                    stack.pop()
                    continue
            else:
                stack.append(val)
        return stack
