from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.items = OrderedDict()  # front: least recently used
        return

    def get(self, key: int) -> int:
        if key not in self.items:
            return -1

        self.items.move_to_end(key)
        return self.items[key]

    def put(self, key: int, value: int) -> None:
        if key in self.items:
            self.items.pop(key)

        if len(self.items) == self.capacity:
            k = next(iter(self.items.keys()))
            self.items.pop(k)
        
        self.items[key] = value
        return
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)