'''
오늘 날짜를 의미하는 문자열 today,
약관의 유효기간을 담은 1차원 문자열 배열 terms와 수집된 개인정보의 정보를 담은 1차원 문자열 배열 privacies가 매개변수로 주어집니다.
이때 파기해야 할 개인정보의 번호를 오름차순으로 1차원 정수 배열에 담아 return 하도록 solution 함수를 완성해 주세요.
'''
import datetime
from dateutil.relativedelta import relativedelta
def solution(today, terms, privacies):
    answer = []
    return answer


today = "2020.01.01"
terms = ["Z 3", "D 5"]
privacie = ["2019.01.01 D", "2019.11.15 Z", "2019.08.02 D", "2019.07.01 D", "2018.12.28 Z"]

test = []
for i in range(len(privacie)):
    test.append(privacie[i].split(' '))

tmp = []
for j in range(len(terms)):
    tmp.append(terms[j].split(' '))
new_day = ''

for i in range(len(tmp)):
    print(tmp[i][0])
    for j in range(len(test)):
        custom_date = test[j][0].split('.')
        if test[j][1] == tmp[i][0]:
            day = list(map(int,test[j][0].split('.')))
            if day[1] + int(tmp[i][1]) > 12:
                new_year = relativedelta(years=day[0]+1)
                month = day[1] + int(tmp[i][1])
                print(new_year,month-day[1], day[2] - 3)
