"""
1
12
123
1234
12345
"""
"""
n = int(input("n ="))
i = 1 
while i<=n :
     print()
     j= 1
     while j<= i :
         print(j , end ="")
         j= j+1
     i= i+1
"""
"""
54321
4321
321
21
1

"""
"""
n= int(input("n ="))
i=n
while i>=1 :
     print()
     j = i
     while j>=1 :
         print(j, end= "")
         j= j-1
     i=i-1
"""

"""
12345
2345
345
45
5

"""
"""
n= int(input("n ="))
i =1 
while i<=n :
     print()
     j =i
     while j<=n :
         print(j, end= "")
         j=j+1
     i= i+1

"""

"""
54321
5432
543
54
5

"""
"""
n= int(input("n ="))
i=1
while i<=n :
     print()
     j=n
     while j>=i :
          print(j, end ="")
          j=j-1
     i=i+1

"""
"""
1
22
333
4444
55555
"""
"""
n= int(input("n ="))
i=1
while i <=n :
      print()
      j=1
      while j<=i :
            print(i, end="")
            j=j+1
      i=i+1
"""

"""
1
**
123
****
12345
"""
"""
n= int(input("n="))
i=1
while i <=n :
      print()
      j=1
      while j<=i :
         if i%2 ==0 :
            print("*", end ="")
         else:
            print(j, end="")
         j=j+1
      i=i+1
"""

"""
1
1*
1*3*
1*3*5
"""
"""
n= int(input("n ="))
i=1
while i<=n :
      print()
      j=1
      while j<=i:
         if j%2 ==0 :
            print("*", end="")
         else:
            print(j, end ="")
         j =j+1
      i=i+1
"""

"""
1
2 3
4 5 6
7 8 9 10
11 12 13 14 15
"""
n = int(input("n ="))
i =1
k=1
while i<=n :
      print()
      j= 1
      while j<=i :
         print(k, end ="")
         k=k+1
         j=j+1
      i= i+1


"""

1**********1
12********21
123******321
1234****4321
12345**54321
123456654321

"""
"""
n= int(input("n ="))
i=1
while i<=n :
     print()
     inc =1
     while inc <= i :
           print(inc ,end= "")
           inc =inc+1
     
     s=1
     while s< (n-i)*2:
          print("*", end="") 
          s= s+1
     
     dec=i
     while dec >= 1:
           print(dec , end ="")
           dec= dec-1

     i=i+1
"""