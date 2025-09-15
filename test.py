import sys
sys.stdin = open("input.txt", "r")


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

# from collections import deque
#
# T = int(input())
# for tc in range(1, T + 1):
#     N, M = map(int, input().split())
#     arr = deque(map(int, input().split()))
#     for i in range(M):
#         arr.append(arr.popleft())
#     print(f'#{tc} {arr[0]}')


# import heapq
# pq = []
# sort_arr = []
# heapq.heappush(pq, 5)
# while pq:
#     sort_arr.append(heapq.heappop(pq))
# print(sort_arr)

# from collections import deque
#
# alist = [[] for _ in range(7)]
# alist[5] = [3, 1]
# alist[3] = [2]
# alist[1] = [4]
# alist[4] = [0, 6]
#
#
# q = deque
# q.append((5))
#
# while q:
#     now = q[0]
#     q.popleft()
#     print(now, end=' ')
#
#     for i in range(len(alist[now])):
#         next = alist[now][i]
#         q.append(next)


##############################################
# Baby-gin


'''
used = [0] * 6
path = []
is_babygin = 0
def is_baby_gin():
    cnt = 0

    a, b, c = path[0], path[1], path[2]
    if a == b == c: cnt += 1
    elif a == (b -1) == (c -2) : cnt += 1

    a, b, c = path[3], path[4], path[5]
    if a == b == c: cnt += 1
    elif a == (b -1) == (c -2) : cnt += 1

    return cnt == 2

def recur(lev):
    global is_babygin
    if lev == 6:
        if is_baby_gin():
            is_babygin = 1
        return

    for i in range(6):
        if used[i] == 1: continue
        used[i] = 1
        path.append(arr[i])
        recur(lev + 1)
        path.pop()
        used[i] = 0

arr = list(map(int, input().split()))
recur(0)
if is_babygin: print('Yes')
else: print('No')
'''


###########################
# 최소합

# import sys
# sys.stdin = open("input.txt", "r")



# def dfs(y, x, sum_v):
#     global min_sum
#
#     if y == N-1 and x == N-1:
#         min_sum = min(min_sum, sum_v)
#         return
#         # 가지치기
#     if min_sum <= sum_v: return
#
#
#     if x < N -1:
#         dfs(y, x + 1, sum_v + arr[y][x+1])
#     if y < N -1:
#         dfs(y + 1, x, sum_v + arr[y+1][x])
#
# T = int(input())
# for tc in range(1, T + 1):
#     N = int(input())
#     arr = [list(map(int, input().split())) for _ in range(N)]
#     min_sum = float('inf')
#
#     dfs(0, 0, arr[0][0])
#     print(f'#{tc} {min_sum}')



##########################################
# 전자카트

'''
def dfs(lev, sum_v):
    global min_v

    # 마지막 구역에서 사무실로 돌아오는 비용
    if lev == N - 1:
        sum_v += arr[path[-1]][0]
        min_v = min(min_v, sum_v)
        return


    for i in range(1, N):
        if used[i] == 1: continue
        used[i] = 1
        path.append(i)
        dfs(lev + 1, sum_v + arr[path[-2]][i])
        path.pop()
        used[i] = 0

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    min_v = float('inf')
    path = [0]
    used = [0] * N
    used[0] = 1
    dfs(0, 0)
    print(f'#{tc} {min_v}')
'''


#################################################################################
'''
def baby_gin():
    cnt = 0

    a, b, c = path[0], path[1], path[2]
    if a == b == c: cnt += 1
    elif a == (b-1) == (c-1): cnt += 1

    a, b, c = path[3], path[4], path[5]
    if a == b == c: cnt += 1
    elif a == (b-1) == (c-1): cnt += 1

    return cnt == 2



def dfs(lev):
    global is_babygin

    if lev == 6:
        if baby_gin():
            is_babygin = 1
        return

    for i in range(6):
        if used[i] == 1: continue
        used[i] = 1
        path.append(arr[i])
        dfs(lev + 1)
        path.pop()
        used[i] = 0


used = [0] * 6
path = []
arr = list(map(int, input().split()))
is_babygin = 0

dfs(0)
if is_babygin: print('Yes')
else: print('No')'''






###################################
# 증가하는 사탕 수열

'''
####### 함수 O
T = int(input())
for tc in range(1, T + 1):
    a, b, c = map(int, input().split())
    eat_cnt = 0

    if a < 1 or b < 2 or c < 3:
        print(f'#{tc} -1')
        continue
    elif a < b < c:
        print(f'#{tc} 0')
        continue

    if b >= c:
        eat_cnt += (b - c + 1)
        b -= eat_cnt
    if a >= b:
        eat_cnt += (a - b + 1)
        a -= eat_cnt
    print(f'#{tc} {eat_cnt}')


####### 함수 X
def cnt_candy(a, b, c):
    eat_cnt = 0

    if a < 1 or b < 2 or c < 3: return -1
    if a < b < c: return 0

    if b >= c:
        eat_cnt += (b - c + 1)
        b -= eat_cnt
    if a >= b:
        eat_cnt += (a - b + 1)
        a -= eat_cnt
    return eat_cnt

T = int(input())
for tc in range(1, T + 1):
    a, b, c = map(int, input().split())
    print(f'#{tc} {cnt_candy(a, b, c)}')
'''


#############################
# 전봇대



'''
def get_result():
    size = len(arr)
    cnt = 0

    for i in range(len(arr)): # 기준이 되는 전봇대
        for tar in range(i): # 갯수를 세야하는 전봇대
            # a 첫번째 전봇대, b 두번째 전봇대
            i_a, i_b = arr[i][0], arr[i][1]
            tar_a, tar_b = arr[tar][0], arr[tar][1]

            if i_b < tar_b: cnt += 1

    return cnt


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr=[]
    for n in range(N):
        a, b = map(int, input().split()) # 전봇대
        arr.append((a, b))

    arr.sort(key=lambda x : x[0]) # 첫 번째 원소(a전봇대)를 기준으로 정렬
    result = get_result()
    print(f'#{tc} {result}')
'''

####################
# 탈주범 검거

'''
from collections import deque
alist = [[] * for _ in range(7)]

alist[0] = [1, 2]
alist[1] = [3]
alist[2] = [4]
alist[4] = [5, 6]

q = deque()
q.append(0)

while q:
    '''


'''from collections import deque

alist = list([] for _ in range(5))

alist[0] = [1, 2]
alist[1] = [0, 2]
alist[2] = [0, 1, 3]
alist[3] = [2, 4]
alist[4] = [3]
q = deque()

N = int(input())
q.append(N)
used = [0] * 6
used[N] = 1

while q:
    now = q[0]
    print(chr(now + ord('A')), end = ' ')
    q.popleft()

    for i in range(len(alist[now])):
        next = alist[now][i]

        if used[next] == 1: continue
        used[next] = 1
        q.append(next)'''

'''
from collections import deque

alist = [[0] * 5 for _ in range(5)]

alist[0][1] = 1
alist[0][4] = 1
alist[1][3] = 1
alist[1][4] = 1
alist[2][0] = 1
alist[3][0] = 1
alist[3][2] = 1
q = deque()
s, e = map(int, input().split())
used = [0] * 5
used[s] = 1
q.append((s, 0))

while q:
    now, level = q[0]
    q.popleft()
    if now == e:
        print(level)
    for i in range(5):
        if alist[now][i] == 0: continue
        if used[i] == 1: continue
        used[i] = 1
        q.append((i, level + 1))
'''

'''
from collections import deque
visited = [[0] * 5 for _ in range(5)]

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

def flood_fill(start_y, start_x):
    q = deque()
    q.append((start_y, start_x))
    visited[start_y][start_x] = 1

    while q:
        now_y, now_x = q.popleft()

        for i in range(4):
            ny = now_y + dy[i]
            nx = now_x + dx[i]

            if ny < 0 or nx < 0 or ny >= 5 or nx >= 5: continue

            if visited[ny][nx] != 0:continue
            visited[ny][nx] = visited[now_y][now_x] + 1
            q.append((ny, nx))

sty, stx = map(int, input().split())
flood_fill(sty, stx)

for y in range(5):
    for x in range(5):
        print(visited[y][x], end=' ')
    print()
'''


'''
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    result = merge(left, right)
    return result

def merge(left, right):
    result = []
    i, j = 0, 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result

arr = [64, 34, 25, 12, 22, 11, 90]
sorted_arr = merge_sort(arr)
print(*sorted_arr)
'''

#####################
# 병합 정렬

'''
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    result = merge(left, right)

    return result

def merge(left, right):
    global cnt
    result = []
    i, j = 0, 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    if j > i: cnt += 1
    # if left[-1] > right[-1]: cnt += 1
    result.extend(left[i:])

    result.extend(right[j:])

    return result

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    cnt = 0
    sorted_arr = merge_sort(arr)

    print(f'#{tc} {sorted_arr[N//2]} {cnt}')
'''





# def quick_sort():
# def quick_sort(arr):
#     if len(arr) <= 1: return arr
#
#     pivot = arr[len(arr) // 2]
#     left = [x for x in arr if x < pivot]
#     middle = [x for x in arr if x == pivot]
#     right = [x for x in arr if x > pivot]
#
#     result = quick_sort(left) + middle + quick_sort(right)
#     return result
#
# T = int(input())
# for tc in range(1, T + 1):
#     N = int(input())
#     arr = list(map(int, input().split()))
#     sorted_arr = quick_sort(arr)
#
#     print(f'#{tc} {sorted_arr[len(sorted_arr) // 2]}')





# 이진탐색 (먼저 sort()하고 탐색) | start, middle, end 는 인덱스



# def binary_search(arr, target):
#     global cnt
#     start = 0
#     end = len(arr) - 1
#     flag = 0
#
#     while start <= end: # start와 end가 같아질때까지
#         mid = (start + end) // 2
#         # 이진 탐색을 통해서 타겟을 찾으면 middle 인덱스 반환
#         if arr[mid] == target:
#             return True
#         # 타겟이 중간값 보다 크면 오른쪽 부분 탐색
#         elif arr[mid] < target:
#             if flag == 2: break
#             flag = 2
#             start = mid + 1
#         else: # 타겟이 중간값보다 작으면 왼쪽 부분 탐색
#             if flag == 1: break
#             flag = 1
#             end = mid - 1
#     # 타겟 못찾으면
#     return False
# T = int(input())
# for tc in range(1, T + 1):
#     N, M = map(int, input().split())
#     a_list = sorted(list(map(int, input().split())))
#     b_list = list(map(int, input().split()))
#     cnt = 0
#     for i in b_list:
#         cnt += binary_search(a_list, i)
#     print(f'#{tc} {cnt}')



'''from collections import deque

alist = list([] for _ in range(5))

alist[0] = [1, 2]
alist[1] = [0, 2]
alist[2] = [0, 1, 3]
alist[3] = [2, 4]
alist[4] = [3]

N = int(input())
q = deque()
q.append(N)

used = [0] * 5
used[N] = 1

while q:

    now = q[0]
    print( chr(now + ord('A')),end=' ')
    q.popleft()
    for i in range(len(alist[now])):
        next = alist[now][i]

        if used[next] == 1: continue
        used[next] = 1
        q.append(next)
'''
#################
# N Queen

# N = int(input())



# arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# ox = ['O', 'X']
# path = []
#
# def get_arr():
#     sum_v = 0
#     num = []
#     for i in range(10):
#         if path[i] == 'O':
#             sum_v += arr[i]
#             if sum_v > 10: return
#             num.append(arr[i])
#     if sum_v == 10:
#         print(*num)
#
# def dfs(lev):
#     if lev == 10:
#         get_arr()
#         return
#
#     for i in range(2):
#         path.append(ox[i])
#         dfs(lev + 1)
#         path.pop()
# dfs(0)

'''used = [0] * 20
used1 = [0] * 100
used2 = [0] * 100
def queen(row):
    global cnt
    if row == N:
        cnt += 1
        return

    for col in range(N):
        if used[col] == 1: continue
        if used1[col + row] == 1 : continue
        if used2[col - row + N] == 1: continue

        used[col] = 1
        used1[col + row] = 1
        used2[col - row + N] = 1

        queen(row + 1)

        used[col] = 0
        used1[col + row] = 0
        used2[col - row + N] = 0

cnt = 0
N = int(input())
queen(0)
print(cnt)'''

# from collections import deque
#
#
# alist = [[0] * 5 for _ in range(5)]
#
# alist[0][1] = 1
# alist[0][4] = 1
# alist[1][3] = 1
# alist[1][4] = 1
# alist[2][0] = 1
# alist[3][0] = 1
# alist[3][2] = 1
#
#
# s, e = map(int, input().split())
# q = deque()
# used = [0] * 5
# used[s] = 1
# q.append((s, 0))
#
# while q:
#     now, lev = q[0]
#     if now == e:
#         print(lev)
#     for i in range(5):
#         if alist[now][i] == 0: continue
#         if used[i] == 1: continue
#         used[i] = 1
#         q.append((i, lev + 1))


# def recur(idx, total_height):
#     global min_answer
#
#     if total_height >= B:
#         min_answer = min(min_answer, total_height)
#         return
#
#
#     if idx == N:
#         return
#
#     recur(idx + 1, total_height + heights[idx])
#     recur(idx + 1, total_height)
#
#
# T = int(input())
# for tc in range(1, T + 1):
#     N, B = map(int, input().split())
#     heights = list(map(int, input().split()))
#     # min_answer = 1e8    # 나올 수 있는 최대 범위 ( 정답이 보장된 경우 )
#     min_answer = 10000 * N    # 나올 수 없다면 최댓값의
#
#     recur(0, 0)
#     print(f'#{tc} {min_answer-B}')

# def get_sum(tar):
#     sum_v = 0
#     for i in range(N):
#         if tar & 0x1:
#             sum_v += heights[i]
#         tar >>= 1
#     return sum_v
#
# T = int(input())
# for tc in range(1, T + 1):
#     N, B = map(int, input().split())
#     heights = list(map(int, input().split()))
#     min_diff = float('inf')
#
#     for tar in range(1, 1 << N):
#         total = get_sum(tar)
#         if total >= B:
#             diff = total - B
#             min_diff = min(min_diff, diff)
#     print(f'#{tc} {min_diff}')



# def recur(month, sum_v):
#     global result
#
#     if month > 12:
#         result = min(result, sum_v)
#         return
#
#     # 1일 이용권
#     recur(month + 1, sum_v + (plan[month] * cost[0]))
#
#     # 1달 이용권
#     recur(month + 1, sum_v + cost[1])
#
#     # 3달 이용권
#     recur(month + 3, sum_v + cost[2])
#
#     # 1년 이용권
#     recur(month + 12, sum_v + cost[3])
#
# T = int(input())
# for tc in range(1, T + 1):
#     cost = list(map(int, input().split()))
#     plan = [0] + list(map(int, input().split()))
#     result = float('inf')
#     recur(1, 0)
#     print(f'#{tc} {result}')


# dy = [-1, 1, 0, 0]
# dx = [0, 0, 1, -1]
#
# def dfs(y, x, sum_v):
#
#     if len(sum_v) == 7:
#         result.add(sum_v)
#         return
#     for i in range(4):
#         ny = y + dy[i]
#         nx = x + dx[i]
#         if 0 > ny or  ny >= 4 or 0 > nx or nx >= 4: continue
#         dfs(ny, nx, sum_v + arr[ny][nx])
#
#
# T = int(input())
# for tc in range(1, T + 1):
#     arr = [input().split() for _ in range(4)]
#     result = set()
#
#     for y in range(4):
#         for x in range(4):
#             dfs(y, x, arr[y][x])
#
#     print(f'#{tc} {len(result)}')



# dy = [-1, 1, 0, 0]
# dx = [0, 0, 1, -1]
#
# def dfs(y, x):
#     global cnt
#
#
#
# T = int(input())
# for tc in range(1, T + 1):
#     N = int(input())
#     arr = [input().split() for _ in range(N)]
#     for y in range(N):
#         for x in range(N):
#             cnt = 1
#             dfs(y, x)
#             ny, nx = y + dy[i], x + dx[i]
#             cnt += 1
#             dfs(ny, nx)



# 순열 문제
# 최소거리 구하기
# 한번씩 다 가보고 최소거리 갱신 (완전탐색)
import sys
sys.stdin = open("input.txt", "r")

'''def get_meter(path):
    sum_v = 0
    sum_v += apples[path[0]][0] + apples[path[0]][1] # 0에서 출발
    for i in range(N - 1):
        dx = abs(apples[path[i]][0] - apples[path[i + 1]][0])
        dy = abs(apples[path[i]][1] - apples[path[i + 1]][1])

        sum_v += dx
        sum_v += dy

    sum_v += apples[path[N - 1]][0] + apples[path[N - 1]][1]  # 다시 출발지로 돌아감

    return sum_v

def dfs(lev):
    global min_v

    if lev == N:
        value = get_meter(path)
        if min_v > value:
            min_v = value
        return

    for i in range(N):
        if used[i] == 1: continue
        path.append(i)
        used[i] = 1
        dfs(lev + 1)
        path.pop()
        used[i] = 0



T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    apples = []
    path = []
    used = [0] * (N + 1)
    min_v = float('inf')

    # 사과 담기
    for _ in range(N):
        x, y = map(int, input().split())
        apples.append([x, y])

    dfs(0)

    print(f'#{tc} {min_v}')'''

'''
def dfs(lev, sum_v):
    global min_v

    if sum_v >= min_v:
        return

    if lev == N:
        last = apples[path[-1]]
        return_dist = last[0] + last[1]  # back to (0, 0)
        total = sum_v + return_dist
        min_v = min(min_v, total)
        return

    for i in range(N):
        if used[i]: continue

        if lev == 0:
            # distance from (0,0) to first apple
            dist = apples[i][0] + apples[i][1]
        else:
            prev = apples[path[-1]]
            curr = apples[i]
            dist = abs(prev[0] - curr[0]) + abs(prev[1] - curr[1])

        path.append(i)
        used[i] = 1
        dfs(lev + 1, sum_v + dist)
        path.pop()
        used[i] = 0


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    apples = []
    path = []
    used = [0] * N
    min_v = float('inf')

    for _ in range(N):
        x, y = map(int, input().split())
        apples.append([x, y])

    dfs(0, 0)

    print(f'#{tc} {min_v}')
'''

from collections import deque


# N, M = map(int, input().split())
# arr = [[] for _ in range(11)]
# for i in range(M):
#     A, B = map(int, input().split())
#     arr[A].append(B)
#     arr[B].append(A)
# R, K = map(int, input().split())
#
#
# q = deque()
# q.append((R, 0))
# used = [0] * (M + 1)
# used[R] = 1
# cnt = 0
# while q:
#     now, lev = q[0]
#     q.popleft()
#     if now == B:
#         if lev <= 3:
#             cnt += 1
#
#     for i in range(10):
#         if arr[now][i] == 0: continue
#         if used[i] == 1: continue
#         used[i] = 1
#         q.append((i, lev + 1))


#
# boss = [i for i in range(10)]
#
# def Find(n):
#     if boss[n] == n: return n
#
#     result = Find(boss[n])      # 재귀호출
#     return result
#
# def Union(t1, t2):
#     a = Find(t1) # t1의 보스는 a다
#     b = Find(t2) # t2의 보스는 b다
#
#     if a == b: return # 이미 보스가 같으면 : 탈락(return)
#     boss[b] = a     # b의 보스가 a다
# Union(6, 7)
# Union(5, 6)
# Union(1, 2)

# a, b = map(int, input().split())
# # 논리 : 보스가 같으면 같은 그룹
#
# if Find(a) == Find(b): print('O')
# else: print('X')


boss = [i for i in range(8)]
def Find(n):
    if boss[n] == n:  # 가리키는 보스가 자기 자신이면
        return n  # 최종 보스다

    result = Find(boss[n])  # 재귀호출
    return result


def Union(t1, t2):
    a = Find(t1)
    b = Find(t2)

    if a == b: return
    boss[b] = a

Union(6, 7)
Union(5, 6)
Union(1, 2)

a, b = map(int, input().split())
if Find(a) == Find(b):
    print('O')
else: print('X')


boss = [i for i in range(10)]

def Find(n):
    if boss[n] == n: return n

    result = Find(boss[n])
    return result

def Union(t1, t2):
    a = Find(t1)
    b = Find(t2)

    if a == b: return
    boss[b] = a
N = int(input())
for i in range()
Union(4, 2)
Union(1, 4)
Union(1, 3)
Union(9, 5)



if Find(a) == Find(b):
    print('O')
else: print('X')