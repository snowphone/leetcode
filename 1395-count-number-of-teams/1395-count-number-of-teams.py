class Solution:
    def numTeams(self, rating: List[int]) -> int:
        n = len(rating)

        @cache
        def solve(team_cnt: int, start_idx: int):
            if start_idx == n:
                return 0
            if team_cnt == 3:
                return 1
    
            answer = 0
            for i in range(start_idx+1, n):
                if rating[start_idx] >= rating[i]:
                    continue
                answer += solve(team_cnt + 1, i)
            return answer

        answer = 0
        answer += sum(solve(1, i) for i in range(n))

        solve.cache_clear()
        rating.reverse()
        answer += sum(solve(1, i) for i in range(n))

        return answer