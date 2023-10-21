class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        "Two-pass O(n) algorithm"
        merged = [
            *(it for it in intervals if it[0] < newInterval[0]),
            newInterval,
            *(it for it in intervals if it[0] >= newInterval[0]),
        ]

        answer = merged[:1]
        for it in merged[1:]:
            if answer[-1][1] < it[0]:
                answer.append(it)
                continue
            answer[-1][0] = min(answer[-1][0], it[0])
            answer[-1][1] = max(answer[-1][1], it[1])

        return answer