def solution(n, computers):
    answer = 0
    visited = [False] * n
    
    def dfs(cur_v):
        visited[cur_v] = True
        for next_v in range(n):
            if computers[cur_v][next_v] == 1: # 연결됐을 경우(1인 경우)만 실행
                if not visited[next_v]:
                    dfs(next_v)
                    
    # 모든 노드에 대해서 dfs() 실행 시도 -> 실행되면 answer ++
    for cur_v in range(n):
        if not visited[cur_v]:
            dfs(cur_v)
            answer += 1
            
    return answer