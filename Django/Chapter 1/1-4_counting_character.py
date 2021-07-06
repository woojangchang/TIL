# 문자열 횟수 세기
# aaabbccd > a3b2c2d1
def solution(input_str):
    answer = ''

    str_full_list = list(input_str)
    str_list = sorted(list(set(input_str)))
    for c in str_list:
        n_c = str(str_full_list.count(c))
        answer += (c+n_c)
    return answer

input_str1 = 'aasvvxvvaoopbccwwwxacc'
input_str2 = 'aabbcccd'

print(solution(input_str1), solution(input_str2))
