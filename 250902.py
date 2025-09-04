# ##################
# # 5176. [파이썬 S/W 문제해결 기본] 8일차 - 이진탐색
# import sys
# sys.stdin = open("input.txt", "r")
#
# def bulid_bt(node):
#     global num
#     if node <= N:
#         bulid_bt(node * 2)
#         tree[node] = num
#         num += 1
#         bulid_bt(node * 2 + 1)
#
# T = int(input())
# for tc in range(1, T + 1):
#     N = int(input())
#     tree = [0] * (N + 1)
#     num = 1
#
#     bulid_bt(1)
#
#     print(f'#{tc} {tree[1]} {tree[N // 2]}')




##########
# 24022. DFS 준비 1 그래프와 인접행렬
# arr = [[0] * 4 for _ in range(4)]
#
# arr[1][0] = 'B'
# arr[2][0] = 'B'
# arr[3][0] = 'B'
# arr[2][1] = 'T'
# arr[3][1] = 'T'
# N = int(input())
# for i in range(4):
#     if arr[N][i] == 0: continue
#     else: print(arr[N][i])

#############################
# DFS 준비 2 그래프와 인접행렬

# arr = [[0] * 5 for _ in range(5)]
#
# arr[0][1] = 2
# arr[1][2] = 3
# arr[1][3] = 4
# arr[2][1] = 2
# arr[4][1] = 2
# N = int(input())
# for j in range(5):
#     if arr[N-1][j] != 0:
#         print(arr[N-1][j])


####################################
# DFS 준비 3 2차원 배열 append

# arr = []
# arr.append([3,5])
# arr.append([])
# print(arr)


#######################################
# DFS 준비 4 2차원 배열 인덱싱

# arr = [[], [], [], []]
# arr[0] = [4, 2, 5, 1, 1]
# arr[1] = [3, 4, 2]
# arr[2] = []
# arr[3] = [1, 1, 2, 3]
# for i in range(len(arr)):
#     print(arr[i])

#######################################
# DFS 준비 5 배열 역순 출력
# arr = [[], [], []]
# arr[0] = ['A', 'B', 'T']
# arr[2] = ['R', 'S']
# for i in range(len(arr)):
#     arr[i] = arr[i][::-1]
#     print(*arr[i], sep='')

#######################################
# DFS 준비 6 그래프와 인접리스트

# arr = [[], [], [], []]
#
#
# arr[1] = [0, 3]
# arr[2] = [1, 3]
#
# print(arr)

######################################
# 24765. 키 순서

T = int(input())
for tc in range(1, T + 1):
    n = int(input())        # n : 학생 수
    m = int(input())        # m : 키를 비교한 횟수
    cnt_student = 0         # 키가 몇 번째인지 알 수 있는 학생 수
    for i in range(1, m + 1):
        a, b = map(int,input().split())     # a < b000



    print(f'#{tc} {cnt_student}')