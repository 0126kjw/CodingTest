# 작성 날짜: 22.10.09

# 문제 설명

# 자연수 n이 매개변수로 주어집니다. n을 x로 나눈 나머지가 1이 되도록 하는 가장 작은 자연수 x를 return 하도록 solution 함수를 완성해주세요. 답이 항상 존재함은 증명될 수 있습니다.

# 제한사항

# 3 ≤ n ≤ 1,000,000

def solution(n):
    count = 0
    while True:
        count = count + 1
        if n % count == 1:
            break
    return count


# 위 문제의 저작권은 2022 프로그래머스 (주)그렙 에 있습니다.