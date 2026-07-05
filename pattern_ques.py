

"""
1. WAP to find out the sum of all integer between 100 and 200 which are divisible by 9

"""
"""
n, m = map(int,input("n =").split())
i=n
sum=0
while i<= m :
    if i%9==0 :
       sum=sum+ i
    i=i+1
print(sum)

"""
"""
2. WAP to print square, cube , square root of all numbers from 1 to n.
"""
"""
import math
n, m = map(int,input("n =").split())
for i in range(n,m+1):
       x= i**2
       y= i**3
       z= float(math.sqrt(i))
       print("i*i = ", x ,"   " , "i*i*i =", y ," i root", z)
"""
"""
3. WAP to find out leap years between two entered years

"""
    
n, m = map(int,input("n =").split())
count =0
for i in range(n, m+1):
        if i%4 == 0 :
            if i%100 == 0 :
                if  i%400 == 0 :
                     print(i,"->","event scheduled")
                     count+=1
                else :
                     print(i,"no event")  
            else :
                 count +=1 
                 print(i,"->","event scheduled")
        else :
           print(i,"no event")
                        
print("Total leap year :",count)
print("Total events scheduled :",count)


"""
4. 

1
00
111
0000
11111
"""
"""
n= int(input("n ="))
i =1
while i<= n :
      print()
      j = 1
      while j <=i :
         if i%2 ==0 :
            print("0" , end="")
         else :
            print("1", end ="")
         j= j+1
      i= i+1 

"""

"""
5.

A
AB
ABC
ABCD
ABCDE

"""
"""
n= int(input(" n=")) 
i=1 
c=65
while i<= n:
    print()
    j= 1
    while j<= i :
       x= chr(c+j-1)
       print(x , end="") 
       j=j+1
    i=i+1
"""
"""

A
BC
DEF
GHIJ

"""
"""
n = int(input("n ="))
i =1
c= 65
while i<=n :
      print()
      j =1
      while j<=i :
         x= chr(c)
         print(x , end ="")
         c+=1
         j+=1
      i+=1
"""
"""
6.
a
ab
abc
abcd
abcde

"""
"""
n = int(input("n ="))
c= 97
i= 1
while i<=n :
        print()
        j=1
        while j<=i :
           x= chr(c+j-1)
           print(x, end ="")
           j+=1
        i+=1

"""

"""
7.
enter n=6

          *
        * *
      * * *
    * * * *
  * * * * *
"""
"""
n= int(input("n ="))

for i in range(1, n+1):
       print()
       for j in range(n+1,i,-1):
          print(" ", end =" ")
       for k in range(i,0, -1):
          print("*", end=" ")

"""

"""
n= int(input("n ="))
i=1
while i<=n :
      print()
      j= i
      while j<= n-1 :
          print(" ", end ="")
          j+=1
      k=i
      while k>=1 :
          print("*", end="")
          k-=1
      i+=1

"""

"""
8.
enter n=6
654321
 65432
  6543
   654
    65

"""
"""
n= int(input("n ="))
i=1
while i<=n :
    print()
    j=1
    while j<=i :
        print(" ",end="")
        j+=1
    k=n
    while k>=i :
        print(k, end= "")
        k-=1

        
    i+=1
"""

"""
9.
        1
      1 0
    1 0 1
  1 0 1 0
1 0 1 0 1

"""
"""
n= int(input("n="))
i=1
while i<=n:
     print()
     j=n
     while j>=i:
        print(" ", end ="")
        j-=1
     k=1
     while k<=i :
         if k%2 ==0 :
             print("0", end ="")
         else :
             print("1", end="")
         k+=1
     i+=1
"""

"""
10. 
enter num=6
0
01
012
0123
01234
"""
"""
n=int(input("n="))
i=0
while i<=n :
     print()
     j =0
     while j<= i:
          print(j, end ="")
          j+=1
     i+=1
"""
