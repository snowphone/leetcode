from bisect import bisect_left

class Solution:
    def _organize(self, items: list[list[int]]):
        items.sort()
        organized = defaultdict(int)
        for p, b in items:
            organized[p] = max(organized[p], b)
        
        return [
            (p, b) for p, b in organized.items()
        ]

    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        items = self._organize(items)

        @cache
        def query(max_price: int):
            inf = 10**9 + 1
            idx = bisect_left(items, (max_price, inf) )
            if idx == 0:
                return 0
            p, b = items[idx-1]
            return max( query(p-1), b )

        return [
            query(max_price) for max_price in queries
        ]