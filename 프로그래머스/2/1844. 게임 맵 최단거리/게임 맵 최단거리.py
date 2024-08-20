from collections import deque

def solution(maps):
    dr = [1, 0, -1, 0]
    dc = [0, 1, 0, -1]
    n = len(maps)
    m = len(maps[0])
    queue = deque([(0, 0, 1)])

    while queue:
        x, y, d = queue.popleft()
        if x == n-1 and y == m-1:
            return maps[x][y]

        for i in range(4):
            nx = x + dr[i]
            ny = y + dc[i]

            if 0 <= nx < n and 0 <= ny < m:
                if maps[nx][ny] == 1 or maps[nx][ny] > d + 1:
                    maps[nx][ny] = d + 1
                    if nx == m - 1 and ny == n - 1:
                        return d + 1

                    queue.append((nx, ny, d + 1))

    return -1
