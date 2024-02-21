#PROGRAM- 1-find duplicate element hacker
'''
n=int(input())
x=list(map(int,input().split()))[:n]
for i in range(n):
    if x[i] in x[i+1:]:
        print(x[i])
        break
        '''
'''
n=int(input())
x=list(map(int,input().split()))[:n]
x.sort()
for i in range(n-1):
    if x[i] == x[i+1]:
        print(x[i])
        break
'''

'''
n=int(input())
x=list(map(int,input().split()))[:n]
for i in x:
    c=x.count(i)
    if c>1:
        print(i)
        break
'''

#PROGRAM- 2 print unique elements of array
'''
n=int(input())
x=list(map(int,input().split()))[:n]
for i in x:
    c=x.count(i)
    if c==1:
        print(i,end=" ")
    '''

'''n=int(input())
x=list(map(int,input().split()))[:n]
unique=[]
for i in x:
    if x.count(i)==1:
        unique.append(i)
print(int(unique))
'''
        

#PROGRAM- 3

        
'''t=int(input())
t1=[]
t2=[]
factors=[]
for i in range(t):
    n=int(input())
    for j in range(1,n+1):
        if n%j==0:
            factors.append(j)
    for j in factors:
        if j%2==0:
            t1.append(j)
        else:
            t2.append(j)
    if len(t1)==len(t2):
        print(1)
    else:
        print(0)


t=int(input())
for i in range(t):
    n=int(input())
    t1=0
    t2=0
    for j in range(1,n+1):
        if n%j==0:
            if j%2==0:
                t1=t1+1
            else:
                t2=t2+1
    if t1==t2:
        print(1)
    else:
        print(0)


t=int(input())
def ans(n):
    
def test(t):
    if t>0:
        n=int(input())
        print(ans(n))
    else:
        return
    test(t-1)
test(t)





        '''


#PROGRAM- 4-cost of grociees codechef
'''t=int(input())
for i in range(t):
    n,x=map(int,input().split())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    c=0
    for j in range(n):
        if a[j]>=x:
            c=c+b[j]
        else:
            continue
    print(c)
'''

#check whether it its prime
'''n=int(input())
lst=[]
for i in range(1,n+1):
    if n%i==0:
        lst.append(i)
count=len(lst)
if count==2:
    print('yes')
else:
    print('no')
'''

#running comapare codechef
'''t=int(input())
for i in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    count=0
    for j in range(n):
        if a[j]<=b[j]*2 and b[j]<=a[j]*2:
            count=count+1
    print(count)


'''

#PROGRAM- 5 - perfect number
#all even perfect numbers in a given range
'''n,x=map(int,input().split())
lst=[]
flst=[]
for i in range(n,x+1):
    if i%2==0:
        lst.append(i)
sum=0
for i in range(1,len(lst)):
    for j in range(1,lst[i]):
        if lst[i]%j==0:
            sum+=j
    if sum == lst[i]:
        print(lst[i])
    sum=0
    '''
x=int(input())
for i in range(2,x+1,2):
    for j in range(1,i):
        if i%j==0:
            sum+=j
    if sum == i:
        print(i)
    sum=0