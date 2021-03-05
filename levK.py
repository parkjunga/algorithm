def solution(array, commands):
    answer = []
    for i in range(len(commands)):
        commands[i] # 분류된
        new_arr = array[commands[i][0]-1:commands[i][1]]
        new_arr.sort()
        answer.append(new_arr[commands[i][2]-1])
    return answer

array = [1, 5, 2, 6, 3, 7, 4]
commands = 	[[2, 5, 3], [4, 4, 1], [1, 7, 3]]

ans = solution(array,commands)
print(ans)

'''
풀이 
1. 반복문을 통해 이중배열을 푼다.
2. 배열내 또 다른 배열에있는 슬라이싱을 통해 데이터에 접근한다.
3. 또 다른 배열을 새로운 배열에 담는다.
4. 정렬한다.
5. 그 배열내에 슬라이싱을 통해 인덱스값으로 찾는다.
'''