
def solution(num_list):
    answer = 0
    add = 0
    mx = 1
    for i in range(len(num_list)):
        add += num_list[i]
        mx *= num_list[i]
    if add * add > mx:
        answer = 1
    else:
        answer = 0
    return answer


solution(num_list=[3, 4, 5, 2, 1])