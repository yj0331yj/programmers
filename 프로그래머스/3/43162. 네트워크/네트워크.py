from collections import deque
def solution(n, computers):
    answer = 0
    visited = [False] * n
    
    def bfs(start_v):
        q = deque()
        q.append(start_v)
        visited[start_v] = True
        
        while q:
            cur_v = q.popleft()
            for next_v in range(n):
                if computers[cur_v][next_v] == 1:
                    if not visited[next_v]:
                        q.append(next_v)
                        visited[next_v] = True
                        bfs(next_v)
    
    for cur_v in range(n):
        if not visited[cur_v]:
            bfs(cur_v)
            answer += 1
            
    return answer