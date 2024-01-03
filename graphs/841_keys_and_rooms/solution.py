from typing import List


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visit = set()
        stack = rooms[0]
        visit.add(0)
        while stack:
            next_room = stack.pop()
            if next_room in visit:
                continue
            visit.add(next_room)
            for key in rooms[next_room]:
                if key in visit:
                    continue
                stack.append(key)
        return len(visit) == len(rooms)
