# 작성 날짜: 22.10.02

# 문제 설명
# 정수 num이 짝수일 경우 "Even"을 반환하고 홀수인 경우 "Odd"를 반환하는 함수, solution을 완성해주세요.

# 제한 조건
# num은 int 범위의 정수입니다.
# 0은 짝수입니다.

def solution(num):
    answer = ''
    if num % 2 == 0:
        answer = 'Even'
    else:
        answer = 'Odd'
    return answer

print(solution(3))  # Odd
print(solution(4))  # Even

# 위 문제의 저작권은 2022 프로그래머스 (주)그렙 에 있습니다.