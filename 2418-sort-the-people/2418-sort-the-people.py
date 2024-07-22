class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        n = len(names)
        return [
            names[i] for i in 
            sorted(range(n), key=lambda i: heights[i], reverse=True)
        ] 
        