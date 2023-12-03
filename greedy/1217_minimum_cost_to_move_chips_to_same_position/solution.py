import collections
import sys
from typing import List


class Solution:
    def min_cost_to_move_chips(self, position: List[int]) -> int:
        counter = collections.Counter(position)
        max_even_pos = -1
        max_even_count = 0
        max_odd_pos = -1
        max_odd_count = 0
        for pos, count in counter.items():
            if pos % 2 == 0:
                if count > max_even_count:
                    max_even_pos = pos
                    max_even_count = count
            else:
                if count > max_odd_count:
                    max_odd_pos = pos
                    max_odd_count = count
        even_result = sys.maxsize if max_even_pos == -1 else 0
        odd_result = sys.maxsize if max_odd_pos == -1 else 0
        for pos, count in counter.items():
            if max_even_pos >= 0 and abs(pos - max_even_pos) % 2 == 1:
                even_result += count
            if max_odd_pos >= 0 and abs(pos - max_odd_pos) % 2 == 1:
                odd_result += count
        return min(even_result, odd_result)

    def min_cost_to_move_chips_2(self, position: List[int]) -> int:
        even_result = 0
        odd_result = 0
        # Realize from prev solution that if we select the tallest odd position
        # stack, we're summing all the even position coins and vice versa.
        for pos in position:
            if pos % 2 == 0:
                odd_result += 1
            else:
                even_result += 1
        return min(even_result, odd_result)

    def min_cost_to_move_chips_3(self, position: List[int]) -> int:
        odd_result = 0
        for pos in position:
            if pos % 2 == 0:
                odd_result += 1
        # We can compute even_result by just "total - odd_result"
        return min(len(position) - odd_result, odd_result)
