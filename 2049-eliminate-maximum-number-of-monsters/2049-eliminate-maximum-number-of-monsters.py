class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        """
        Kill the monster that takes the minimum time to reach the city.
        """
        kill_cnt = 0
        n = len(dist)

        time_to_reach = [ dist[i] / speed[i] for i in range(n) ]
        time_to_reach.sort()

        for t, it in enumerate(time_to_reach, 0):
            if t >= it:
                return t
            continue
        return n
        

            

