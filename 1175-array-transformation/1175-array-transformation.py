class Solution:
    def transformArray(self, arr: List[int]) -> List[int]:
        n = len(arr)
        answer = arr.copy()
        
        for i in range(1, n-1):
            if arr[i-1] > arr[i] < arr[i+1]:
                answer[i] += 1
            elif arr[i-1] < arr[i] > arr[i+1]:
                answer[i] -= 1

        return answer if arr == answer else self.transformArray(answer)