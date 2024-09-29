class AllOne:
    def __init__(self):
        self.m = dict()
        return

    def inc(self, key: str) -> None:
        self.m.setdefault(key, 0)
        self.m[key] += 1
        return

    def dec(self, key: str) -> None:
        self.m[key] -= 1
        if self.m[key] == 0:
            del self.m[key]
        return

    def getMaxKey(self) -> str:
        answer = ''; cnt = 0
        for k, v in self.m.items():
            if v > cnt:
                answer, cnt = k, v
        return answer

    def getMinKey(self) -> str:
        answer = ''; cnt = 987654321
        for k, v in self.m.items():
            if v < cnt:
                answer, cnt = k, v
        return answer
