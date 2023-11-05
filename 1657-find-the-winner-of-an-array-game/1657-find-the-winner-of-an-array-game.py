from sortedcontainers import SortedSet

class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:

        if arr[0] == max(arr[:k+1]):
          return arr[0]

        k = min(k, len(arr))
        n = len(arr)

        window = SortedSet()
        r = 0
        for i in range(1, n):
          # sz == arr[i+1, r] both inclusive
          # sz == k - 1
          # r - (i + 1) + 1 == k-1
          # r == (k-1) + (i+1) - 1
          # r == k + i - 1

          while r < min(k + i - 1, n-1):
            r += 1
            window.add(arr[r])

          # 우측만 이기면 된다. 내 왼쪽은 이미 다 이겼으므로.
          #if arr[i] == max(arr[i:e]):
          if arr[i] == window[-1]:
            return arr[i]


