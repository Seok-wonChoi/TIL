# 증가하는 사탕 수열
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



#############################
# 전봇대

def get_result():
    size = len(arr)
    cnt = 0

    for i in range(size): # 기준이 되는 전봇대
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


