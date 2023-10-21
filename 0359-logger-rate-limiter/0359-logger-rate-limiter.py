class Logger:

    def __init__(self):
        self.cache = dict()

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        before = self.cache.get(message, -987654321)
        if before + 10 <= timestamp:
            self.cache[message] = timestamp
            return True
        return False
        


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)