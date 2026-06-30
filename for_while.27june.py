"""
1. Product of Odd Numbers up to N

A puzzle game rewards players by multiplying odd numbers up to n.
Write a program using loops to find product of odd numbers.

Input:
5

Output:
15
"""

"""
n = int(input("n = "))
product =1
i= 1
while i<= n :
       i=i+1
       if i%2 ==0:
           continue
      
       else:
           product =product *i
print(product)
"""

"""
2. Count Numbers Divisible by 7 Between Two Numbers

A company filters lucky coupon numbers divisible by 7.
Write a program using loops to count such numbers in range.

Input:
1 30

Output:
Count = 4
"""

"""
n = int(input(" n ="))
count =0
i=1
while i<= n :
       i= i+1
       if i%7 !=0 :
            continue
       else:
           count = count+1
print("count =", count)
"""

"""
3. Display Numbers Ending with 5

A supermarket tracks token numbers ending in 5.
Write a program using loops to display numbers ending with 5 between two numbers.

Input:
10 40

Output:
15 25 35
"""

"""
n1= int(input("n1 ="))
n2 = int(input("n2 ="))

for i in range(n1, n2+1  ):
      r= i % 10
      if r!= 5:
          continue
      print(i, end=" ")
"""

"""
4. Strong Number Checker

A digital lock opens only for strong numbers.

A strong number is a number whose sum of factorial of digits equals the number.

Example:
145 = 1! + 4! + 5!
"""
"""
"""
"""
5. Harshad Number Checker

A number scanner is installed in a research laboratory where thousands of numeric access codes are tested every day. To identify mathematically balanced codes, the system checks whether the entered number qualifies as a Harshad number. Numbers passing this test are considered valid for the next stage of processing.

A Harshad number is a number that is exactly divisible by the sum of its digits.

Example:
18 = 1 + 8 = 9 and 18 / 9 = 2

Write a program using loops to check whether the entered number is a Harshad number.

Input:
18

Output:
Harshad Number
"""
"""
n= int(input("n ="))
sum=0
temp =n
for i in range(n):
       r= n%10
       sum= sum + r
       n =n//10
if temp % sum ==0 :
     print("Harshad Number")
else:
     print("not a harshad number")
"""

"""
6. Automorphic Number Checker

A digital security company designs smart lockers that open only for special self-matching numeric codes. When a user enters a number, the system squares the number and checks whether the result ends with the same digits as the original code. If yes, the locker grants access.

An automorphic number is a number whose square ends with the same number.

Example:
25² = 625

Write a program using loops to check whether the entered number is an Automorphic number.

Input:
25

Output:
Automorphic Number
"""
"""
n= int(input("n ="))
sq = n*n
temp =n
for i in range(1,2):
     r = sq %100
     if temp == r :
         print("Automorphic number")
     else:
         print("Non automorphic number")

"""

"""
7. Duck Number Checker

A verification system is used by an e-commerce company to validate promotional coupon numbers. Coupon numbers containing at least one zero in between digits are considered special duck numbers. However, if the number starts with zero, it is rejected immediately.

A duck number is a number that contains at least one zero but does not start with zero.

Example:
1023

Write a program using loops to check whether the entered number is a Duck number.

Input:
1023

Output:
Duck Number
"""
"""
n= int(input("n ="))
d=1
for i in range(len(str(n))):
      r= n%10  
      d= d *r
      n= n//10
if d == 0:
        print("Duck number") 
        
else:
        print("not a duck number")
"""

"""
8.
Mirror Difference Transaction Verification System
A multinational banking company processes thousands of daily transaction IDs. To detect suspicious patterns and validate system-generated IDs,
 the security software performs a Mirror Difference Verification Test.
For every entered transaction ID:

Reverse the digits of the transaction ID

Find the absolute difference between the original ID and the reversed ID


Count the total number of digits in the difference


Apply the following conditions using if-elif-else:

If the difference is 0, print Perfect Match


Else if the difference is divisible by 9, print Verified


Else print Rejected


Write a program to automate this verification process using loops and conditional statements.
Input:
4215
Output:
Reverse = 5124Difference = 909Digits = 3Verified
Input:
1221
Output:
Reverse = 1221Difference = 0Digits = 1Perfect Match
Input:
1234
Output:
Reverse = 4321Difference = 3087Digits = 4Verified
"""


n= int(input("n ="))
temp =n
rev =0

for i in range(len(str(n))):
       rev= rev*10 +n%10 
       n= n//10
print(rev)

diff =  rev - temp 
print(diff)

count =0 

for i in range(len(str(diff))) :
        r = diff % 10
        count = count +1
        diff = diff //10
print(count)

if diff == "0" :
     print("Perfect match")
elif diff % 9 ==0 :
     print("Verified")
else :
     print("Rejected")


"""
9.
Step Difference Number Analyzer

A mathematics research center studies hidden patterns inside numbers.
For every entered number, the system compares adjacent digits step by step.

Write a program to:

Find the absolute difference between every pair of adjacent digits
Display all step differences
Find the sum of all step differences
Find the largest step difference
If the sum of step differences is divisible by the number of digits, print Balanced Number
Otherwise print Unbalanced Number

Use loops wherever required.

Input:
57294
Output:
Step Differences: 2 5 7 5
Sum = 19
Largest = 7
Unbalanced Number
"""
"""
n= int(input("n ="))
a = len(str(n))
diff =r2 -r1

for i in range(a):
      r1 = n % 10
      r2 = n % 100
      
      n =n//10
    
      print(diff , end =" ")   

"""
"""
10.
 Prime Security Code Checker

A high-security research lab uses numeric passcodes to unlock restricted doors. To improve security,
 only prime numbers are accepted because they have exactly two factors and are harder to predict using common patterns.

When an employee enters a code, the system must verify whether the number is prime. If yes, access is granted; otherwise, access is denied.

Write a program to check whether the entered number is Prime or Not Prime.

Input:
29

Output:
Prime Number
"""
n= int(input("n ="))
x= 0

if n<=1 :
  print(" Not Prime")

else :
    i=2
    while i<n :
         if n% i ==0:
            x=1
            break
         i =i+1
if x ==0 :
    print("Prime Number")
else :
    print(" Not a prime number")
             
           






     
     