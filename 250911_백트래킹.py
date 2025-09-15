##########
# 이진 탐색
def binary_search(arr, target):
    global cnt
    start = 0
    end = len(arr) - 1
    flag = 0

    while start <= end: # start와 end가 같아질때까지
        mid = (start + end) // 2
        # 이진 탐색을 통해서 타겟을 찾으면 middle 인덱스 반환
        if arr[mid] == target:
            return True
        # 타겟이 중간값 보다 크면 오른쪽 부분 탐색
        elif arr[mid] < target:
            if flag == 2: break
            flag = 2
            start = mid + 1
        else: # 타겟이 중간값보다 작으면 왼쪽 부분 탐색
            if flag == 1: break
            flag = 1
            end = mid - 1
    # 타겟 못찾으면
    return False
T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    a_list = sorted(list(map(int, input().split())))
    b_list = list(map(int, input().split()))
    cnt = 0
    for i in b_list:
        cnt += binary_search(a_list, i)
    print(f'#{tc} {cnt}')



###################################
# N-QUEEN
used = [0] * 20
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
print(cnt)