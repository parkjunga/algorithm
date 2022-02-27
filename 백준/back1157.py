'''
알파벳공부
'''
a = input()

dic = {}
for i in range(len(a)):
    if a[i] in dic:
        dic[a[i]] += 1
    else:
        dic[a[i]] = 1

all_value = dic.values()
max = max(all_value)
count = 0
num = []
for k,v in dic.items():
    if v == max:
        num.append(k)

if len(num) >= 2:
    print('?')
else:
    print(num[0])
