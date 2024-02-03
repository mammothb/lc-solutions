import collections
from typing import List


class Solution:
    """
    @param cards: A list of cards.
    @return: A list of feasible solution.
             we will sort your return value in output
    """

    def get_the_number(self, cards: List[int]) -> List[int]:
        # write your code here
        result = []
        counter = collections.Counter(cards)
        for i in range(1, 10):
            if counter[i] < 4 and self.is_valid(cards + [i]):
                result.append(i)
        if result:
            return result
        return [0]

    def is_valid(self, cards):
        if not cards:
            return True
        cards = sorted(cards)
        curr = cards[0]
        counter = collections.Counter(cards)
        # sparrow head is at the beginning
        if len(cards) % 3 == 2 and counter[curr] >= 2 and self.is_valid(cards[2:]):
            return True
        # kezi at the beginning
        if counter[curr] >= 3 and self.is_valid(cards[3:]):
            return True
        # shunzi at the beginning
        if counter[curr + 1] > 0 and counter[curr + 2] > 0:
            counter[curr] -= 1
            counter[curr + 1] -= 1
            counter[curr + 2] -= 1
            temp = []
            for num, count in counter.items():
                for _ in range(count):
                    temp.append(num)
            if self.is_valid(temp):
                return True
        return False
