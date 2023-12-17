from collections import defaultdict
from typing import List

from sortedcontainers import SortedList


class FoodRatings:
    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        """
        food -> entry (rating)
        cuisine -> entry
        """
        self.lookup = dict()
        self.q = defaultdict(
            lambda: SortedList(key=lambda it: (-it[0], it))
        )  # cuisine -> (rating, food) queue
        for food, cuisine, rating in zip(foods, cuisines, ratings):
            self.q[cuisine].add((rating, food))
            self.lookup[food] = (cuisine, (rating, food))
        return

    def changeRating(self, food: str, new_rating: int) -> None:
        cuisine, old_key = self.lookup[food]
        self.q[cuisine].remove(old_key)

        new_key = (new_rating, food)
        self.q[cuisine].add(new_key)

        self.lookup[food] = (cuisine, new_key)
        return

    def highestRated(self, cuisine: str) -> str:
        return self.q[cuisine][0][1]


# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)