arr = [2, 1, 4, 4, 2, 2, 1]

dat = [0] * 5
idx = 0

for i in range(len(arr)):
    idx = arr[i]
    dat[idx] += 1

for i in range(len(dat)):
    if dat[i] > 0: print(f'{i} : {dat[i]}')

