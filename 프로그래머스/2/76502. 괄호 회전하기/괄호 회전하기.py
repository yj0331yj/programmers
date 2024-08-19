def solution(s):
    def is_valid(s):
        stack = []
        for i in s:
            if i in "({[":
                stack.append(i)
            else:
                if not stack:
                    return False
                if i == ")" and stack[-1] != "(":
                    return False
                if i == "]" and stack[-1] != "[":
                    return False
                if i == "}" and stack[-1] != "{":
                    return False
                stack.pop()
        return not stack

    answer = 0
    s_list = list(s)
    
    for _ in range(len(s_list)):
        if is_valid(s_list):
            answer += 1
        s_list.append(s_list.pop(0))  # 리스트 회전
    
    return answer