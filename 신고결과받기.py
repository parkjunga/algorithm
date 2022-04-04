def solution(id_list, report, k):
    new_report = list(set(report))
    id_dic = {}
    new_id_dic = {}
    for i in range(len(id_list)):
        id_dic[id_list[i]] = 0
        new_id_dic[id_list[i]] = 0
    nnew_report = []
    for j in range(len(new_report)):
        nnew_report.append(new_report[j].split(' '))

    for i in range(len((nnew_report))):
         id_dic[nnew_report[i][1]] += 1

    for i,v in id_dic.items():
        if v >= k:
            for j in range(len(nnew_report)):
                if i == nnew_report[j][1]:
                    new_id_dic[nnew_report[j][0]] += 1
    answer = list(new_id_dic.values())

    return answer


id_list = ["con", "ryan"]
report = ["ryan con", "ryan con", "ryan con", "ryan con"]
k = 3

print(solution(id_list,report,k))