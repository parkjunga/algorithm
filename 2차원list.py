'''

3 4

0 1 0 0

0 0 0 0

0 0 1 0


'''

n,m = map(int,input().split())

# 1
'''
1차원 리스트인 mylist에 행의 개수(n)만큼의 0으로 채운다.
그 다음 n번의 for문ㅇㄹ 통해 한줄씩 input값으로 받아서 mylist에 채워진 0을 입력값으로 대체한다.
이 때도 map함수 통해 int형 변환
'''
mylist = [0 for _ in range(n)]
for i in range(n):
    mylist[i] = list(map(int,input().split()))
print(mylist)

# 2
'''
비어있는 1차원 리스트인 mylist를 선언하고,
n번의 for문을 통해 한 줄씩 입력받은 값을 mylist에 추가 해준다.
append를 통해 한 줄씩 순서대로 리스트의 원소로 추가
'''

mylist = []
for i in range(n):
    mylist.append(list(map(int,input().split())))

# 3
'''
선언,초기화,입력받고, 원소추가를 한 줄로 축약한것 
앞서 나왔던 list comprehension을 통해 mylist의 원소가 될 형식을 list(map(int,(input().split())) 로지정하고 
n번 만큼 실행한다. 
'''
mylist = [list(map(int,input().split())) for _ in range(n)]

