class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stk = []

        for log in logs:
            if log == './':
                continue
            elif log == '../':
                stk and stk.pop()
            else:
                stk.append(log)
        return len(stk)