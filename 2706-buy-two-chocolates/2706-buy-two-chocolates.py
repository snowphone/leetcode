class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        prices.sort()
        acc = sum(prices[:2])

        return money - acc if money >= acc else money