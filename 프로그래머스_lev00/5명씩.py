def solution(names):
    answer = []
    for i in range(len(names)):
        if i % 5 == 0 :
            answer.append(names[i])
    return answer


names = ["nami", "ahri", "jayce", "garen", "ivern", "vex", "jinx"]
solution(names)
