# 작성 날짜: 23.02.07

# 문제 설명
# 두 수를 입력받아 두 수의 최대공약수와 최소공배수를 반환하는 함수, solution을 완성해 보세요. 배열의 맨 앞에 최대공약수, 그다음 최소공배수를 넣어 반환하면 됩니다. 예를 들어 두 수 3, 12의 최대공약수는 3, 최소공배수는 12이므로 solution(3, 12)는 [3, 12]를 반환해야 합니다.

# 제한 사항
# 두 수는 1이상 1000000이하의 자연수입니다.

def solution(n, m):
    answer = []
    for i in range(min(n, m), 0, -1):
        if n%i==0 and m%i==0:
            answer.append(i)
            break
    for i in range(max(n, m), n*m+1):
        if i%n==0 and i%m==0:
            answer.append(i)
            break
    return answer

print(solution(3, 12))  # [3, 12]
print(solution(2, 5))  # [1, 10]

# 다른 사람의 풀이(유클리드 호제법)
def gcdlcm(a, b):
    c, d = max(a, b), min(a, b)
    t = 1
    while t > 0:
        t = c % d
        c, d = d, t
    answer = [c, int(a*b/c)]

    return answer

# 위 문제의 저작권은 2023 프로그래머스 (주)그렙 에 있습니다.