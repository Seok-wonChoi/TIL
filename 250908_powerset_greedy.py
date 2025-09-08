#############################################
# recursion

# # # 3명의 친구 부분집합 찾기
# # arr = ['O', 'X']
# # name = ['MIN', 'CO', 'TIM']
# # path = []
# #
# #
# # def recur(cnt):
# #     # 종료조건 (3명을 모두 고려)
# #     if cnt == 3:
# #         print(*path)
# #         return
# #
# #     # 재귀호출 파트
# #     # - 부분집합에 포함 되는 경우 (O를 추가)
# #     path.append(arr[0])
# #     recur(cnt + 1)
# #     path.pop()
# #
# #     # - 포함되지 않는 경우 (X를 추가)
# #     path.append(arr[1])
# #     recur(cnt + 1)
# #     path.pop()
# #
# #
# # recur(0)  # 0명을 고려한 상태로 시작
#
# ----------------- 실제 많이 보게 될 코드

'''name = ['MIN', 'CO', 'TIM']


def recur(cnt, subset):
    if cnt == 3:
        print(*subset)
        return

    # 부분집합에 포함 시키는 경우
    recur(cnt + 1, subset + [name[cnt]])
    # 포함 시키지 않는 경우
    recur(cnt + 1, subset)


recur(0, [])'''



##################################################################
# binary
'''arr = [1, 2, 3, 4]

# i: 0~2^n == i번째 부분집합
for i in range(1 << len(arr)):
    for idx in range(len(arr)):
        if i & (1 << idx):
            print(arr[idx], end=" ")
    print()

# 검사하고자 하는 비트를 오른쪽으로 하나씩 shift 하면서 체크하는 코드
def get_sub(tar):
    print(f'target = {tar}', end=' / ')
    for i in range(len(arr)):
        # 0x1 로 표기한 이유 (사실 1, 0b1, 0b0001, True 다 된다)
        # - 비트 연산임을 명시하는 권장 방법
        if tar & 0x1:  # 가장 우측 비트를 체크
            print(arr[i], end=' ')
        tar >>= 1


for target in range(1 << len(arr)):
    get_sub(target)
    print()'''


#################################
# Baby-gin


'''used = [0] * 6
path = []
is_babygin = 0
def is_baby_gin():
    cnt = 0

    a, b, c = path[0], path[1], path[2]
    if a == b == c: cnt += 1
    elif (a) == (b -1) == (c -2) : cnt += 1

    a, b, c = path[3], path[4], path[5]
    if a == b == c: cnt += 1
    elif (a) == (b -1) == (c -2) : cnt += 1

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
else: print('No')'''


############################
# 최소합

'''def dfs(y, x, sum_v):
    global min_sum

    if y == N-1 and x == N-1:
        min_sum = min(min_sum, sum_v)
        return
        # 가지치기
    if min_sum <= sum_v: return


    if x < N -1:
        dfs(y, x + 1, sum_v + arr[y][x+1])
    if y < N -1:
        dfs(y + 1, x, sum_v + arr[y+1][x])

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    min_sum = float('inf')

    dfs(0, 0, arr[0][0])
    print(f'#{tc} {min_sum}')'''


##############################################
# 전자카트

'''
def dfs(lev, sum_v):
    global min_v


    # 마지막 구역에서 사무실로 돌아오는 비용
    if lev == N -1:
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