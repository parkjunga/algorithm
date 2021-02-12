'''
# 큐
정수를 저장하는 큐를 구현한 다음, 입력으로 주어지는 명령을 처리하는 프로그램을 작성하시오.

명령은 총 여섯 가지이다.

push X: 정수 X를 큐에 넣는 연산이다.
pop: 큐에서 가장 앞에 있는 정수를 빼고, 그 수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
size: 큐에 들어있는 정수의 개수를 출력한다.
empty: 큐가 비어있으면 1, 아니면 0을 출력한다.
front: 큐의 가장 앞에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
back: 큐의 가장 뒤에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.

입력
첫째 줄에 주어지는 명령의 수 N (1 ≤ N ≤ 10,000)이 주어진다. 둘째 줄부터 N개의 줄에는 명령이 하나씩 주어진다.
주어지는 정수는 1보다 크거나 같고, 100,000보다 작거나 같다. 문제에 나와있지 않은 명령이 주어지는 경우는 없다.

'''

from sys import stdin

n = int(stdin.readline())

'''
0. 명령어는 n만큼 입력할 수 있따.
1. 명령어와 값을 입력한다.
2. 명령어의 해당하는 행동을 실행한다.
'''
arr = []

test= [1,2,3]
print(len(test), "<-사이즈")
for i in range(n):
    # 명령어 * 값
    m = stdin.readline().split()
    if m[0] == 'push':
        arr.insert(0,m[1])
        print('어레이상태',arr)
    elif m[0] == 'pop':
        if len(arr) != 0:
            print(arr.pop())
        else:
            print(-1)
    elif m[0] == 'size':
        print(len(arr))
    elif m[0] == 'empty':
        if len(arr) == 0:
            print(1)
        else:
            print(0)
    elif m[0] == 'back':
        if len(arr) == 0:
            print(-1)
        else:
            print(arr[0])
    elif m[0] == 'front':
        if len(arr) == 0:
            print(-1)
        else:
            print("프론트",arr[len(arr)-1])

