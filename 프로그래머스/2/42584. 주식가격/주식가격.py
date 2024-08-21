def solution(prices):
    n = len(prices)
    answer = [0] * n
    stack = []

    for i in range(n):
        # 현재 가격이 스택에 저장된 이전 가격보다 낮은 경우
        while stack and prices[i] < prices[stack[-1]]:
            j = stack.pop()
            answer[j] = i - j  # 가격이 떨어지기까지 걸린 시간 계산
        stack.append(i)  # 현재 인덱스를 스택에 추가
    
    while stack:
        i = stack.pop() 
        answer[i] = n - 1 - i  # 끝까지 가격이 떨어지지 않은 경우

    return answer