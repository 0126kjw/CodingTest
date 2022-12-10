# 작성 날짜: 22.10.13

# 문제 설명
# 0부터 9까지의 숫자 중 일부가 들어있는 정수 배열 numbers가 매개변수로 주어집니다. numbers에서 찾을 수 없는 0부터 9까지의 숫자를 모두 찾아 더한 수를 return 하도록 solution 함수를 완성해주세요.

# 제한사항
# 1 ≤ numbers의 길이 ≤ 9
# 0 ≤ numbers의 모든 원소 ≤ 9
# numbers의 모든 원소는 서로 다릅니다.

def solution(numbers):
    answer = 0
    for i in range(1, 10):
        if i not in numbers:
            answer = answer + i
    return answer

print(solution([1,2,3,4,6,7,8,0]))  # 14
print(solution([5,8,4,0,6,7,9]))  # 6

# 위 문제의 저작권은 2022 프로그래머스 (주)그렙 에 있습니다.