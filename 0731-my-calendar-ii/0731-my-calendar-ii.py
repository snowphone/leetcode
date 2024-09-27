class MyCalendarTwo:
    def __init__(self):
        self.bookings = []
        self.double_bookings = []
        return

    def book(self, start: int, end: int) -> bool:
        last = end - 1
        booking = (start, last)

        if any(
            self._overlap(booking, it)
            for it in self.double_bookings
        ):
            return False

        self.double_bookings += [
            self._overlapped(it, booking)
            for it in self.bookings
            if self._overlap(it, booking)
        ]
        self.bookings.append(booking)
        return True


    def _overlap(self, lhs: tuple[int, int], rhs: tuple[int, int]):
        return max(lhs[0], rhs[0]) <= min(lhs[1], rhs[1])

    def _overlapped(self, lhs: tuple[int, int], rhs: tuple[int, int]):
        return (max(lhs[0], rhs[0]), min(lhs[1], rhs[1]))
            
