import heapq
from typing import List


class Solution:
    """Description

    Given a binary array lunch with size n representing a collection of food for
    lunch, in which lunch[i][0] represents the amount of calories of the ith food
    and lunch[i][1] represents its delicious degree, and a binary array dinner
    with size m representing a collection of food for dinner, in which
    dinner[i][0] represents the amount of calories of the ith food and
    dinner[i][1] represents its delicious degree.  Please choose at most one kind
    of food in each collection, and to return the minimum calories you will take,
    while the sum of delicious degree of the chosen food should not be less than
    T.

    @param lunch: an array that contains each lunch food's calories and value
    @param dinner: an array that contains each dinner food's calories and value
    @param t: the minest limit value
    @return: return the min calories
    """

    def get_min_calories(
        self, lunch: List[List[int]], dinner: List[List[int]], t: int
    ) -> int:
        # write your code here
        lunch = sorted(lunch, key=lambda x: (x[1], x[0]))
        dinner = sorted(dinner, key=lambda x: (x[1], x[0]))

        # See if there is a single item that fulfills the delicious degree
        # requirement
        result = float("inf")
        for cal, degree in lunch:
            if degree >= t:
                result = min(result, cal)
        for cal, degree in dinner:
            if degree >= t:
                result = min(result, cal)

        h = [(cal, i) for i, (cal, _) in enumerate(lunch)]
        heapq.heapify(h)

        # Search from left of lunch (least delicious) and right of dinner
        # (most delicious)
        l = 0
        r = len(dinner) - 1
        while l < len(lunch) and 0 <= r:
            if lunch[l][1] + dinner[r][1] >= t:
                while h and h[0][1] < l:
                    heapq.heappop(h)
                result = min(result, h[0][0] + dinner[r][0])
                r -= 1
            else:
                l += 1

        if result == float("inf"):
            return -1
        return result
