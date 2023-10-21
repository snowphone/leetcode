class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        scores = defaultdict(list)
        for id, score in items:
            scores[id].append(score)
        
        answer = []
        for id, score_list in scores.items():
            score_list.sort(reverse=True)
            answer.append( (id, sum(score_list[:5]) // 5 ) )
        answer.sort()
        return answer
        
