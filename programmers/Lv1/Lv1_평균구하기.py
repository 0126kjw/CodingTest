# 작성 날짜: 22.10.02

# 문제 설명
# 정수를 담고 있는 배열 arr의 평균값을 return하는 함수, solution을 완성해보세요.

# 제한사항
# arr은 길이 1 이상, 100 이하인 배열입니다.
# arr의 원소는 -10,000 이상 10,000 이하인 정수입니다.

def solution(arr):
    answer = sum(arr) / len(arr)
    return answer

print(solution([1,2,3,4]))  # 2.5
print(solution([5,5]))  # 5.0

# 위 문제의 저작권은 2022 프로그래머스 (주)그렙 에 있습니다.