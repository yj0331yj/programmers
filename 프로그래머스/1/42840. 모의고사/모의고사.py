def solution(answers):
    answer = []
    supoja1 = [1, 2, 3, 4, 5]
    supoja2 = [2, 1, 2, 3, 2, 4, 2, 5,]
    supoja3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    score1 = 0
    score2 = 0
    score3 = 0
    
    for i in range(len(answers)):
        if answers[i] == supoja1[i % len(supoja1)]:
            score1 += 1
        if answers[i] == supoja2[i % len(supoja2)]:
            score2 += 1
        if answers[i] == supoja3[i % len(supoja3)]:
            score3 += 1
    
    score = [score1, score2, score3]
    m = max(score) 
    
    for idx, val in enumerate(score):
        if val == m:
            answer.append(idx + 1)
        
    return answer