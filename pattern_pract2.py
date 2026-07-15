"""
1.
*****
"""

"""
n=int(input("n ="))
for i in range(1,n+1):
    print("*", end ="")
"""

"""
2.
*
*
*
*
*
"""

"""
n=int(input("n ="))
for i in range(1,n+1):
    print("*")
"""

"""
3.
*****
 ****
  ***
   **
    *
"""
"""
n= int(input("n ="))
i=1
while i <=n :
       print()
       space =1
       while space<=i :
           print(" ",end= "")  
           space +=1
       star=n 
       while star>=i :
           print("*",end ="")
           star-=1
       i+=1
"""
"""
4.
 ************
  **********
   ********
    ******
     ****
      **
"""
"""
n= int(input("n ="))
i=1
while i <=n :
       print()
       space =1
       while space<=i :
           print(" ",end= "")  
           space +=1
       star=n 
       while star>=i :
           print("*",end ="*")
           star-=1
       i+=1
"""
"""
5.
12345
12345
12345
12345
12345
"""
"""
n= int(input("n ="))
i=1
while i<=n :
     print()
     j=1
     while j<=5 :
        print(j, end =" ")
        j+=1
     i+=1
"""
"""
6.
11111
22222
33333
44444
55555
"""
"""
n= int(input("n ="))
i=1
while i <=n :
      print()
      j=1
      while j<=n :
         print(i, end="")
         j=j+1
      
      i+=1
"""
"""
7.
1
00
111
0000
11111
"""
"""
n= int(input("n ="))
i=1
while i<=n :
    print()
    j=1
    while j<=i:
       if i%2 ==0:
          print("0",end="")
       else:
          print("1",end="")
       j+=1
    i+=1
"""

"""
8.
*****
*****
*****
*****
*****
"""
"""
n= int(input("n ="))
i=1
while i<=n:
       print()
       j=1
       while j<=n :
          print("*",end="")
          j+=1
       i+=1
"""

"""
9.

*
**
***
****
*****
"""
"""
n= int(input("n ="))

i=1
while i<=n :
     print()
     j=1
     while j<=i:
        print("*",end ="")
        j+=1
     i+=1
"""

"""
10.

1
12
123
1234
12345
"""
"""
n= int(input("n ="))
i=1
while i<=n :
      print()
      j=1
      while j<=i:
         print(j, end="")
         j+=1
      i+=1
"""

"""
11.

1
22
333
4444
55555
"""
"""
n= int(input("n ="))
i=1
while i<=n :
      print()
      j=1
      while j<=i:
         print(i, end="")
         j+=1
      i+=1
"""

"""
12.

1
01
101
0101
10101
"""
"""
n= int(input("n ="))
i=1
while i<= n:
     print()
     j=i
     while j>=1:
            if j%2 ==0 :
               print("0", end="")
            else :
               print("1", end="")
            j-=1
     i+=1
"""

"""
13.

A
AB
ABC
ABCD
ABCDE
"""
"""
n= int(input("n ="))
c=65
i=1
while i <=n:
      print()
      j=1
      while j<=i :
          print(chr(c+j-1),end="")
          
          j+=1
      i+=1
"""
"""
14.

a
ab
abc
abcd
abcde
"""

"""
n= int(input("n ="))
c=97
i=1
while i<=n :
       print()
       j=1
       while j<=i :
          print(chr(c+j-1),end ="")
          j+=1
       i+=1
"""

"""
15.

1
23
456
78910
"""
"""
n= int(input("n ="))
i=1
k=1
while i<=n :
      print()
      j=1
      while j<=i :
          print(k, end="")
          k+=1
          j+=1
      i+=1
"""

"""
16.

A
BB
CCC
DDDD
EEEEE
"""
'''
n=int(input("n ="))
c=65
i=1
while i<=n:
    print()
    j=1
    while j<=i :
       x= chr(c)
       print(x,end ="")
       j+=1
    c+=1
       
    i+=1
'''

'''
17.

a
bc
def
ghij
klmno
'''

'''
n=int(input("n ="))

k=97
i=1
while i<=n :
     print()
     j=1
     while j<=i :
        c=chr(k)
        print(c, end="")
        k+=1
        j+=1
     i+=1
'''

'''
18.

*
##
***
####
*****
'''

'''
n= int(input("n="))
i=1
while i<=n :
    print()
    j=1
    while j<=i :
        if i%2 ==0 :
            print("#", end="")
        else :
            print("*", end="")
        j+=1
    i+=1
'''

'''
19.

1
10
101
1010
10101
'''

'''
n= int(input("n ="))
i=1
while i<=n :
     print()
     j=1
     while j<=i :
         if j%2 ==0:
             print("0", end="")
         else :
             print("1", end="")
         j+=1
     i+=1
'''

'''
20.

*
* *
*   *
*     *
* * * * *
'''
'''
n= int(input("n ="))
i=1
while i<=n :
      print()
      j=1
      while j<=i :
         if i==1 or i==n or j==1 or j==i :
              print("*",end="")
         else:
              print(" ",end ="")
         j+=1
      i+=1
'''
'''
21.

* 
 *
  *
   *
    *
'''
'''
n= int(input("n ="))
i=1
while i<=n :
      print()
      j=1
      while j<=i :
         if j%i==0:
             print("*", end="")
         else:
             print(" ",end ="")
         j+=1
      i+=1
'''
'''
22.

1
12
1 3
1  4
12345
'''
'''
n= int(input("n="))
i=1
while i <= n:
      print()
      j=1
      while j<=i :
         if i==1 or i==n or j==1 or j==i:
             print(j, end="")
         else :
             print(" ", end="")
         j+=1
      i+=1
'''

'''
23.

1
22
3 3
4  4
55555
'''
'''
n= int(input("n ="))
i=1
while i <= n:
      print()
      j=1
      while j<=i :
         if i==1 or i==n or j==i or j==1 or j==n:
             print(i, end="")
         else :
             print(" ", end="")
         j+=1
      i+=1
'''

'''
24.

A
AB
A C
A  D
ABCDE
'''
'''
n= int(input("n ="))
c=65
i=1
while i<=n:
     print()
     j=1
     while j<=i :
        if i==1 or i==n or j==i or j==1 or j==n:
            print(chr(c+j-1),end="")
        else:
            print(" ", end="") 
            
        j+=1 
     i+=1
'''
'''
25.

a
bc
d f
g  j
klmno
'''
'''
n= int(input("n="))

ch=97
for i in range(1, n+1):
    for j in range(1, i+1):
      if i==n or j==1 or j==i :
           print(chr(ch), end="")
      else:
           print(" ", end="")
      ch+=1
    print()


'''
'''
26.

5
54
543
5432
54321
'''
'''
n=int(input("n ="))
i=0
while i<=n :
     print()
     j=n
     while j>=n-i:
        print(j, end="")
        j-=1
     i+=1
'''
'''
27.
*
*#
*#*
*#*#
*#*#*
'''
'''
n= int(input("n="))
i=1
while i<=n :
     print()
     j=1
     while j<=i :
        if j%2==0 :
           print("#", end="")
        else:
           print("*", end="")
        j+=1
     i+=1
'''
'''
28.
*
**
*@*
*@@*
* * * * *
'''
'''
n= int(input("n ="))
i=1
while i <= n:
      print()
      j=1
      while j<=i :
         if i==1 or i==n or j==i or j==1 or j==n:
             print("*", end="")
         else :
             print("@", end="")
         j+=1
      i+=1
'''
'''
29.

1
10
1 1
1  0
10101
'''
'''
n= int(input("n ="))
i=1
while i<=n:
     print()
     j=1
     while j<=i :
         if i==1 or i==n or j==i or j==1 or j==n:
             if j%2==0:
               print("0", end="")
             else:
               print("1", end="")
         else:
               print(" ",end="")
         j+=1
     i+=1
'''
'''
30.
1
123
12345
1234567
123456789
'''
'''
n= int(input("n ="))
i=1
while i<= n:
     print()
     j=1
     while j<= i*2-1:
         print(j, end="")
         j+=1
     i+=1
'''
'''
31.
1
222
33333
4444444
555555555
'''

'''
n= int(input("n ="))
i=1
while i<=n :
    print()
    j=1
    while j<=i*2-1:
        print(i, end ="")
        j+=1
    i+=1
'''

'''
32.

***** 
**** 
***
**
* 
'''
'''
n= int(input("n ="))
i= 1
while i<=n :
      print()
      j=n
      while j>=i:
          print("*", end="")
          j-=1
      i+=1
'''
'''
33.

12345
1234
123
12
1
'''
'''
n= int(input("n ="))
i=1
while i<= n:
    print()
    j=1
    while j<=n-i+1 :
       print(j, end="")
       j+=1
    i+=1
'''
'''
35.
55555
4444
333
22
1
'''
'''
n= int(input("n ="))
i=n
while i>=1 :
    print()
    j=i
    while j>=1:
      print(i, end="")
      j-=1
    i-=1
'''
'''
36.
ABCDE
ABCD
ABC
AB
A
'''
'''
n= int(input("n ="))

i=0
while i<=n:
      print()
      j=1
      ch= 65
      while j<=n-i:
         print(chr(ch), end="")
         ch+=1
         j+=1
      i+=1
'''
'''
37.
EEEEE
DDDD
CCC
BB
A

'''
'''
n= int(input("n ="))
i=n
while i>=1:
    print()
    j=i
    ch= chr(64+i)
    while j>=1 :
       print(ch, end="")
       j-=1
    i-=1
'''

'''
38.

*****
*  *
* *
**
*

'''
'''
n= int(input("n ="))
i=n
while i>=1 :
      print()
      j=1
      while j<=i:
          if i==n or i==j or j==1:
              print("*" , end="")
          else:
              print(" ", end ="")
          j+=1
      i-=1

'''
'''
39.
ABCDE
A  D
A C
AB
A
'''
'''
n= int(input("n="))
i=n
while i>=1 :
       print()
       j=1
       ch= 65
       while j<=i :
            if i==n or i==j or j==1 :
                print(chr(ch), end="")
            else :
                print(" ", end ="")
            ch+=1
            j+=1
       i-=1
'''
'''
40.
*****
####
***
##
*
'''
'''
n= int(input("n ="))
i=n
while i>=1 :
     print()
     j=1 
     while j<=i :
        if i%2 !=0 :
             print("*", end="")
        else :
             print("#", end ="")
        j+=1
     i-=1
'''

'''
41.
55555
4  4
3 3
22
1
'''
'''
n= int(input("n="))
i=n
while i>=1 :
      print()
      j=i
      while j>=1 :
          if i==n or j==i or j==1 or j==n :
              print(i, end="")
          else:
              print(" ", end="")
          j-=1

      i-=1
'''
'''
42.
123456
54321
1234
321
12
1
'''
'''
n=int(input("n ="))
i=n
while i>=1 :
     print()
     if i%2 ==0 :
        j=1
        while j<=i :
           print(j, end="")
           j+=1
     else:
         j=i
         while j>=1 :
             print(j , end="")
             j-=1
     i-=1
    
'''
'''
43.
*
**
****
*******
***********
'''
'''
n= int(input("n="))
inc=1
star =1

i=1
while i<=n :
      print()
      j=1
      while j <=star:
          print("*" , end="")
          j+=1
      star = star+inc
      inc = inc+1
      i+=1
          
'''

'''
44.
A
BCD
EFGHI
JKLMNOP
'''

'''
n= int(input("n ="))

ch=(65)
i=1
while i<= n:
     print()
     j=1
     while j<i+i:
         print(chr(ch), end="")
         j+=1
         ch+=1
         
     i=i+1
'''
'''
45.
54321
5432
543
54
5
'''

'''
n= int(input("n ="))
i=1
while i<=n :
       print()
       j=n
       while j>=i :
          print(j , end="")
          j-=1
           
       
       i+=1
'''
'''
46.

     1
    12
   123
  1234
 12345

'''
'''
n= int(input("n ="))
i= 1
while i<=n :
        print()
        j=n
        while j>=i:
            print(" ", end="")
            j-=1
        k=1
        while k<=i:
             print(k, end="")
             k=k+1
        i+=1
'''
'''
47.
     1
    22
   333
  4444
 55555
'''
'''
n= int(input("n ="))

i= 1
while i<=n :
        print()
        j=n
        while j>=i:
            print(" ", end="")
            j-=1
        k=1
        while k<=i :
            print(i , end="")
            k=k+1
            
        i+=1
'''

'''
48.

     5
    44
   333
  2222
 11111
'''
'''
n= int(input("n ="))
i=n
while i>=1 :
        print()
        j=i
        while j>1:
            print(" ", end="")
            j-=1
        k=1
        while k<=n-i+1:
            print(i, end="")
            k+=1
      
        i-=1
       
'''

'''
49.
     A
    AB
   ABC
  ABCD
 ABCDE
'''
'''
n= int(input("n ="))
i=1
while i<= n:
      print()
      j=n
      while j>=i :
          print(" ", end="")
          j-=1
      k=1
      ch=65
      while k<=i :
           print(chr(ch), end="")
           ch+=1
           k+=1
      i+=1

'''
'''
50.

     1
    11
   1*1
  1**1
 11111
'''
'''
n= int(input("n ="))
i=1
while i<= n:
      print()
      j=n
      while j>=i :
           print(" ", end="")
           j-=1
      k=1
      while k<=i :
          if i==1 or k==i or i==n or k==1 :
               print("1", end="")
          else :
               print("*" , end="")
          k+=1
     
      i+=1
'''
'''
51.
     A
    AB
   A_C
  A__D
 ABCDE
'''
'''
n= int(input("n ="))
i=1
while i<=n :
      print()
      j=n
      while j>=i:
         print(" ", end="")
         j-=1
      k=1
      ch=65
      while k<=i:
          if k==1 or k==i or i==n or k==1:
              print(chr(ch), end="")
          else:
              print("_", end="")
          ch= ch+1
          k+=1
         
      i+=1
'''
'''
52.
     1
    10
   101
  1010
 10101
'''
'''
n= int(input("n ="))
i=1
while i<=n :
      print()
      j=n
      while j>=i:
         print(" ", end="")
         j-=1
      k=1
      while k<=i :
          if k%2==0:
               print("0", end="")
          else:
               print("1", end="")
          k+=1
      i+=1
'''
'''
53.
 12345
  1234
   123
    12
     1
'''
'''
n= int(input("n="))
i=1
while i<=n:
     print()
     j=1
     while j<=i:
        print(" ", end="")
        j+=1
     k=1
     while k<=n-i+1:
         print(k, end="")
         k+=1
     i+=1

'''
'''
54.
 55555
  4444
   333
    22
     1
'''
'''
n= int(input("n="))
i=n
while i>=1:
     print()
     j=n
     while j>i:
         print(" ", end="")
         j-=1
     
     m=1
     while m<=i:
         print(i, end="")
         
         m=m+1
     i-=1

'''
'''
55.

 12345
  1__4
   1_3
    12
     1
'''
'''
n= int(input("n ="))
i=1
while i<=n:
     print()
     j=1
     while j<=i:
         print(" ", end="")
         j+=1
     k=1
     while k<=n-i+1:
        if i==1  or k==1  or k==n-i+1:
            print(k, end="")
        else:
            print("_", end="")
        k=k+1
     i+=1           

'''
'''
56.
 55555
  4__4
   3_3
    22
     1
'''
'''
n= int(input("n ="))
i=n
while i>=1:
      print()
      j=n
      while j>=i :
        print(" ", end="")
        j-=1
      k=1
      while k<=i:
         if i==n or k==1  or k==i or i==1:
           print(i, end="")
         else:
           print("_", end="")
         k+=1
      i-=1
'''
'''
57.
 ABCDE
  A__D
   A_C
    AB
     A
'''
'''
n= int(input("n ="))
i=n
while i>=1:
      print()
      j=n
      while j>=i :
        print(" ", end="")
        j-=1
      k=1
      ch=65
      while k<=i:
         if i==n or k==1  or k==i or i==1:
           print(chr(ch), end="")
         else:
           print("_", end="")
         ch+=1
         k+=1
      i-=1
'''
'''
58.
 ABCDE
  ABCD
   ABC
    AB
     A
'''
'''
n= int(input("n ="))
i=n
while i>=1 :
      print()
      j=n
      while j>=i :
         print(" ", end="")
         j-=1
      k=1
      ch=65
      while k<=i:
           print(chr(ch), end="")
           ch+=1
           k+=1
      i-=1
'''
'''
59.
 11111
  2222
   333
    44
     5
'''
'''
n= int(input("n="))
i=1
while i<= n:
      print()
      j=1
      while j<=i :
         print(" ", end="")
         j+=1
      k=1
      while k<=n-i+1:
         print(i, end="")
         k+=1
      i+=1
'''
'''
60.
         * 
       * *
     * * *
   * * * *
 * * * * *

'''
'''
n= int(input("n ="))
i=1
while i<=n :
     print()
     j=1
     while j<=n-i+1:
          print(" ", end="")
          j+=1
     k=1
     while k<=i:
          print("*", end="")
          k+=1
     i+=1

'''
'''
61.
     1
    1 2
   1 2 3
  1 2 3 4
 1 2 3 4 5

'''
'''
n= int(input("n ="))
i=1
while i<=n:
     print()
     j=1
     while j<=n-i+1:
          print(" ", end="")
          j+=1
     k=1
     while k<=i:
         print(k, end=" ")
         k+=1
     i+=1
'''

'''
62.
     A 
    A B    
   A B C
  A B C D
 A B C D E  
'''
'''
n= int(input("n="))
i=1
while i<=n:
     print()
     j=1
     while j<=n-i+1:
          print(" ", end="")
          j+=1
     k=1
     ch=65
     while k<=i:
         print(chr(ch), end=" ")
         ch+=1
         k+=1
     i+=1
'''
'''
63.
     X 
    X X 
   X__X
  X____X
 X X X X X

'''
'''
n= int(input("n="))
i=1
while i<=n:
     print()
     j=1
     while j<=n-i+1:
          print(" ", end="")
          j+=1
     k=1
     while k<=i:
         if i==1 or k==1 or k==i or k==n or i==n:
            print("X", end=" ")
         else:
            print("_", end=" ")
         k+=1
     i+=1
'''
'''
64.

     *
    ***
   *****
  *******
 *********
'''
'''
n= int(input("n="))

i=1
while i<=n :
      print()
      j=n
      while j>=i:
          print(" ", end=" ")
          j-=1
      k=1
      while k<= i*2-1 :
          print("*", end=" ")
          k=k+1
          
          
          
      i+=1
'''
'''
65.
     1
    123
   12345
  1234567
 123456789
'''
'''
n= int(input("n ="))
i=1
while i<=n :
       print()
       j=n
       while j>=i :
         print(" ", end=" ")
         j-=1
       k=1
       while k<=i*2-1:
           print(k, end=" ")
           k+=1
       i+=1
'''
'''
66.
     A
    ABC
   ABCDE
  ABCDEEF
 ABCDEFGHI
'''
'''
n= int(input("n ="))
i=1
while i<=n :
       print()
       j=n
       while j>=i :
         print(" ", end=" ")
         j-=1
       k=1
       ch=65
       while k<=i*2-1:
           print(chr(ch), end=" ")
           k+=1
           ch+=1
       i+=1
'''
'''
67.
     *
    *_*
   *___* 
  *_____* 
 *********
'''
'''
n= int(input("n ="))
i=1
while i <= n:
       print()
       j=n
       while j>= i :
           print(" ", end="")
           j-=1
       k=1
       while k<=i*2-1 :
           if i==1  or k==1 or k==2*i-1 or i==n :
               print("*", end="")
           else:
                print("_", end="")
           k+=1
       i+=1
'''
'''
68.
     1
    1*1
   1***1
  1*****1
 111111111
'''
'''
n= int(input("n ="))
i=1
while i<=n :
       print()
       j=n
       while j>=i :
            print(" ", end='')
            j-=1
       k=1
       while k<=i*2-1:
           if i==1 or i==n or k==1 or k==2*i-1 :
                 print("1" , end="")
           else:
                 print("*", end="")
           k+=1
       i+=1
'''

'''
69.
     1
    1 1
   1 2 1
  1 3 3 1
 1 4 6 4 1
'''
'''
n= int(input("n ="))
i=1
while i<= n:
       print()
       j=n
       while j>= i:
            print(" ", end="")
            j-=1
       k=1
   
       while k<=i :
             if k== i  or k==1 :
                  print("1", end=" ")
             else:
                  print(i-1, end=" ")
             k+=1
       i+=1   
'''
'''
70.
     A
    B_B
   C___C
  D______D
 EEEEEEEEE
'''
'''
n= int(input('n='))
i=1
while i<=n:
      j=n
      while j>i:
         print(" ",end="")
         j=j-1

      k=1
      while k<=2*i-1:
          
          if i==n or k==1  or k==(2*i)-1 :
             print(chr(64+i),end="")
          else:
             print("_",end="")
          k=k+1 
      print()
      i=i+1
'''
'''
71.
     #
    *#* 
   **#** 
  ***#*** 
 ****#****
'''
'''
n= int(input("n ="))
i=1
while i<=n :
        print()
        j=n
        while j>i :
            print(" ",end="")
            j-=1
        k=1
        while k<=2*i-1 :
          if k==i :
            print("#", end="")
          else:
            print("*" , end="")
          k+=1
        i +=1   
'''

'''
72.
*********
 ******* 
  ***** 
   ***
    * 
'''
'''
n= int(input("n ="))
i=n
while i>=1:
      j=1
      while j<=(n-i) :
           print(" ", end="")
           j+=1
      k=1
      while k<=2*i-1:
            print("*" ,end="")
            k+=1
      print()
      i-=1
'''
'''
73.
 * * * * * 
  * * * * 
   * * * 
    * * 
     *
'''
'''
n= int(input("n ="))
i=n
while i>=1:
      print()
      j=1
      while j<= n-i :
            print(" ", end="")
            j+=1
      k=1
      while k<=i:
           print("*", end=" ")
           k+=1
     
      i-=1
'''

'''
74.
 123456789
  1234567
   12345
    123
     1
'''
'''
n= int(input("n ="))
i=n
while i>=1 :
       print()
       j=1
       while j<= n-i :
            print(" ", end="")
            j+=1
       k=1
       while k<=2*i-1:
            print(k, end="")
            k+=1
       i-=1

'''
'''
75.
 A B C D E
  A B C D
   A B C
    A B
     A
'''
'''
n= int(input("n="))
i=1
while i<=n :
      print()
      j=1
      while j<=i :
          print(" ", end="")
          j+=1
      k=1
      ch=65
      while k<=n+1-i:
           print(chr(ch),end=" ")
           ch+=1
           k+=1
      
      i+=1
'''

'''
76.
 5 5 5 5 5
  4 4 4 4
   3 3 3
    2 2
     1
'''
'''
n= int(input("n ="))
i=n
while i>=1 :
     print()
     j=1
     while j<=n-i:
        print(" ", end="")
        j+=1
     k=1
     while k<=i :
        print(i, end=" ")
        k+=1
     i-=1
'''
'''
77.
 123456789
  1     7
   1   5 
    1 3
     1
'''
'''
n= int(input("n ="))
i=n
while i>=1 :
       print()
       j=1
       while j<= n-i :
            print(" ", end="")
            j+=1
       k=1
       while k<=2*i-1:
          if i==n or k==1 or k==2*i-1:
            print(k, end="")
          else:
            print(" ", end="")
          k+=1
       i-=1
'''
'''
78.

 123456789
  1+++++7
   1+++5
    1+3
     1
'''
'''
n= int(input("n ="))
i=n
while i>=1 :
       print()
       j=1
       while j<= n-i :
            print(" ", end="")
            j+=1
       k=1
       while k<=2*i-1:
          if i==n or k==1 or k==2*i-1:
            print(k, end="")
          else:
            print("+", end="")
          k+=1
       i-=1
'''

'''
79.
x
xx
xxx
xxxx
xxx
xx
x
'''
'''
n= int(input("n="))
i=1
while i<=n:
     print()
     j=1
     while  j<=i :
         print("X", end="")
         j+=1 

     i+=1
k=1
while k<=n-1:
     print()
     m=1
     while m<=n-k :
         print("X", end="")
         m+=1
     
     k+=1
'''
'''
80.
1
12
123
1234
123
12
1
'''
'''
n= int(input("n ="))
i=1
while i<=n :
      print()
      j=1
      while j<=i :
          print(j, end="")
          j+=1
      i+=1
k=1
while k<=n-1:
      print()
      m=1
      while m<=n-k:
         print(m, end="")
         m+=1
      
      k+=1
'''
'''
81.
    1
   12
  123
 1234
  123
   12
    1
'''
'''
n= int(input("n ="))
i=1
while i<=n :
      print()
      j=n
      while j>=i:
          print(" ", end="")
          j-=1
      k=1
      while k<=i :
           print(k, end="")
           k+=1
      i+=1
m=1
while m<=n-1 :
       print()

       space= 1
       while space <=m+1:
            print(" ", end="")
            space+=1

       l=1
       while l<=n-m:
           print(l, end="")
           l+=1
       m+=1
'''
'''
82.
1
1 2
1  3
1   4
1  3
1 2
1
'''
'''
n= int(input("n="))
i=1
while i<=n :
       print()
       j=1
       while j<=i:
          if j==1 or i==1 or j==i:
              print(j, end="")
          else:
              print(" ", end="")
          j+=1
       i+=1
k= 1
while k<=n-1:
      print()
      m=1
      while m<=n-k:
          if m==n-k or m==1 :
              print(m, end="")
          else:
              print(" ", end="")
          m+=1
      k+=1
'''
'''
83.
    *
   *_*
  *_*_*
 *_*_*_*
  *_*_*
   *_*
    *  
'''
'''
n= int(input("n ="))
i=1
while i<=n :
       print()
       j=n
       while j>=i:
           print(" ", end="")
           j-=1
       k=1
       while k<=i*2-1:
            if k%2==0:
               print("_", end="")
            else:
               print("*", end="")
            k+=1
  
       i+=1
m=n-1
while m>=1 :
        print()
        g=1
        while g<=n-m+1:
             print(" ", end="")
             g+=1
        s=1
        while s<=m*2-1 :
            if s%2==0 :
                 print("_", end="")
            else:
                 print("*", end='')
            s+=1
        m-=1
'''

'''
84.
    *
   ***
  ***** 
 ******* 
  ***** 
   *** 
    *
'''
'''
n=int(input("n ="))
i=1
while i<=n:
     print()
     j=n
     while j>=i:
         print(" ", end="")
         j-=1
     k=1
     while k<= i*2-1:
          print("*", end="")
          k+=1
        
     i+=1
m=n-1
while m>=1:
       print()
       g=1
       while g<=n-m+1:
          print(" ", end="")
          g+=1
       s=1
       while s<=m*2-1:
           print("*", end="")
           s+=1
       m-=1
'''
'''
85.
    *
   *_* 
  *___* 
 *_____*
  *___* 
   *_*
    *
'''
'''
n= int(input("n ="))
i=1
while i<=n:
      print()
      j=n
      while j>=i:
         print(" ", end="")
         j-=1
      k=1
      while k<=i*2-1:
           if i==1 or k==1 or k==i*2-1:
                print("*", end="")
           else:
                print("_", end="")
           k+=1
      i+=1

m=n-1
while m>=1 :
     print()
     l=1
     while l<=n-m+1:
          print(" ", end="")
          l+=1
     s=1
     while s<=m*2-1:
         if s==1 or m==1 or s== m*2-1:
             print("*", end="")
         else:
             print("_", end="")
         s+=1
     m-=1
'''
'''
86.
     1
    212
   32123
  4321234
 543212345
'''
'''
n= int(input("n ="))
i=1
while i<=n:
    print()
    m=n
    while m>=i:
         print(" ", end="")
         m-=1
    j=i
    while j>=1:
       print(j, end='')
       j-=1
    k=2
    while k<=i:
       print(k, end='')
       k+=1

    i+=1
'''
'''
87.
*        *
**      **
***    ***
****  ****
***** *****
'''
'''
n= int(input("n ="))
i=1
while i<=5 :
      print()
      j=1
      while j<=i :
          print("*", end="")
          j+=1
      k=1
      while k<=(n-i)*2:
           print(" ", end="")
           k+=1
      m=1
      while m<=i :
           print("*", end='')
           m+=1
      i+=1

'''
'''
88.
***** *****
****  ****
***    ***
**      **
*        *
'''
'''
n= int(input("n ="))
i=1
while i<=n:
     print()
     j=n
     while j>=i:
        print("*", end='')
        j-=1
     k=1
     while k<=i*2-1:
         print(" ", end="")
         k+=1
     m=1
     while m<=n+1-i :
         print("*", end='')
         m+=1
     i+=1

'''
'''
89.
      1               
     101            
    10101         
   1010101           
  101010101  
 10101010101
'''
'''
n= int(input("n ="))
i=1
while i<= n:
      print()
      j=n
      while j>=i:
         print(" ", end='')
         j-=1
      k=1
      while k<=i*2-1 :
           if k%2==0 :
               print("0",end="")
           else:
               print("1", end='')
           k+=1

      i+=1
'''
'''
90.

*         *
  *      *
   *   *
     *
    *  *
  *      *
*          *

'''























