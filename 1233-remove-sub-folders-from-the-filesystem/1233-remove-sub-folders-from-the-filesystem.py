class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        def pf(body, prefix):
            sz = len(prefix)
            return prefix == body[:sz]

        answer = []
        folder.sort()
        folder = sorted(
            it.split('/') for it in folder
        )

        n = len(folder)
        i = 0
        while i < n:
            it = folder[i]
            answer.append(it)
            i = next(
                (j for j in range(i+1, n) if not pf(folder[j],it)),
                n,
            )
        return [
            '/'.join(it) for it in answer
        ]
