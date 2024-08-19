def solution(s):
    stack = []
    
    for i in s:
        # '('일 경우 스택에 넣기
        if i == '(': 
            stack.append(i)
        # ')'일 경우 스택에서 여는 괄호를 제거 -> 스택이 비어있다면 짝이 맞지 않으므로 False를 반환
        elif i == ')':
            if stack:
                stack.pop()
            else:
                return False
    
    # 스택이 비어 있으면 True, 비어 있지 않으면 False를 반환
    return not stack
