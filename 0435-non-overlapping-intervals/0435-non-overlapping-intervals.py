class Solution:
    '''
    Merging intervals: Sort by start time
    Biggest non-overlapping intervals: Sort by finish time
    '''
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # Earliest Deadline-First Scheduling
        intervals.sort(key=itemgetter(1))

        refined = [intervals[0]]
        answer = 0
        for b, e in intervals[1:]:
            prev_b, prev_e = refined[-1]
            if prev_e == b:
                refined[-1] = (prev_b, e)
                continue
            elif prev_e < b:
                refined.append((b, e))
                continue

            answer += 1
        return answer
            
            