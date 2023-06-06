import re


def solution(s):
    new_s = re.findall("-?\d+", s)
    new_s = list(map(int,new_s))
    mx = max(new_s)
    mi = min(new_s)
    mx = str(mx)
    mi = str(mi)
    answer = mi + " "+ mx
    return answer


s = "-1 -2 -3 -4"
print(solution(s))