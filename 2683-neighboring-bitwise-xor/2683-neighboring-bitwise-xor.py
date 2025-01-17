class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        n = len(derived)
        original = [0 for _ in range(n)]

    
        def try_with(start_value: int):
            original[0] = start_value
            for i, d in enumerate(derived):
                original[(i + 1) % n] = d ^ original[i]
            
            return original[0] == start_value
        
        return try_with(0) or try_with(1)
        