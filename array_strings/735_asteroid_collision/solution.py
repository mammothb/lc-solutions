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

    def asteroidCollision_2(self, asteroids: List[int]) -> List[int]:
        stack = []
        for asteroid in asteroids:
            # always add asteroid moving to the right
            if asteroid > 0:
                stack.append(asteroid)
            else:
                # if empty or both asteroids moving in the same direction
                if not stack or stack[-1] * asteroid > 0:
                    stack.append(asteroid)
                else:
                    # destroy smaller asteroids from stack
                    while stack and stack[-1] > 0 and stack[-1] < abs(asteroid):
                        stack.pop()
                    # if empty or both moving same direction
                    if not stack or stack[-1] * asteroid > 0:
                        stack.append(asteroid)
                    # destorys both top of stack and curr asteroid
                    elif stack[-1] == asteroid == 0:
                        stack.pop()
                    # only curr asteroid gets destroyed

        return stack
