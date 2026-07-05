"""
1. Prime Security Code Checker

A high-security research lab uses numeric passcodes to unlock restricted doors. To improve security,
 only prime numbers are accepted because they have exactly two factors and are harder to predict using common patterns.

When an employee enters a code, the system must verify whether the number is prime. If yes, access is granted; otherwise, access is denied.

Write a program to check whether the entered number is Prime or Not Prime.

Input:
29

Output:
Prime Number
"""

"""
n= int(input("n ="))
flag =0

if n<=1 :
    print("not a prime number")
else :
    i=2
    while i<n :
       if n%i ==0 :
          flag = 1
          break
       i = i+1

if flag == 0:
     print("Prime Number")
else :
     print("Not a Prime Number")
"""

"""
2. Next Prime ID Generator

A multinational company auto-generates employee IDs in numeric sequence.
 Due to internal policy, only prime numbered IDs are assigned to new premium employees.

The HR manager enters the current last issued ID, and the software must search forward to find the next available prime number ID.

Write a program to find the first prime number after n.

Input:
14

Output:
Next Prime = 17
"""
"""
n= int(input("n ="))

for i in range(n+1 , n+100):
   flag =0

   for j in range (2 , i):
     if i % j ==0 :
          flag =1
          break
   if flag ==0 :
        print(i)
        break
"""
# other method of Ques 2

"""
n= int(input("n ="))
num = n+1

while True :
     flag =0
     for i in range(2, num):
            if num% i==0 :
               flag = 1
               break

     if flag == 0:
          print("next prime ", num)
          break
     num= num +1
"""
"""
3. Composite Number Detector

A product testing company labels batch numbers as risky if they have more than two factors. Such numbers are known as composite numbers and indicate repeated grouping patterns.

The quality control officer enters a batch number, and the software checks whether it is Composite or Not.

Write a program to check whether a number is Composite or Not.

Input:
12

Output:
Composite Number
"""
"""
n= int(input("n ="))
flag =0

if n<1 :
    print("not a composite number")

else :
      for i in range(2, n-1):
           if n% i ==0 :
               flag =1
               break
           i= i+1
if flag !=0 :
       print("is a composite number")
else:
       print("not a composite number")

"""


"""
4. Prime Security Code Checker – Advanced

A high-security lab accepts only prime numbered access codes.

When a user enters a number, the software must:

- Check whether number is prime
- If prime, print next immediate prime number
- If not prime, print previous immediate prime number

Write a program using loops only.

Input:
29

Output:
Prime Number
Next Prime = 31
"""

n= int(input("n ="))
num= n+1
flag =0

if n<1 :
     print("Not prime")


if n>1 :
  num= num+1
  while True :
    flag =0
    for i in range(2,num):
         if num%i ==0 :
             flag =1
             break
    if flag ==0 :
       print("next prime num",num)
       break
    num = num+1
else:

  num = num-1
  while n>1:
    flag =0
    for i in range(2,num):
          if num%i ==0 :
              flag =1
              break
    if flag ==0 :
       print("previuos prime num", num)
       break
    num= num-1
          


"""
5. Next Prime ID Generator – Smart Version

A company gives prime numbered employee IDs to premium staff.

Manager enters current ID.
System must:

- Find next prime number after current ID
- Find difference between current ID and next prime

Write a program using loops.

Input:
20

Output:
Next Prime ID = 23
Gap = 3
"""
"""
n= int(input("n ="))
temp =n
num= n+1


while True :
    flag =0
    for i in range(2, num):
          if num%i == 0:
              flag =1
              break
    if flag==0:
      print("next prime",num)
      break
    num = num+1

diff = num-temp
print("difference is ", diff)
       
"""

"""
6. Composite Number Detector – Risk Version

A product company marks composite numbers as risky.

User enters a number.
System must:

- Check Composite or Not
- Count total factors
- Print smallest factor other than 1

Input:
12

Output:
Composite Number
Factors Count = 6
Smallest Factor = 2
"""
"""

n= int(input("n ="))
temp =n
flag =0
count =0
l=len(str(n))
smallest =0
if n<1 :
    print("not a composite number")

else :
      for i in range(2, n-1):
           if n% i ==0 :
               flag =1
               break
           i= i+1
if flag !=0 :
       print("is a composite number")
else:
       print("not a composite number")  

flag =0
for i in range(1,n+1):
      
      if n%i ==0 :
         count = count+1
print("factor count", count)

for i in range(2,l):
       r= temp%10
       if smallest>= r:
          smallest =r
          if smallest==0:
             break
       temp =temp//10
print("smallest", smallest)
   
"""   
"""
7.
 Prime Sum Lucky Number

A lottery app checks if sum of digits is prime.

Write a program to:

- Find sum of digits
- If prime print Lucky Number
- Else Normal Number

Input:
4528

Output:
Sum = 19
Lucky Number
"""
"""
n= int(input("n ="))
sum =0
for i in range(len(str(n))):
     r= n%10
     sum=sum+r
     n= n//10
print(sum)

if n<=1:
   print("not prime ")
else:

    flag =0
    for i in range(2,sum):
      if sum%i ==0 :
        flag =1
        break

if flag ==0 :
     print("its a prime number and lucky number")
else :
     print("not prime and normal number")
"""
"""
8. Largest Smallest Sum Prime Checker

A number analyzer finds largest and smallest digit.

Write a program to:

- Find largest digit
- Find smallest digit
- Find sum of both
- Check whether sum is Prime or Not

Input:
57294

Output:
Largest = 9
Smallest = 2
Sum = 11
Prime
"""
"""
n= int(input("n ="))
l = len(str(n))
largest =1
smallest =9
sum=0

for i in range(l):
     r= n%10
     if largest<= r :
        largest= largest +r
        largest =r
     else :
        if smallest >=r :
           smallest = smallest +r
           smallest =r
     n=n//10
print("largest ", largest)
print("smallest ", smallest)

sum= largest + smallest
print("sum" , sum)

flag =0

if sum<1 :
    print("not a prime number")
else :
    i=2
    while i<sum :
       if sum%i ==0 :
          flag = 1
          break
       i = i+1

    if flag == 0:
        print("Prime Number")
    else :
        print("Not a Prime Number")

"""
"""
9.Even Odd Difference Prime System

A smart scanner counts even and odd digits.

Write a program to:

- Count even digits
- Count odd digits
- Find difference
- Check whether difference is Prime or Not

Input:
123456

Output:
Even Count = 3
Odd Count = 3
Difference =0
not prime
"""
"""
import math
m = int(input("num : "))
ecount = 0 ; ocount = 0
while m > 0 :
    d = m%10
    m = m//10
    if d%2 == 0 :
        ecount += 1
    else :
        ocount += 1

print("even count =",ecount)
print("odd count =",ocount)

n = abs(ecount - ocount)
print("Difference =",n)

num = math.sqrt(n)
if n <= 1:
    print("not prime")
else :
    i = 2 
    while i <= int(num) :
        if n%i == 0 :
            print("not prime")
            break
        i+=1
    else :
        print("prime")

"""
"""

10.Zero Count Prime Scanner

A banking system checks account numbers.

Write a program to:

- Count zero digits
- Find sum of digits
- Add zero count and sum
- Multiply by smallest digit
- Check whether final result is Prime or Not

Input:
908406

Output:
Zero Count = 2
Sum = 27
Smallest Digit = 0
Final Result = 0
Not Prime
"""
"""
n= int(input("n ="))
l = len(str(n))
m= n
count= 0
smallest =9
sum =0

for i in range(l):
      r = n%10
      sum = sum+r
      if r==0 :
         count = count+1
      n=  n//10
print("count",count)
print("sum",sum)

add= count+ sum
print("add",add)


for i in range(l) :
     r = m%10
     if smallest >=r :
         smallest =r
     m=  m//10
print("smallest" ,smallest)
mutiply = sum * smallest
print("mutiply", mutiply)

flag =0

if sum<1 :
    print("not a prime number")
else :
    i=2
    while i<sum :
       if sum%i ==0 :
          flag = 1
          break
       i = i+1

    if flag == 0:
        print("Prime Number")
    else :
        print("Not a Prime Number")

 """   



















   


























           


