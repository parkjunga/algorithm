##"w" : n이 1 커집니다.
## "s" : n이 1 작아집니다.
## "d" : n이 10 커집니다.
## "a" : n이 10 작아집니다.
def solution(n, control):
    answer = n
    for i in range(len(control)):
        if control[i] == "w" :
            answer += 1
        elif control[i] == 's':
            answer -= 1
        elif control[i] == 'd':
            answer += 10
        else:
            answer -= 10
    return answer

n = 0
control = "wsdawsdassw"
print(solution(n,control))