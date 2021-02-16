'''
반복문(for, while)

a = range(1,10) # 1부터 10까지 range(시작숫자,끝숫자)

for i in range(10):
    print("hello")




i = 1
while i < 10:
    print(i)
    i += 1 # i = i + 1
'''
# for문
for i in range(10,0,-1): # 0전까지 1씩 감소
    print("for문 = ", i)

# while문
i = 10
while i >= 1: # 1씩 감소
    print("while문 = ",i)
    i -= 1

#무한반복
i = 1
while True:
    print("무한박복 = ",i)
    # 무한반복 멈추게 하기 위해 조건 추가
    if i == 10:
        break
    i += 1

# continue
for i in range(1, 11):
    if i%2 == 0: # i 가 짝수이면 넘긴다.
        continue
    print("컨티뉴 =",i)

# for문 break for else 중간에 break하게 되면 else를 하지 않는다.
for i in range(1, 111):
    print(i)
    if i==5:
        break # 반복문 멈춘다 건너뛰는것 X
else:
    print(11)