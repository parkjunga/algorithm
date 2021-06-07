def solution(s):
    answer = ''

    # 1차적으로 -비교일경우가 있어 그냥 비교는 안된다.
    # map을 이용해 문자열을 int형 리스트로 변환한다
    s = list(map(int,s.split()))
    new_s = [min(s),max(s)]

    # int형이기때문에 문자열 조합을 위해 다시한번 변환한다.
    answer = ' '.join(map(str,new_s))
    return answer

a = "-1 -2 -3 -4"
print(solution(a))