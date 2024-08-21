from collections import deque

def solution(maps):
    answer = -1
    n = len(maps)
    m = len(maps[0])
    dr = [1, 0, -1, 0]
    dc = [0, 1, 0, -1]
    visited = [[False]*m for _ in range(n)]
    q = deque()
    
    if maps[0][0] == 1:
        q.append((0,0))
        visited[0][0] = True
        
        while q:
            cur_r, cur_c = q.popleft()
            if cur_r == n-1 and cur_c == m-1:
                return maps[cur_r][cur_c]
            
            for i in range(4):
                next_r = cur_r + dr[i]
                next_c = cur_c + dc[i]
                if 0 <= next_r < n and 0 <= next_c < m and maps[next_r][next_c] == 1:
                    if not visited[next_r][next_c]:
                        q.append((next_r, next_c))
                        visited[next_r][next_c] = True
                        maps[next_r][next_c] = maps[cur_r][cur_c] + 1
    
    return answer