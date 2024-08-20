from collections import deque
def solution(maps):
    n = len(maps)
    m = len(maps[0])
    q = deque()
    dr = [1, 0, -1, 0]
    dc = [0, 1, 0, -1]
    visited = [[False] * m for _ in range(n)]

    # 시작점 예약
    if maps[0][0] == 1:
        q.append((0, 0))
        visited[0][0] = True

    while q:
        # 현재 노드 방문
        cur_r, cur_c = q.popleft()
        # 목표 지점에 도달했을 때 현재의 거리 반환
        if cur_r == n-1 and cur_c == m-1:
            return maps[cur_r][cur_c]

        # 다음 노드 예약
        for i in range(len(dr)):
            nr = cur_r + dr[i]
            nc = cur_c + dc[i]
            if 0 <= nr < n and 0 <= nc < m and maps[nr][nc] == 1:
                if not visited[nr][nc]:
                    q.append((nr, nc))
                    visited[nr][nc] = True
                    # 새로운 위치까지의 거리 업데이트
                    maps[nr][nc] = maps[cur_r][cur_c] + 1

    return -1
