#####################
# dfs


def dfs(node):
    print(node, end=' ')

    # 다음 재귀 호출
    # node 로 부터 갈 수 있는 노드들을 모두 확인
    # --> 그 중에서 한 곳으로 진행
    for next_node in graph[node]:
        # 이미 방문한 지점은 가지마라!
        if visited[next_node]:
            continue

        visited[next_node] = 1  # 방문처리
        dfs(next_node)


V, E = map(int, input().split())

# 인접 리스트 (연결된 간선만 저장)
graph = [[] for _ in range(V + 1)]
for _ in range(E):
    start, end = map(int, input().split())
    graph[start].append(end)
    graph[end].append(start)  # 양방향인 경우

visited = [0] * (V + 1)  # 방문 여부 기록
visited[1] = 1  # 출발점 초기화
dfs(1)


###############################
# bfs

from collections import deque


def bfs(start_node):
    # q의 의미: 다음에 방문해야 할 노드들 (후보열, 대기열)
    q = deque([start_node])  # 시작점을 queue 에 넣고 시작

    while q:
        # 1. 가장 앞의 노드를 뽑는다
        # 2. 해당 노드에서 갈 수 있는 노드들을 queue 에 넣는다.
        now = q.popleft()

        print(now, end=' ')

        for next_node in graph[now]:
            # 방문했으면 continue
            if visited[next_node]:
                continue

            visited[next_node] = 1
            q.append(next_node)


V, E = map(int, input().split())

# 인접 리스트 (연결된 간선만 저장)
graph = [[] for _ in range(V + 1)]
for _ in range(E):
    start, end = map(int, input().split())
    graph[start].append(end)
    graph[end].append(start)  # 양방향인 경우

visited = [0] * (V + 1)
visited[1] = 1
bfs(1)