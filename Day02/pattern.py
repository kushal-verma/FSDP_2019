def pat(n):
    for i in range(0,n):
        print('*'*i)
    for i in range(n,0,-1):
        print('*'*i)
n=int(input("Enter a number>"))
print(n)
pat(n)
 