'''
알파벳공부
'''
a = input()

dic = {}
for i in range(len(a)):
    if a[i].lower() in dic:
        dic[a[i].lower()] += 1
    else:
        dic[a[i]] = 1

mx = max(dic.values())

count = 0
for k,v in dic.items():
    if mx == v:
        count +=1

if count > 1:
    ans = '?'
else:
    ans = max(dic.keys(), key= lambda k : dic[k])
    ans = ans.upper()
print(ans)