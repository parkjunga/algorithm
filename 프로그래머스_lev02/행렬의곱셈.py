def solution(arr1, arr2):
    answer = [[]]
    for i in range(len(arr1)):
        for j in range(len(arr1[i])):
            print(arr1[i][j] * arr2[i][j])
        print('----')
    return answer

arr1 = [[2, 3, 2], [4, 2, 4], [3, 1, 4]]
arr2 = 	[[5, 4, 3], [2, 4, 1], [3, 1, 1]]
solution(arr1,arr2)