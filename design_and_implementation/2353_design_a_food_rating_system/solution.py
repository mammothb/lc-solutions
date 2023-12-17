import heapq
from typing import List


class FoodRatings:
    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        n = len(foods)
        self.food_to_rating = {}
        self.food_to_cuisine = {}
        self.cuisine_to_food = {}
        for i in range(n):
            self.food_to_rating[foods[i]] = -ratings[i]
            self.food_to_cuisine[foods[i]] = cuisines[i]
            if cuisines[i] not in self.cuisine_to_food:
                self.cuisine_to_food[cuisines[i]] = []
            self.cuisine_to_food[cuisines[i]].append((-ratings[i], foods[i]))

        for cuisine in self.cuisine_to_food:
            heapq.heapify(self.cuisine_to_food[cuisine])

    def changeRating(self, food: str, newRating: int) -> None:
        self.food_to_rating[food] = -newRating
        heapq.heappush(
            self.cuisine_to_food[self.food_to_cuisine[food]], (-newRating, food)
        )

    def highestRated(self, cuisine: str) -> str:
        while (
            self.cuisine_to_food[cuisine]
            and self.cuisine_to_food[cuisine][0][0]
            != self.food_to_rating[self.cuisine_to_food[cuisine][0][1]]
        ):
            heapq.heappop(self.cuisine_to_food[cuisine])
        return self.cuisine_to_food[cuisine][0][1]


# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)
