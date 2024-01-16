from random import choice

class RandomizedSet:
    "Problem stated from Moloco"
    def __init__(self):
        self.items = list()
        self.val_to_index = dict()

    def insert(self, val: int) -> bool:
        if val in self.val_to_index:
            return False
        self.items.append(val)
        self.val_to_index[val] = len(self.items) - 1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.val_to_index:
            return False

        idx = self.val_to_index[val]

        last_elem = self.items[-1]
        last_elem_idx = self.val_to_index[last_elem]


        del self.val_to_index[val]
        self.items.pop()

        if idx != last_elem_idx:
            self.items[idx] = last_elem
            self.val_to_index[last_elem] = idx
        return True

    def getRandom(self) -> int:
        return choice(self.items)