##########################
#
boss = [i for i in range(0)]
def Find(n):
    if boss[n] == n: return n

    result = Find(boss[n])      # 재귀호출
    return result


############################
# 경로압축

def Find(n):
    if boss[n] == n: return n

    boss[n] = Find(boss[n])
    return boss[n]


'''return Find(boss[n])만 하는 건 경로 압축 아님 → 그냥 루트를 찾기만 하는 버전.

boss[n] = Find(boss[n])를 해야 비로소 경로 압축입니다.'''
##############################################