

def soultion(A,B):
    answer = 0
    AA = sorted(A)
    BB = sorted(B,reverse=True)
    for i in range(len(A)):
        answer += (AA[i] * BB[i])
    return answer


A = [1, 4, 2]
B = [5, 4, 4]

soultion(A,B)
