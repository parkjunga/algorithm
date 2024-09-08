def solution(my_string, index_list):
    answer = ''
    for i in range(len(index_list)):
        answer += my_string[index_list[i]]
    return answer


my_string = "cvsgiorszzzmrpaqpe"
index_list = [16, 6, 5, 3, 12, 14, 11, 11, 17, 12, 7]
solution(my_string,index_list)