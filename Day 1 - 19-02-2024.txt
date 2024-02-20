#PROGRAM1 - hello world

#APPROACH 1
for i in range(1000):
    print("Hello World")

#APPROACH 2
i=0
while(i<5):
    print("Hello World")
    i+=1




#PROGRAM 2 - relation
a,b=map(int,input().split())
if a<b:
    print('a < b')
elif a>b:
    print('a > b')
else:
    print('a == b')




#PROGRAM 3 - triangle
a,b,c=map(int,input().split())
if a+b > c and b+c>a and c+a>b:
    print("Yes")
else:
    print("No")




#PROGRAM 4 -divide apples 2
n=int(input())
k=int(input())
while(k>=n):
    k=k-n
print(k)




#PROGRAM 5 -reverse the number

#APPROACH 1
n=int(input())
i=0
if n<0:
    n=n*(-1)
    while(n):
        r=n%10
        i=(i*10)+r
        n=n//10
    print(i*(-1))
elif n>0:
    while(n):
        r=n%10
        i=(i*10)+r
        n=n//10
    print(i)
elif n==0:
    print(n)


#APPROACH 2
n=int(input())
i=0
if n==0:
    print(n)
while(n):
        r=n%10
        i=(i*10)+r
        n=n//10
if  r<0:
    print(i*(-1))
elif r>0:
    print(i)




#PROGRAM 6 -watermelon
n=int(input())
if(n<=3)or (n%2==1):
    print("No")
else:
    print("Yes")





#PROGRAM 7 - fever
t=int(input())
x=0         #no initialization for while loop
while(x<t):    #for i in range(t) #while(t>0)
    n=int(input())
    if n>98:
        print("Yes")
    else:
        print("No")
    x+=1     #t=t-1





#PROGRAM 8 - discount

#APPROACH 1
t=int(input())
for i in range(t):
    x=int(input())
    ans=100-x
    print(ans)


#APPROACH 2
t=int(input())
for i in range(t):
    a,b,c,d=map(int,input().split())
    'x1=a-c'
    'y1=b-d'
    if a-c<b-d:
        print("first")
    elif b-d<a-c:
        print("second")
    else:  # y1==x1
        print("any")




#PROGRAM 9 - chef and candies
t=int(input())
for i in range(t):
    n,x=map(int,input().split())
    if n>x:
        ans=n-x
        if ans%4 ==0:
            print(ans//4)
        else:
            print((ans//4)+1)
        
    else:
        print(0)





#PROGRAM 10 - minimum pizzas

#APPROACH 1
t=int(input())
for i in range(t):
    n,x=map(int,input().split())
    res=n*x
    if res%4 ==0:
        print(res//4)
    else:
        print((res//4)+1)


#APPROACH 2
t=int(input())
for i in range(t):
    n,x=map(int,input().split())
    ts=n*x #total slices
    tp=0 #total pieces
    while(ts>4):
        tp+=1
        ts=ts-4
    if ts==0:
        print(tp)
    else:
        print(tp+1)
