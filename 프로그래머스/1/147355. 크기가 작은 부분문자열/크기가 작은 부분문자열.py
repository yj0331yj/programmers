def solution(t, p):
    answer = 0
    lt = len(t)
    lp = len(p)
    for i in range(lt-lp+1):
        res = t[i:i+lp] # 부분 문자열 추출
        if res <= p:
            answer += 1
        else:
            continue
    return answer