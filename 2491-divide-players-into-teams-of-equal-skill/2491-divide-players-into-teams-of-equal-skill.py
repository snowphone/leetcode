from collections import Counter

class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        n_pairs = len(skill) // 2
        acc = sum(skill)

        if acc % n_pairs:
            return -1
        
        target = acc // n_pairs

        counter = Counter(skill)

        def pop(it):
            counter[it] -= 1
            if not counter[it]:
                del counter[it]
        answer = 0

        while counter:
            it = next(iter(counter.keys()))
            if (target - it) not in counter:
                return -1
            answer += (target-it) * it
            pop(it)
            pop(target - it)
            
        return answer
