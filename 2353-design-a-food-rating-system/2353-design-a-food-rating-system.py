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
            key = self.q[cuisine].index((rating, food))
            self.lookup[food] = (cuisine, key)
        return

    def changeRating(self, food: str, new_rating: int) -> None:
        cuisine, old_key = self.lookup[food]
        del self.q[cuisine][old_key]

        new_entry = (new_rating, food)
        self.q[cuisine].add(new_entry)

        new_key = self.q[cuisine].index(new_entry)
        self.lookup[food] = (cuisine, new_key)
        return

    def highestRated(self, cuisine: str) -> str:
        return self.q[cuisine][0][1]
