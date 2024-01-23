class Solution:
    def maxLength(self, arr: List[str]) -> int:

        new_arr = [
            jt for it in arr if len(it) == len( jt := frozenset(it) )
        ]
        
        arr = new_arr
        n = len(arr)
        
        def fn(i: int, ans: set[str]):
            if i == n:
                return ans

            if arr[i] & ans:
                return fn(i+1, ans)
            else:
                return max(
                    fn(i+1, ans),
                    fn(i+1, ans | arr[i]),
                    key=len,
                )
        return len(fn(0, frozenset() )) if arr else 0