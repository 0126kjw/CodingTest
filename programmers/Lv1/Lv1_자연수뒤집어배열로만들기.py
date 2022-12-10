# 작성 날짜: 22.10.08

# 문제 설명

# 자연수 n을 뒤집어 각 자리 숫자를 원소로 가지는 배열 형태로 리턴해주세요. 예를들어 n이 12345이면 [5,4,3,2,1]을 리턴합니다.

# 제한 조건
# n은 10,000,000,000이하인 자연수입니다.

def solution(n):
    answer = list(map(int, str(n)))
    answer.reverse()
    return answer

print(solution(12345))

# 위 문제의 저작권은 2022 프로그래머스 (주)그렙 에 있습니다.