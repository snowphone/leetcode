from bisect import bisect_left

class MyCalendar:
    def __init__(self):
        self.arr = []
        
    def book(self, start: int, end: int) -> bool:
        last = end - 1  # To make [start, last]
        idx = bisect_left(self.arr, (start, last))
        
        prev_start, prev_last = self.arr[idx-1] if idx > 0 else (-1, -1)
        if not (prev_last < start):
            return False
        next_start, next_last = self.arr[idx] if idx < len(self.arr) else (10**9+1, 10**9+1)
        if not (last < next_start):
            return False
        
        self.arr.insert(idx, (start, last))
        return True
        


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)