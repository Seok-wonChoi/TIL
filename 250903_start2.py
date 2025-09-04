
'''
# 10진수를 2진수를 변환
def decimal_to_binary(n):
    bin_num = ''

    if n == 0:
        return '0'
    # 0보다 클 때까지 2로 나누면서 나머지를 정답에 추가
    while n > 0:
        remain = n % 2
        bin_num = str(remain) + bin_num
        n = n // 2
    return bin_num

print(decimal_to_binary(4))
'''

'''
# 10진수를 16진수로 변환
def decimal_to_hexadecimal(n):
    hex_digits = '0123456789ABCDEF'
    hex_num = ''

    if n == 0:
        return 0

    while n > 0:
        remain = n % 16
        hex_num = hex_digits[remain] + hex_num
    return hex_num

print(decimal_to_hexadecimal())
'''


'''# 2진수를 10진수로 변환
def binary_to_decimal(bin_str):
    dec_num = 0
    pow = 0
    for digit in reversed(bin_str):
        if digit == '1':
            dec_num += 2 ** pow
        pow += 1

    return dec_num
print(binary_to_decimal('11'))'''


'''secret_code = 1004

print(7070 ^ secret_code)
print(7070 ^ secret_code ^ secret_code)'''

#----------------------------

# print(1 << 1, bin(1 << 1))
# print(1 << 4, bin(1 << 4))

'''num = 2
for _ in range(5):
    print(num, end=' ')
    num <<= 1'''

# 1. 부분집합의 수
'''arr = [1, 2, 3, 4]'''
'''print(f'부분 집합의 수 : {1 << len(arr)}')'''

# 2. 전체 부분집합의 수
# for i in range(1 << len(arr)):
#     for idx in range(len(arr)):
#         # i : 부분집합 번호 (각 자리의 포함 여부)
#         # (1 << idx) : 0b1, 0b10, 0b100, 0b1000
#         if i & (1 << idx):
#             print(arr[idx], end=' ')
#     print()


# 3. 합이 10인 부분집합만 구해라

'''arr = [1, 2, 3, 4, 5, 6]
for i in range(1 << len(arr)):
    subset = []
    total = 0

    for idx in range(len(arr)):
        if i & (1 << idx):
            subset.append(arr[idx])
            total += arr[idx]
    if total == 10:
        print(f'합이 10인 부분집합 : {subset}')'''


# 비트 연산은 어떻게 활용할까?

