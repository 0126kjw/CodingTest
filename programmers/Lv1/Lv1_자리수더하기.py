# 작성 날짜: 22.10.02

# 문제 설명
# 자연수 N이 주어지면, N의 각 자릿수의 합을 구해서 return 하는 solution 함수를 만들어 주세요.
# 예를들어 N = 123이면 1 + 2 + 3 = 6을 return 하면 됩니다.

# 제한사항
# N의 범위 : 100,000,000 이하의 자연수

def solution(n):
    answer = 0
    my_list = list(str(n))
    for i in my_list:
        answer = answer + int(i)
    return answer

print(solution(123))  # 6
print(solution(987))  # 24

# 위 문제의 저작권은 2022 프로그래머스 (주)그렙 에 있습니다.