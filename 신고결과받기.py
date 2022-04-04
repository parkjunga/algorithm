def solution(id_list, report, k):
    new_report = list(set(report))
    id_dic = {id: 0 for id in id_list} # 처음 신고당한 횟수를 담음
    new_id_dic = {id: 0 for id in id_list} # 유저별로 처리결과 전송예정인 배열
    nnew_report = [new_report[j].split(' ') for j in range(len(new_report))]

    for i in range(len((nnew_report))):
        id_dic[nnew_report[i][1]] += 1

    for i,v in id_dic.items():
        if v >= k:
            for j in range(len(nnew_report)):
                if i == nnew_report[j][1]:
                    new_id_dic[nnew_report[j][0]] += 1
    answer = list(new_id_dic.values())

    return answer


id_list = ["muzi", "frodo", "apeach", "neo"]
report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
k = 2

print(solution(id_list,report,k))