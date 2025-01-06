class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        answer = [sum(i for i, ch in enumerate(boxes) if ch == "1")]
        n = len(boxes)
        # lsum: # of balls in [0, i]
        # rsum: # of balls in (i, n)
        lsum, rsum = int(boxes[0] == "1"), sum(ch == "1" for ch in boxes[1:])
        for i in range(1, n):
            answer.append(answer[-1] - rsum + lsum)

            lsum += int(boxes[i] == "1")
            rsum -= int(boxes[i] == "1")

        return answer
