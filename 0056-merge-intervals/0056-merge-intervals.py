class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        
        answer = [intervals[0]]

        for beg, end in intervals[1:]:
            prev_beg, prev_end = answer[-1]
            if (prev_end >= beg):
                answer[-1] = [prev_beg, max(end, prev_end)]
            else:
                answer.append([beg, end])
        return answer