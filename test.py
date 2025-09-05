# import sys
# sys.stdin = open("input.txt", "r")


#
# path = []
#
# def dfs(x):
#     if x == 3:
#         print(*path)
#         return
#
#     for i in range(1, 7):
#         path.append(i)
#         dfs(x + 1)
#         path.pop()
# dfs(0)

# N = int(input())
# path = []
# used = [0] * 7
# def dfs(x):
#     if x == N:
#         print(*path)
#         return
#
#     for i in range(1, 7):
#         if used[i] == 1: continue
#         used[i] = 1
#         path.append(i)
#         dfs(x + 1)
#         path.pop()
#         used[i] = 0
# dfs(0)


# import sys
# sys.stdin = open("input.txt", "r")
#
# N = int(input())
# path = []
#
# cnt = 0
# def dfs(x):
#     global cnt
#     if x == N:
#         if sum(path) <= 10:
#             cnt += 1
#         return
#
#     for i in range(1, 7):
#         path.append(i)
#         dfs(x + 1)
#         path.pop()
#
# dfs(0)
# print(cnt)


# import sys
# sys.stdin = open("input.txt", "r")
#
# arr = ['A', 'B', 'C', 'D', 'E']
# path = []
#
# def get_str(lev, start):
#     if lev == 3:
#         print(*path)
#         return
#     for i in range(start, 5):
#         path.append(arr[i])
#         get_str(lev + 1, i + 1)
#         path.pop()
# get_str(0, 0)
# N = int(input())
# path = []
# def get_num(lev, start):
#     if lev == N:
#         print(*path)
#         return
#
#     for i in range(start, 7):
#         path.append(i)
#         get_num(lev + 1, i)
#         path.pop()
#
# get_num(0, 1)

# T = int(input())
# for tc in range(1, T + 1):
#     num = float(input())
#     r = 0
#
#     if num >= 0.5:
#         r += 0.1
#         num -= 0.5
#     if num >= 0.25:
#         r += 0.01
#         num -= 0.25
#     if num >= 0.125:
#         r += 0.001
#         num -= 0.125
#     if num >= 0.0625:
#         r += 0.0001
#         num -= 0.0625
#     if num >= 0.03125:
#         r += 0.00001
#         num -= 0.03125
#
#     r = str(r)
#     r = r[r.find('.')+1:]
#     if r < 3:
#         r = 'overflow'
#     print(r)



# def change(n):
#     binary = ''
#     power = -1
#     cnt = 0
#
#     while n > 0 and cnt < 13:
#         value = 2 ** power      # 2의 -1제곱, 2의 -2제곱 ...
#
#         if n >= value:      # 현재 자리값을 뺄 수 있다
#             binary += '1'
#             n -= value
#         else:
#             binary += '0'
#         power -= 1
#         cnt += 1
#     if n > 0:
#         return 'overflow'
#     else:
#         return binary
#
# T = int(input())
# for tc in range(1, T + 1):
#     num = float(input())
#     result = change(num)
#     print(f'#{tc} {result}')


# import sys
# sys.stdin = open("input.txt", "r")

'''arr = ['O', 'X']
name = ['A', 'B', 'C', 'D', 'E']
path = []

def get_name():
    for i in range(len(name)):
        if path[i] == 'O':
            print(name[i], end=' ')

    print()

def get_subset(lev):

    if lev == len(name):
        get_name()
        return

    for i in range(2):
        path.append(arr[i])
        get_subset(lev + 1)
        path.pop()
get_subset(0)
print(cnt)
'''


# import sys
# sys.stdin = open("input.txt", "r")
#
# N = int(input())
# path = []
# def get_num(lev, start):
#     if lev == N:
#         print(*path)
#         return
#
#     for i in range(start, 7):
#         path.append(i)
#         get_num(lev + 1, start + i - 1)
#         path.pop()
# get_num(0, 1)

# name = ['Luffy', 'Zoro', 'Sanji']
# path = []
# arr = [1, 0]
#
# def get_name():
#     for i in range(len(name)):
#         if path[i] == 1:
#             print(name[i], end=' ')
#     print()
# def get_subset(lev):
#     if lev == 3:
#         get_name()
#         return
#
#     for i in range(2):
#         path.append(arr[i])
#         get_subset(lev + 1)
#         path.pop()
# get_subset(0)


#######################
# 이진수 표현

# import sys
# sys.stdin = open("input.txt", "r")
#
# T = int(input())
# for tc in range(1, T + 1):
#     N, M = list(map(int, input().split()))
#
#     bit = 'ON'
#     for i in range(N):
#         if M & (1 << i) == 1: continue
#         bit = "OFF"
#         break
#
#
#     print(f'#{tc} {bit}')


#####################################
# 어학 능력 향상 교육

# import sys
# sys.stdin = open("input.txt", "r")



##########################
# 이진수2

# import sys
# sys.stdin = open("input.txt", "r")
#
# T = int(input())
# for tc in range(1, T + 1):
#     N = float(input())
#


# arr = [[], [], [], [], []]
# arr[0] = ['U', 'R', 'K']
# arr[1] = ['S', 'R']
# arr[3] = ['S', 'K']
# arr[4] = ['R', 'U']
# N = int(input())
# for i in arr[N]:
#     print(i)


# arr = [[0] * 6 for _ in range(6)]
#
# arr[0][0] = 'A'
# arr[0][1] = 'B'
# arr[0][2] = 'T'
# arr[0][3] = 'Q'
# arr[1][4] = 'V'
# arr[1][5] = 'X'
#
# N = int(input())
# for i in range(len(arr)):
#     if i > 0 and arr[N][i] != 0:
#         print(arr[N][i])


# arr = [[0] * 6 for _ in range(6)]
#
# arr[0][1] = 1
# arr[0][2] = 1
# arr[0][3] = 1
# arr[1][4] = 1
# arr[1][5] = 1
# def dfs(n):
#     print(n, end=' ')
#     for i in range(6):
#         if arr[n][i] == 0: continue
#         dfs(i)
#
# dfs(0)

# arr = [[0] * 4 for _ in range(4)]
# arr[0] = [1, 3]
# arr[1] = [2]
# arr[2] = [0, 3]
# arr[3] = [2]
# used = [0] * 4
# used[0] = 1

'''############
# 인접행렬
arr = [[0] * 4 for _ in range(4)]
arr[0][1] = 1
arr[0][3] = 1
arr[1][2] = 1
arr[2][0] = 1
arr[2][3] = 1
arr[3][2] = 1

used = [0] * 4
used[0] = 1

def dfs(n):
    print(n)
    for i in range(4):
        if arr[n] == 0: continue
        # 이미 갔던 곳(방문했던 곳)이라면 무시
        if used[i] == 1: continue
        used[i] = 1
        dfs(i)
dfs(0)'''

####################################
# 인접리스트
'''
arr = [[0] * 4 for _ in range(4)]

arr[0] = [1, 3]
arr[1] = [2]
arr[2] = [0, 3]
arr[3] = [2]

used = [0] * 4
used[0] = 1
def dfs(n):
    print(n)
    for i in range(len(arr[n])):
        next = arr[n][i]
        if used[next] == 1: continue

        used[next] = 1
        dfs(n + 1)
dfs(0)
'''


###################################
# DFS 시작 3 가중치

'''n = int(input())
MAP = [
    [0, 7, 20, 8],
    [0, 0, 5, 0],
    [15, 0, 0, 0],
    [0, 0, 6, 0]
]

used = [0] * 4
used[0] = 1  # 시작노드 방문처리


# 모든 경로를 탐색 (used배열을 지워줘야한다)
def dfs(now, sum_v):
    if now == n:  # 목적지에 도착하면
        print(sum_v, end=' ')

    for i in range(4):
        if MAP[now][i] == 0: continue
        if used[i] == 1: continue
        used[i] = 1
        # dfs(i, sum_v + 인접행렬의 좌표)
        dfs(i, sum_v + MAP[now][i])
        used[i] = 0  # 모든 경로 탐색


dfs(0, 0)'''



##########################################
# DFS final

'''a, b = map(int, input().split())
arr = [[0] * 6 for _ in range(6)]
max_v = 0
min_v = float('inf')


arr[0][1] = 2
arr[0][2] = 6
arr[0][3] = 3
arr[1][0] = 2
arr[1][2] = 7
arr[1][3] = 4
arr[2][0] = 6
arr[2][1] = 7
arr[3][0] = 3
arr[3][1] = 4
arr[3][2] = 2
arr[4][2] = 1
arr[4][5] = 7


used = [0] * 6
used[a] = 1
def dfs(n, sum_v):
    global max_v
    global min_v

    if n == b:
        max_v = max(max_v, sum_v)
        min_v = min(min_v, sum_v)
        return
    for i in range(6):
        if arr[n][i] == 0: continue
        if used[i] == 1: continue
        used[i] = 1
        dfs(i, sum_v + arr[n][i])
        used[i] = 0

dfs(a, 0)
print(max_v)
print(min_v)'''


###########################################
# boss 문제 - 럭셔리 여행

# import sys
# sys.stdin = open("input.txt", "r")
#
# `N = int(input())
# arr = [list(map(int, input().split())) for _ in range(N)]
# a, b = map(int, input().split())
#
# max_v = float('-inf')
# min_v = float('inf')
#
# used = [0] * N
# used[a] = 1
#
# def dfs(now, sum_v):
#     global max_v
#     global min_v
#
#     if now == b:
#         max_v = max(max_v, sum_v)
#         min_v = min(min_v, sum_v)
#         return
#
#     for i in range(N):
#         if arr[now][i] == 0: continue
#         if used[i] == 1: continue
#         used[i] = 1
#         dfs(i , sum_v + arr[now][i])
#         used[i] = 0
#
# dfs(a, 0)
#
# print(min_v)
# print(max_v)
