class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        indexer = lambda x: (k + x % k) % k
        counter = Counter(map(indexer, arr))

        def pop(it):
            counter[it] -= 1
            if not counter[it]:
                del counter[it]
            return

        while counter:
            it = next(iter(counter.keys()))
            pop(it)
            target  = indexer(k - it)
            if target not in counter:
                return False
            pop(target)

        return True
        


