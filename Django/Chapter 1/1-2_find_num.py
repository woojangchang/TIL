# 숫자로 구성된 문자열을 받아 없는 숫자 반환
# 012345689 > 7
def solution(input_str):
    num_list = list('0123456789')
    for num in num_list:
        if num not in input_str:
            return num

input_str1 = '012345689'
input_str2 = '942348647892135468'
input_str3 = '0316842134756321021347'

print(solution(input_str1), solution(input_str2), solution(input_str3))
