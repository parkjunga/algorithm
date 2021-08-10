def solution(scores):
    answer = ''
    wrap = []
    new_arr = []
    sum = 0
    tmp = 0
    for i in range(len(scores)): # 0번째
        scores[i] = list(map(int,scores[i])) # 타입변환
        for j in range(len(scores)):
            new_arr.append(scores[j][i])
#            print(scores[j][i],scores[i][i],i,j)
        if max(new_arr) == scores[i][i] and len(new_arr) >= 3:
            tmp = scores[i][i]
            new_arr.remove(scores[i][i])
        if min(new_arr) == scores[i][i]:
            tmp = scores[i][i]
            new_arr.remove(scores[i][i])
        sum = 0
        if tmp == max(new_arr) or tmp == min(new_arr): #반례의 경우포함
            new_arr.append(tmp)
#        print(new_arr)
        for t in range(len(new_arr)):
#           print(new_arr[t])
            sum += new_arr[t]
#        print('------------')
#        print(new_arr)
#        print(sum/len(new_arr))
        sum = sum/len(new_arr)
        new_arr = []
        wrap.append(sum)
#    print(wrap)

    for m in range(len(wrap)):
        if wrap[m] >= 90:
            answer += 'A'
        elif 80 <= wrap[m] < 90:
            answer += 'B'
        elif 70 <= wrap[m] < 80:
            answer += 'C'
        elif 50 <= wrap[m] < 70:
            answer += 'D'
        elif wrap[m] < 50:
            answer += 'F'
    return answer


scores = [[0, 0, 30], [0, 0, 20], [0, 0, 20]]
print(solution(scores))