def solution(n):
    answer = 0
    
    while n:
        answer = answer * 3 + n % 3
        n = n // 3
    
    return answer