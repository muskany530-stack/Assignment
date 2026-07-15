"""
1.
Multiplication Table Generator

Scenario:
A school learning app helps students practice multiplication tables.
The user enters a number n, and the system prints multiplication tables from 1 to n using nested loops.

Input:
Enter limit: 3

Output:
1 x 1 = 1
1 x 2 = 2
1 x 3 = 3

2 x 1 = 2
2 x 2 = 4
2 x 3 = 6

3 x 1 = 3
3 x 2 = 6
3 x 3 = 9
"""
"""
n = int(input(" enter limit  ="))

for n in range (1,4):
        for i in range(1,4):
             print(n ,"*",i , " =" , n*i)
"""

"""
2.
Perfect Number Analyzer

A mathematics research system analyzes special numbers within a given range.
The user enters a starting number and ending number.
The system checks every number in that range and displays all Perfect Numbers using nested loops.

(A Perfect Number is a number whose sum of proper divisors is equal to the number itself.)

Input:
Enter starting number: 1
Enter ending number: 1000

Output:
Perfect Numbers are:
6
28
496

"""
"""
a = int(input("enter starting num :"))
b= int(input("enter ending num :"))

while a<= b :
         i=1
         sum =0
         temp =a
         while i < temp //2+1 :
                if temp% i ==0 :
                     sum = sum + i
                i= i+1

         if sum == a:
             print("perfect numbers are ")
             print(a)
         a= a+1
"""

"""
3.
Prime Number Range Checker

A cyber security system generates prime numbers for encryption analysis.
The user enters a starting number and ending number.
The system checks and displays all prime numbers between the given range using nested loops.

Input:
Enter starting number: 10
Enter ending number: 50

Output:
Prime Numbers are:
11
13
17
19
23
29
31
37
41
43
47
"""
"""

a= int(input("enter starting number :"))
b= int(input("enter ending number :"))

while a<=b :
       n=a
       x= True
       if n>1 :
            i =2
            while i<n//2 :
               if n%i ==0 :
                  x = False
                  break
               i=i+1

       if x == True :
            print(n)
       a=a+1 
                  
"""

"""

4.
Armstrong Number Finder

A digital number analysis system checks for Armstrong numbers within a range.
The user enters starting and ending numbers.
The system finds all Armstrong numbers using nested loops.

Input:
Enter starting number: 1
Enter ending number: 500

Output:
Armstrong Numbers are:
1
153
370
371
407
"""
"""
a= int(input("enter starting number :"))
b= int(input("enter ending number :"))

for a in range(a , b+1):
         sum=0
         temp =a
         p= len(str(a))
         i =1
         while a<b :
             digit = a%10
             sum = sum+ digit **p
             a= a//10
         i=i+1
 

if sum == temp :
      print(a)
"""

"""
5.
Strong Number Detector

A banking security system uses Strong Numbers for special authentication testing.
The user enters a range of numbers.
The system identifies all Strong Numbers between the given range using nested loops.

A Strong Number is a number in which the sum of factorials of its digits is equal to the original number.

Example:
145

1! + 4! + 5!
= 1 + 24 + 120
= 145

Since the sum is equal to the original number, 145 is called a Strong Number.

Input:
Enter starting number: 1
Enter ending number: 500

Output:
Strong Numbers are:
1
2
145
"""
"""
a= int(input("enter starting number :"))
b= int(input("enter ending number :"))

for a in range(a, b+1):
      temp =a 
      total =0 
      while temp >0 :
           d = temp% 10
           fact =1 
           
           for i in range(1 , d+1):
               fact=  fact*i
           total = total + fact
           temp = temp //10
      if total == a :
          print(a)
              
"""

"""
6.
Palindrome Number Range Checker

A barcode verification system checks for palindrome numbers within a specific range.
The user enters starting and ending numbers.
The system displays all palindrome numbers using nested loops.

Input:
Enter starting number: 100
Enter ending number: 200

Output:
Palindrome Numbers are:
101
111
121
131
141
151
161
171
181
191

"""

"""

a= int(input("enter starting number :"))
b= int(input("enter ending number :"))

for a in range(a, b+1):
          temp = a
          rev =0
         
          for i in range(len (str(temp))) :
              rev = rev*10 + temp% 10
              
              temp = temp //10
             
          if rev == a :
               print(a)                
        
"""
"""
7.
Neon Number Detector

Scenario:
A smart calculator system checks special numbers used in mathematical testing.
The user enters a range of numbers.
The system identifies all Neon Numbers using nested loops.

Theory:
A Neon Number is a number where the sum of digits of its square is equal to the original number.

Example:
9

Square of 9 = 81

8 + 1 = 9

Since the sum is equal to the original number, 9 is called a Neon Number.

Input:
Enter starting number: 1
Enter ending number: 100

Output:
Neon Numbers are:
1
9

"""
"""
a= int(input("enter starting number :"))
b= int(input("enter ending number :"))

for a in range(a, b+1):
         temp =a
         sum =0
         sq = a*a
         for i in range(len(str(sq))):
                
                 r = sq %10
                 sum = sum +r
                 sq = sq//10
         if sum == a :
                print(a)

"""

"""
8.
Online Exam Result Processing System

An online examination system stores marks of multiple classes.
Each class contains multiple students, and each student has marks for multiple subjects.

The program should use:
- First loop for classes
- Second loop for students
- Third loop for subjects

The system calculates total marks of every student.

Input:
Enter number of classes: 2
Enter students per class: 2
Enter subjects per student: 3

Class 1

Student 1
Enter mark: 70
Enter mark: 80
Enter mark: 90

Student 2
Enter mark: 60
Enter mark: 75
Enter mark: 85

Class 2

Student 1
Enter mark: 88
Enter mark: 77
Enter mark: 66

Student 2
Enter mark: 90
Enter mark: 92
Enter mark: 95

Output:
Class 1
Student 1 Total = 240
Student 2 Total = 220

Class 2
Student 1 Total = 231
Student 2 Total = 277

"""
"""
a = int(input("enter number of classes"))
b= int(input("enter students"))
c= int(input("enter subject per student"))

for i in range(1 ,a+1):
     print("class =",i)
     for j in range (1, b+1):
         print("students =", j)
         total =0
         for k in range(1 ,c+1):
             marks= int(input("enter marks ="))
             total = total + marks
         print("students ", j, "Total ", total)

"""

"""
9.Leap Year Event Scheduler – Multi-Year Analysis System

A city event management system schedules special festivals only in leap years.

To plan future events, the system analyzes multiple years instead of just one.

Write a program to:

- Read start year and end year from user
- For every year in the range, check whether it is a Leap Year or Not 
- Apply rules:
    - Divisible by 4 → Leap Year candidate  
    - Divisible by 100 → Not Leap Year  
    - Divisible by 400 → Leap Year  

- If leap year → print year with "Event Scheduled"
- Else → print year with "No Event"

- After checking all years:
    - Count total leap years
    - Print total events scheduled

Input:
2000
2005

Output:
2000 → Event Scheduled
2001 → No Event
2002 → No Event
2003 → No Event
2004 → Event Scheduled
2005 → No Event

Total Leap Years = 2
Total Events Scheduled = 2

"""

a= int(input("enter starting number :"))
b= int(input("enter ending number :"))
count=0
for n in range(a, b+1):
      if n%4==0:
         if n%100==0:
            if n%400==0:
               print(n,"-> event scheduled")
               count=count+1
            else:
               print(n,"no event")
         else:
             print(n,"event scheduled")
             count=count+1
      else:
           print(n,"no event")
 

print("Total Leap Years =",count)
print("Total Events Scheduled =",count)



































             