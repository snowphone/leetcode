from sortedcontainers import SortedList

class NumberContainers:

    def __init__(self):
        self.container = {}
        self.rev = defaultdict(SortedList)

    def change(self, index: int, number: int) -> None:
        "O(log(n))"
        prev_number = self.container.get(index)
        if prev_number is not None:
            self.rev[prev_number].remove(index)

        self.container[index] = number
        self.rev[number].add(index)

    def find(self, number: int) -> int:
        'O(1)'
        indices = self.rev[number]
        return indices[0] if indices else -1


# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)