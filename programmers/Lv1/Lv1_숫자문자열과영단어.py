# 작성 날짜: 23.02.24

# 문제 설명
# 네오와 프로도가 숫자놀이를 하고 있습니다. 네오가 프로도에게 숫자를 건넬 때 일부 자릿수를 영단어로 바꾼 카드를 건네주면 프로도는 원래 숫자를 찾는 게임입니다.

# 다음은 숫자의 일부 자릿수를 영단어로 바꾸는 예시입니다.
# 1478 → "one4seveneight"
# 234567 → "23four5six7"
# 10203 → "1zerotwozero3"
# 이렇게 숫자의 일부 자릿수가 영단어로 바뀌어졌거나, 혹은 바뀌지 않고 그대로인 문자열 s가 매개변수로 주어집니다. s가 의미하는 원래 숫자를 return 하도록 solution 함수를 완성해주세요.

# 나의 풀이
def solution(s):
    num = {"zero":"0", "one":"1", "two":"2", "three":"3", "four":"4", "five":"5", "six":"6", "seven":"7", "eight":"8", "nine":"9"}
    answer = []
    result = []
    for i in list(s):
        if i.isdigit():
            result.append(i)
        else:
            answer.append(i)
            if ''.join(answer) in num.keys():
                result.append(num[''.join(answer)])
                answer = []
    return int(''.join(result))

print(solution("one4seveneight"))  # 1478
print(solution("23four5six7"))  # 234567

# 다른 사람의 풀이
num_dic = {"zero":"0", "one":"1", "two":"2", "three":"3", "four":"4", "five":"5", "six":"6", "seven":"7", "eight":"8", "nine":"9"}

def solution(s):
    answer = s
    for key, value in num_dic.items():
        answer = answer.replace(key, value)
    return int(answer)


# 위 문제의 저작권은 2023 프로그래머스 (주)그렙 에 있습니다.