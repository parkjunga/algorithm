'''
중첩 반복문(2중 for문)
*
* *
* * *
* * * *
'''

for i in range(5):
    for j in range(i+1): # i = 1 별한개 찍고
        print('*',end=' ')
    print()
'''
* * * *
* * * 
* * 
* 
'''

for i in range(5):
    for j in range(5-i): # 5-0 5 , 5-1 =4 
        print("*",end=' ')
    print()