def solution(arr):
    answer = [arr[0]]
    
    for i in arr:
        if not i == answer[-1]:
            answer.append(i)

    return answer