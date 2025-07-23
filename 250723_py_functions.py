# 3. map 함수, split()메서드
# map함수를 쓰는 목적 : 정수로 변환



# 4. 정수 여러개를 입력받아 리스트에 할당
# arr = list(map(int,input().split()))
# print(*arr)


# 5. 심화 2차원 리스트를 입력받기 (D3 난이도)
#  3x3 행렬
# 반드시 중첩 반복문
# --->리스트 컴프리헨션

# result = []
# for i in range(3): # 3행
#     arr = list(map(int,input().split()))
#     result.append(arr) # 행 추가, 행 추가, 행 추가

# print(result)

# result = []
# result = [list(map(int,input().split())) for i in range(3)]
# print(result)

#def num_reverse(x):
#     x = str(x)
#     result = x[::-1]

#     return result
# a = 12345
# rvs_result = num_reverse(a)
# print(rvs_result)


#sort()와 sorted()의 차이
arr = [1, 2, 3, 4, 5]
#반환 x 원본 변경-> sort()

# map 
map(첫번쨰 인자 == 함수, 두번째 인자)
