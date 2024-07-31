class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        n = len(books)

        @cache
        def solve(idx):
            if idx == n:
                return 0

            answer = 2**31
            height = 0
            remaining_width = shelfWidth
            for i in range(idx, n):
                w, h = books[i]
                if w > remaining_width:
                    break
                remaining_width -= w
                height = max(h, height)
                answer = min(
                    answer,
                    height + solve(i + 1)
                )
            return answer

        return solve(0)
