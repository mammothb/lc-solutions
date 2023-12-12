from typing import List


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for asteroid in asteroids:
            destroyed = False
            # Only destroy when top of stack is moving right (positive) and curr
            # asteroid is moving left (negative)
            while stack and stack[-1] > 0 and asteroid < 0 and not destroyed:
                if abs(stack[-1]) < abs(asteroid):
                    stack.pop()
                elif abs(stack[-1]) == abs(asteroid):
                    stack.pop()
                    destroyed = True
                else:
                    destroyed = True
            if not destroyed:
                stack.append(asteroid)
        return stack
