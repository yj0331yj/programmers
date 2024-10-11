def solution(s):
    answer = ''
    s1 = s.split(' ')

    for i in s1:
        for j in range(len(i)):
            if j % 2 == 0:
                answer += i[j].upper()
            else:
                answer += i[j].lower()
        answer += ' ' # 각 단어가 끝난 후 공백 추가
    return answer[:-1]  # 마지막 공백을 제거하고 반환