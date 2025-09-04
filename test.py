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

arr = ['O', 'X']
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