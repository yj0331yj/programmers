def solution(participant, completion):
    participant_dict = {}

    # participant에서 각 이름 출현 횟수 확인(동명이인도 카운트)
    for i in participant:
        if i in participant_dict:
            participant_dict[i] += 1
        else:
            participant_dict[i] = 1

    # completion에 있는 완주자 이름 제거
    for i in completion:
        participant_dict[i] -= 1

    # participant_dict에 남아 있는 완주하지 못한 사람 찾기
    for i in participant_dict:
        if participant_dict[i] > 0:
            return i


