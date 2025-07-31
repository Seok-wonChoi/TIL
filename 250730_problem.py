
# 2
def longest_string(str_list):
    max_cnt = 0
    temp = ""
    for string in str_list:
        cnt = 0
        for char in string:
            cnt += 1
        if cnt > max_cnt:
            max_cnt = cnt
            temp = string
    return temp

##########################################
# 8

def reverse_string(s):
    if len(s) <= 1:
        return s
    
    return reverse_string(s[1:]) + s[0]