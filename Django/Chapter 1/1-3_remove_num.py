# 문자열에서 숫자를 제거하기
def solution(input_str):
    answer = ''
    num_list = list('0123456789')
    for c in input_str:
        if c not in num_list:
            answer += c
    return answer

input_str1 = 'H123e4l5l6o7, P8y9t1h2o3n.4'
input_str2 = '25B7789y12e0525, 45P12y5t69h366o17n23.4'

print(solution(input_str1), solution(input_str2))