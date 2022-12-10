# 작성 날짜: 22.11.13

# 문제 설명
# 두 정수 left와 right가 매개변수로 주어집니다. left부터 right까지의 모든 수들 중에서, 약수의 개수가 짝수인 수는 더하고, 약수의 개수가 홀수인 수는 뺀 수를 return 하도록 solution 함수를 완성해주세요.

# 제한사항
# 1 ≤ left ≤ right ≤ 1,000

def solution(left, right):
    answer = 0
    for i in range(left,right+1):
        if int(i**0.5)==i**0.5:
            answer -= i
        else:
            answer += i
    return answer

print(solution(13, 17))  # 43
print(solution(24, 27))  # 52

# 위 문제의 저작권은 2022 프로그래머스 (주)그렙 에 있습니다.