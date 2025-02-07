class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        color_cnt = {}
        colors = {}

        def update(loc: int, color: int):
            if (prev_color := colors.get(loc)) is not None:
                color_cnt[prev_color] -= 1
                if color_cnt[prev_color] == 0:
                    del color_cnt[prev_color]

            colors[loc] = color
            color_cnt.setdefault(color, 0)
            color_cnt[color] += 1
            return

        answer = []
        for x, color in queries:
            update(x, color)
            answer.append( len(color_cnt) )

        return answer