from collections import deque

def solution(numbers, target):
    answer = 0
    n = len(numbers)
    q = deque()
    q.append((0, 0))

    while q:
        idx, value = q.popleft()
        if idx == n and value == target:
            answer += 1
        elif idx == n:
            pass
        else:
            q.append((idx+1, value + numbers[idx]))
            q.append((idx+1, value - numbers[idx]))

    return answer