class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        def calc(target: int):
            cnt = 0
            for i, ch in enumerate(boxes):
                if ch == '1':
                    cnt += abs(i - target)
            return cnt
        
        return [ calc(i) for i, _ in enumerate(boxes) ]
            