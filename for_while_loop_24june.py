"""
1. Sum of First N Natural Numbers
A teacher wants to reward students by giving points daily. On day 1, a student gets 1 point, day 2 → 2 points, and so on. This follows a natural number sequence.
Write a program to calculate the *total points earned after n days* by summing all natural numbers up to n using loops.

Input: n = 10
Output: Total Points = 55
"""
"""
n= int(input("n ="))
sum =0
for i in range(0,n+1,1) :
     sum= sum +i
print("Total Points =",sum)
"""

"""
n= int(input("n ="))
i=1
sum=0
while i<=n :
     sum= sum+i
     i= i+1
print("Total Points =",sum)
"""

"""
2. Factorial of a Number
In project scheduling, tasks are dependent on previous tasks, and the total number of ways to arrange them is calculated using factorial. Factorial of a number n is the product of all numbers from 1 to n.
Write a program to calculate the *factorial of a given number using loops*.

Input: n = 5
Output: Total Ways = 120
"""

"""
n= int(input("n ="))
fact =1
for i in range(n,0,-1) :
     fact = fact*i
print("Total ways =", fact)
"""
"""
n= int(input("n ="))
fact= 1
i=1
while n>=i:
   fact= fact*i
   i= i+1
print(fact)
"""

"""
3. Multiplication Table
A shopkeeper wants to calculate bulk pricing for a product. If one item costs ₹n, then cost for multiple quantities can be calculated using multiplication.
Write a program to print the *multiplication table of a given number up to 10 using loops*.

Input: n = 6
Output:
6 x 1 = 6
6 x 2 = 12
...
6 x 10 = 60
"""

"""
n= int(input("n ="))
x=0
for i in range(1,11):
     print(n,"*",i,"is",n*i)
"""

"""
n= int(input("n ="))
x=0
i=1
while i<=10:
    print(n,"*",i,"is",n*i)
    i=i+1
"""

"""
4. Reverse a Number
A security system stores OTP codes in reverse format for encryption to increase data safety. Reversing a number means extracting digits and rebuilding it in reverse order.
Write a program to *reverse a given integer using loops*.

Input: 1234
Output: 4321
"""

"""
n= int(input("number ="))
rev=0
for i in range(len(str(n))):
      rev = rev * 10 + n%10
      n= n//10
print(rev)
"""

"""
n=int(input("n ="))
rev=0
while n>0:
      rev = rev*10 + n%10
      n=n//10
print(rev)
"""

"""
5. Palindrome Check
A number plate is considered special if it reads the same forward and backward. Such numbers are called palindromes.
Write a program to *check whether a given number is a palindrome using loops*.

Input: 121
Output: Palindrome
"""

"""
n= int(input("n ="))
temp=0
rev=0
for i in range(n,0,-1):
     rev = rev*10 +n%10
     n=n//10
if n==temp:
      print("palindrome")
else:
      print("not palindrome")
"""

"""
n= int(input("n ="))
temp = 0
rev=0
while n>0:
   rev= rev*10 +n%10
   n= n//10

if n==temp:
     print("palindrome")
else:
     print("not palindrome")
"""

"""
6. Armstrong Number (3-digit)
In coding competitions, certain numbers are considered unique. A 3-digit Armstrong number is one where the sum of the cubes of its digits equals the number itself.
Write a program to *check whether a number is an Armstrong number using loops*.

Input: 153
Output: Armstrong
"""

"""
num= int(input("n ="))
temp=num
sum=0
for i in range(3):
     n= num % 10
     sum= sum +( n**3)
     num = num//10
     
if sum == temp :
    print("armstrong number")
else:
    print("not an armstrong num")
"""
"""
num = int(input("n ="))
temp= num
sum=0
while num>0:
      n=num%10
      sum = sum+(n**3)
      num= num//10

if sum == temp:
      print("Armstrong number")
else:
      print("Not an armstrong")
"""

"""
7. Count Even Digits*
A data analyst is analyzing numeric IDs and needs to determine how many digits in the ID are even.
Write a program to *count the number of even digits in a given number using loops*.

Input: 123456
Output: Even digits count = 3

---
"""
"""
n= int(input("n ="))
count =0
for i in range(len(str(n))):
	r=n%10
	if r%2 ==0:
            count=count+1
	n=n//10
print(count)
"""

"""
n= int(input("n ="))
count=0
i=1
while n>=i :
      r =n%10
      if r%2==0 :
          count= count+1
      n=n//10
print(count)
"""

"""
*8. Count Odd Digits*
A banking system flags IDs with too many odd digits for further verification.
Write a program to *count the number of odd digits in a given number using loops*.

Input: 123456
Output: Odd digits count = 3
"""

"""
n= int(input("n ="))
count=0
i=1
while n>=i :
   r=n%10
   if r%2 != 0:
       count = count+1
   n=n//10
print(count)
"""

"""
9. Check All Digits Are Even*
A machine only accepts numbers where every digit is even. If any digit is odd, the number is rejected.
Write a program to *check whether all digits of a number are even using loops*.

Input: 2468
Output: All Even

Input: 2456
Output: Not All Even
"""

"""
n= int(input("Enter number ="))
a=len(str(n))
count=0
for i in range(a):
	r=n%10
	if r%2==0:
		count=count+1
	n=n//10
if a==count:
	print("All Even")
else:
	print("Not all even")
"""

"""
n= int(input("Enter number ="))
temp=len(str(n))
count=0

while n>0:
    r=n%10
    if r%2 ==0:
         count=count +1
    n=n//10
if temp==count :
      print("All even")
else:
      print("NOt all even")
    
"""
"""
10. Even Numbers Between Two Numbers*
A teacher wants to assign only even roll numbers for a special activity. The system should display all even numbers between two given numbers.
Write a program to *display all even numbers between two numbers using loops*.

Input: 10, 20
Output: 10 12 14 16 18 20
"""

"""
start= int(input("enter the start number"))
stop= int(input("enter the stop number"))

for i in range(start, stop, 1):
       if i%2 ==0 :
           print(i)
"""
"""

start= int(input("enter the start number"))
stop= int(input("enter the stop number"))

i= 1
while (start<stop) :
     if i%2 ==0:
         print(i)
     start= start+1
"""

"""
11. Count Occurrence of a Digit*
A system logs repeated digits in a number for pattern analysis and reporting.
Write a program to count how many times a given digit appears in a number us
"""
#for loop
n = input("Enter number: ")
d = input("Enter digit: ")

count = 0

for x in n:
    if x == d:
        count = count + 1

print(count)
"""
"""
#while loop
n = int(input("Enter number: "))
d = int(input("Enter digit: "))

count = 0

while n > 0:
    digit = n % 10

    if digit == d:
        count = count + 1

    n = n // 10

print(count)
"""

"""
12. Multiplication of Digits
A puzzle game calculates a score by multiplying all digits of a number together. After calculating the score, the game also checks whether the final score is even or odd to assign a bonus.
Write a program to find the product of all digits of a number using loops and then check whether the result is even or odd.

Input: 1234
Output: 24
Even
"""
"""
#for loop
n = input("Enter number: ")

product = 1

for x in n:
    product = product * int(x)

print(product)

if product % 2 == 0:
    print("Even")
else:
    print("Odd")
"""

""" 
#while loop


n = int(input("Enter number: "))

product = 1

while n > 0:
    digit = n % 10
    product = product * digit
    n = n // 10

print(product)

if product % 2 == 0:
    print("Even")
else:
    print("Odd")
"""

"""
13. Number Range Display System (if-elif with loops)*
A number analysis tool processes two input values and displays numbers between them based on their relationship.

* If the first number is less than the second, display numbers in ascending order
* If the first number is greater than the second, display numbers in descending order
* If both numbers are equal, display "Both numbers are same"

Write a program using if-elif-else and loops to implement this logic.

Input: 5, 10
Output: 5 6 7 8 9 10

Input: 10, 5
Output: 10 9 8 7 6 5

Input: 7, 7
Output: Both numbers are same

"""
"""
#for loop
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if a < b:
    for i in range(a, b + 1):
        print(i, end=" ")

elif a > b:
    for i in range(a, b - 1, -1):
        print(i, end=" ")

else:
    print("Both numbers are same")
"""
"""
#while loop

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if a < b:
    while a <= b:
        print(a, end=" ")
        a = a + 1

elif a > b:
    while a >= b:
        print(a, end=" ")
        a = a - 1

else:
    print("Both numbers are same")
"""

"""
14. Floor Movement System (Elevator)
An elevator system takes the current floor and destination floor as input.

If current floor < destination → move upward and display floors
If current floor > destination → move downward and display floors
If both are same → display "Already on the same floor"

Write a program using if-elif-else and loops to simulate elevator movement.

Input: 1, 5
Output: 1 → 2 → 3 → 4 → 5

Input: 7, 3
Output: 7 → 6 → 5 → 4 → 3

Input: 4, 4
Output: Already on the same floor
"""
"""
#for loop

current = int(input("Current floor: "))
destination = int(input("Destination floor: "))

if current < destination:
    for i in range(current, destination + 1):
        print(i, end=" ")

elif current > destination:
    for i in range(current, destination - 1, -1):
        print(i, end=" ")

else:
    print("Already on the same floor")
"""
"""
#while loop
current = int(input("Current floor: "))
destination = int(input("Destination floor: "))

if current < destination:
    while current =< destination:
        print(current, end=" ")
        current = current + 1

elif current > destination:
    while current >= destination:
        print(current, end=" ")
        current = current - 1

else:
    print("Already on the same floor")
""" 






      


      


