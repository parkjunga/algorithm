a, b = map(int, input().strip().split(' '))
list = [ a * '*' for _ in range(b)]
for i in range(len(list)):
    print(list[i])
print()