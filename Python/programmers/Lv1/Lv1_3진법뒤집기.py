# 작성 날짜: 23.02.15

# 문제 설명
# 자연수 n이 매개변수로 주어집니다. n을 3진법 상에서 앞뒤로 뒤집은 후, 이를 다시 10진법으로 표현한 수를 return 하도록 solution 함수를 완성해주세요.

# 제한사항
# n은 1 이상 100,000,000 이하인 자연수입니다.

def solution(n):
    answer=''
    while n:
        answer+=str(n%3)
        n=n//3
    return int(answer,3)

print(solution(45))  # 7
print(solution(125))  # 229

# 위 문제의 저작권은 2023 프로그래머스 (주)그렙 에 있습니다.