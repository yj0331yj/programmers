from collections import deque

def solution(numbers, target):
    answer = 0
    n = len(numbers)
    q = deque()
    q.append((0, 0))  # 초기 설정: (인덱스, 현재까지의 합)

    while q:
        i, value = q.popleft()
        # 모든 숫자를 사용한 경우 현재까지의 합이 목표값과 같다면 답을 1 증가
        if i == n and value == target:
            answer += 1
        # 모든 숫자를 사용했지만 목표값과 다를 경우 pass
        elif i == n:
            pass
        # 아직 모든 숫자를 사용하지 않은 경우
        else:
            q.append((i+1, value + numbers[i])) # 현재 숫자를 더한 경우를 큐에 추가
            q.append((i+1, value - numbers[i])) # 현재 숫자를 뺀 경우를 큐에 추가
    
    return answer
