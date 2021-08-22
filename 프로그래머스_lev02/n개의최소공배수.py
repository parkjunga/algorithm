def solution(arr):
    answer = 1
    max_arr = 1
    for i in range(2,len(arr)+1):
        for j in range(len(arr)):
            if arr[j] % i == 0:
                print(arr[j] // i)

                arr[j] = arr[j] // i
                if max_arr == i:
                    continue
                else:
                    max_arr = i
                break

    print(arr)
    return answer

arr = [2,6,8,14]
#test
print(solution(arr))