from collections import deque
def solution(numbers, target):
    answer = 0
    n = len(numbers)
    q = deque()
    q.append([-numbers[0], 0])
    q.append([+numbers[0], 0])

    while q:
        num, i = q.popleft()
        if i + 1 == n:
            if num == target:
                answer += 1
        else:
            q.append([num - numbers[i+1], i+1])
            q.append([num + numbers[i+1], i+1])
        
    return answer
