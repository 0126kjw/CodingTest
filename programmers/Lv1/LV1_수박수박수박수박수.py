# 작성 날짜: 22.11.10

# 문제 설명
# 길이가 n이고, "수박수박수박수...."와 같은 패턴을 유지하는 문자열을 리턴하는 함수, solution을 완성하세요. 예를들어 n이 4이면 "수박수박"을 리턴하고 3이라면 "수박수"를 리턴하면 됩니다.

# 제한 조건
# n은 길이 10,000이하인 자연수입니다.

def solution(n):
    text = ['수','박']
    answer = []
    for i in range(n):
        if i % 2 == 0:
            answer.append(text[0])
        else:
            answer.append(text[1])
    return ''.join(answer)

print(solution(3))  # '수박수'
print(solution(4))  # '수박수박'


# 위 문제의 저작권은 2022 프로그래머스 (주)그렙 에 있습니다.