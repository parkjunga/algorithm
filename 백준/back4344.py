c = int(input())
l = []
for i in range(c):
    l.append(list(map(int,input().split())))

sum2 = []
countzip = []

for i in range(len(l)):
    sumsic = sum(l[i])-l[i][0]
    sumsic = sumsic/l[i][0]
    sum2.append(sumsic)
    count = 0
    for j in range(1,len(l[i])):
        if sumsic < l[i][j]:
            count += 1
    countzip.append(format(round(count/l[i][0] * 100,3),'.3f'))

for i in range(len(countzip)):
    print(countzip[i]+'%')