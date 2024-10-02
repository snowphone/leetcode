class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        indexer = lambda x: (k + x % k) % k
        counter = Counter(map(indexer, arr))

        while counter:
            it = next(iter(counter.keys()))

            target  = indexer(k - it)
            if target not in counter:
                return False
                
            # Batch-compare
            if it == 0:
                if counter[it] & 1:
                    return False
            else:
                if counter[it] != counter[target]:
                    return False

            for jt in {it, target}:
                del counter[jt]

        return True