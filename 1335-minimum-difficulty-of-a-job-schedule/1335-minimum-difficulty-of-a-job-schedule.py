class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        '''
        1. Partition into the number of `d` groups.
        2. Pick the maximum number for each group.
        3. Accumulate picked numbers as an answer.
        '''

        if len(jobDifficulty) < d:
            return -1
        
        n = len(jobDifficulty)

        @cache
        def fn(i: int, d: int):
            if d == 1:
                return max(jobDifficulty[i:])
            
            answer = 987654321
            m = 0
            for j in range(i, n - d + 1):
                m = max(m, jobDifficulty[j])
                answer = min(
                    answer,
                    m + fn(j+1, d-1)
                )
            return answer
            
        return fn(0, d)
        
