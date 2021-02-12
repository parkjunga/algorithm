'''
binary search (이진탐색) : 반드시 정렬된 상태에서 시작해야한다. 로그실행시간을 보장한다.
용어 설명
target : 찾고자하는 값
data: 오름차순으로 정렬된 list
start: data의 처음 값 인덱스
end: data의 마지막 값 인덱스
mid: start,end의 중간 인덱스
바이너리 서치
data중 target을 검색하여 index 값을 return 한다.
없으면 None을 return
'''
# target = 찾고자하는값, data: list값
def binary_search(target,data):
    data.sort() # 먼저 정렬부터한다 (오름차순)
    start = 0
    end = len(data) - 1
    while start <= end: # 반복문은 인덱스 끝까지돌린다.
        mid = (start+end) // 2 # 중간 인덱스
        if data[mid] == target:
            return mid # 함수를 끝낸다.
        elif data[mid] < target: #중간값 보다 타겟값이 크면 시작인덱스를 mid보다 뒤로
            start = mid + 1
        else:
            end = mid - 1
    return None

li = [i ** 2 for i in range(11)]
print(li)
target = 9
idx = binary_search(target,li)

if idx:
    print(li[idx])
else:
    print('찾는게없다.')