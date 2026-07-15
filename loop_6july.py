"""
1.Leap Year Event Scheduler – Multi-Year Analysis System
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
"""
start=int(input("enter the start year "))
end = int(input("enter the end year"))
count=0
for i in range(start, end+1):
          if i%4 ==0:
               if i%100==0:
                      if i%400==0 :
                           print(i," Event schedule")
                           count +=1
                      else :
                           print("No event ")
               else:
                  print(i," Event scheduled ") 
                  count +=1
          else:
               print(" No Event")
               
print("Total leap year =", count)
print("Total events scheduled =", count)
"""

"""
2.
Fibonacci Series Generator

A learning app helps students understand number patterns. One of the most important patterns is the Fibonacci series, where each number is the sum of the previous two numbers.

The series starts with:
0 1

Write a program to:

- Read a number n (number of terms)
- Print the Fibonacci series up to n terms using a loop

Input:
7

Output:
0 1 1 2 3 5 8
"""
"""
n= int(input("n ="))
a,b = 0,1
for i in range(n):
    print(a,end= "")
    a,b= b,a+b

"""
"""
3.

Fibonacci Population Growth Tracker

A wildlife research team is studying the growth of a rare species.  
They observe that the population follows a Fibonacci pattern:

- Month 1 → 0 animals  
- Month 2 → 1 animal  
- Every next month → sum of previous two months  

The researchers want to analyze the growth pattern.

Write a program to:

- Read number of months n
- Generate Fibonacci series up to n months using loop
- Print population for each month
- Find total population observed
- Count how many months population exceeded 5

Input:
8

Output:
Population Growth:
0 1 1 2 3 5 8 13

Total Population = 33
Months with Population > 5 = 2
"""
"""
n= int(input("Enter the number :"))
a,b =0,1
sum=0
count =0
for i in range(n):
     print(a,end="")
     sum=sum+a
     if a>5 :
        count+=1
     a,b= b,a+b
print("Total Population =", sum)
print("Months Population exceed =",count)

"""
"""
4.Spy Number Detector

A cybersecurity system flags special numeric codes.

A number is called a Spy Number if:
Sum of digits = Product of digits

Write a program to check whether the entered number is Spy Number or Not.

Input:
1124

Output:
Spy Number
"""
"""
n= int(input("n ="))
sum =0
product =1
for i in range(len(str(n))):
     r=n%10
     sum= sum +r
     product = product *r
     n =n//10
if sum == product :
    print("Spy Number")
else:
    print("Not a spy number")
"""

"""
5.

Automorphic Number Lock

A high-security digital locker validates access codes using a special mathematical rule.

When a user enters a numeric code, the system squares the number and checks whether the last digits of the square match the original number.
 If it matches, the code is considered valid.

An Automorphic Number is a number whose square ends with the same number.

Task:
Write a Python program to check whether a given number is an Automorphic Number or not.

Example:
Input:
25

Output:
Automorphic Number
"""
"""
n= int(input("n ="))
temp =n
digit =0
while temp>0 :
    digit+=1
    temp= temp // 10
divisor = 10**digit
sq = n*n

if sq % divisor==n :
      print("Automorphic Number")
else :
      print("Not an Automorphic Number")
"""

"""
6.Buzz Number Detector 

A gaming system includes a special feature to identify “Buzz Numbers” for unlocking bonus rewards. Whenever a player enters a number, the system evaluates it using a predefined mathematical rule before granting access to hidden features.

A number is considered a Buzz Number if it satisfies at least one of the following conditions:

* The number is divisible by 7, OR
* The number ends with the digit 7

If the number satisfies any one of these conditions, it is treated as a valid Buzz Number and the player receives a reward. Otherwise, the system rejects the number.

Task:
Write a Python program to check whether a given number is a Buzz Number or not.

Example:
Input:
27

Output:
Buzz Number

"""
"""
n= int(input("n ="))
temp =n

if temp%10 ==7 or temp% 7 ==0:
       print("Buzz number")
else:
       print("Not  buzz number")
"""

"""
7.
Adam Number Verification System – Question

A high-security digital system is designed to validate special mirrored numbers known as Adam Numbers before granting access to sensitive data.

When a user enters a numeric code, the system performs a dual verification process:

* It calculates the square of the entered number.
* It reverses the number and calculates the square of the reversed value.
* Finally, it checks whether both results are mirror images (reverses) of each other.

A number is called an Adam Number if:
The square of the number and the square of its reverse are reverses of each other.

Task:
Write a Python program to check whether a given number is an Adam Number or not.

Examples:

Input:
12
Output:
Adam Number

Input:
13
Output:
Not an Adam Number

Input:
11
Output:
Adam Number

Example:
12 → 12² = 144, reverse(12) = 21 → 21² = 441 → reverse of 144
"""

"""
n= int(input("n ="))
sq= n*n
temp2 = sq
temp=n
rev1 =0
for i in range(len(str(temp))):
        rev1= rev1*10 + temp%10
        temp=  temp//10

rev_sq = rev1*rev1
rev2 =0
temp2 = sq
for j in range(len(str(sq))):
         rev2= rev2*10 +temp2%10
         temp2 =temp2//10

if rev_sq == rev2 :
      print("Adam number")
else :
      print("Not an Adam number") 

"""

"""
8.
Trimorphic Number Analyzer

A coding system checks cube-based patterns.

A Trimorphic Number:
Cube of number ends with the same number.

Example:
4³ = 64

Write a program to check Trimorphic Number.

Input:
4

Output:
Trimorphic Number
"""
"""
n= int(input("n ="))
temp =n
digit =0
while temp >0 :
       digit+=1
       temp =temp//10
divisor= 10**digit
cube = n*n*n
if cube % divisor ==n:
      print("Trimorphic number")
else:
      print("Not Trimorphic") 
"""
"""
9.
Abundant Number Detector

A financial system analyzes surplus numbers.

An Abundant Number:
Sum of proper factors > number

Write a program to check Abundant Number.

Input:
12

Output:
Abundant Number
"""
"""
n= int(input("n ="))


i=1
sum=0

temp =n
while i<=temp//2 :
     if temp%i ==0:
         
         sum= sum+i
     i+=1
if n< sum :
      print("Abundant Number")
else:
      print("Not Abundant")
"""
"""
10.
Electricity Bill Processing System (Multi-House)

An electricity board processes bills for multiple houses in a society.

Write a program to:

- Read number of houses n
- For each house:
    - Read units consumed
    - Calculate bill using slab rates:

        First 100 units      → ₹5 per unit  
        Next 100 units      → ₹7 per unit  
        Above 200 units     → ₹10 per unit  

    - Apply conditions:
        - If bill > ₹2000 → add 10% surcharge  
        - If units < 50 → give ₹100 subsidy  

    - Print bill for each house

- After processing all houses:
    - Print total bill collected
    - Print highest bill

---

Input:
3
120
250
40

Output:
House 1 Bill = 640
House 2 Bill = 1700
House 3 Bill = 100

Total Collection = 2440
Highest Bill = 1700
"""

n= int(input("enter number of houses ="))
total =0
highest =0
for i in range(1,n+1) :
   unit = int(input("enter units ="))
   bill =0
   if unit<100 :
        bill=100*5
   elif unit >=100 and unit <=200:
        bill= 100*5 +7*(unit-100)
   else :
        bill= 100*5 + 100*7 +10*(unit-200)
        print("bill amount =",bill)

   if bill>2000:
       surcharge = (bill*10/100)

   if unit<50 :
       bill = bill-100
   if bill<0 :
       bill =0
   
   print("house",i,"Bill =",bill)
   total= total + bill
   
   if bill >highest :
      highest = bill

print("Total Collection =", total)
print("Highest bill =",highest)
   
   
  
 