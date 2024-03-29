from collections import deque
import sys
input = sys.stdin.readline

dx = [0, 0, 1, -1] # 좌우
dy = [1, -1, 0, 0] # 상하

def bfs(graph, a, b):
    n = len(graph)
    queue = deque()
    queue.append((a, b))
    graph[a][b] = 0
    count = 1
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if ls[nx][ny] == 1:
                graph[nx][ny] = 0
                queue.append((nx, ny))
                count += 1
    return count


n = int(input())
ls = []
for i in range(n):
    ls.append(list(map(int, input())))

cnt = []
for i in range(n):
    for j in range(n):
        if ls[i][j] == 1:
            cnt.append(bfs(ls, i, j))

cnt.sort()
print(len(cnt))
print(*cnt, end='\n')

