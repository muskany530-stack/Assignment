"""
n= int(input("n ="))
sum =0
i=1
while i<=n :
   sum= sum+i
   i=i+1
print("sum is", sum)
"""
"""
n= int(input("n ="))
sum =0

for i in range(0,n+1,1):
    sum = sum+i
  
print(sum)
"""
"""
n= int(input("n ="))
fact =1
for i in range(n,1,-1):
    fact= fact*i
print(fact)
"""
"""
n= int(input("n ="))
fact =1	
i=1
while n>=i :
     fact= fact*i
     i+=1
print(fact)
"""
"""
n= int(input("n ="))
for i in range(1,11,1):
    print(n,"*",i,"=",n*i)
"""
"""
n= int(input("n ="))
i=1
while i<=10:
    print(n,"*",i,"=",n*i)
    i+=1
"""
"""
n= int(input("n ="))
rev =0
for i in range(len(str(n))):
       rev= rev*10 +n%10
       n= n//10
       
print(rev)
"""

"""
n= int(input("n ="))
rev=0
while n>0:
   rev= rev*10 + n%10
   n= n//10
print(rev)
"""
"""
n= int(input("n ="))
temp= n
rev =0
for i in range(len(str(n))):
    rev= rev*10 + n%10
    n= n//10

if rev== temp:
    print("palindrone")
else:
    print("not a palindrone ")

"""
"""
n= int(input("n ="))
temp=n
rev=0
while n>0 :
   rev=rev*10 + n%10
   n= n//10
if rev== temp:
	print("palindrone")
else:
        print("not a palindrone ")
"""
"""
n= int(input("n ="))
temp=n
l= len(str(n))
count=0
for i in range(l):
     d= n%10
     count= count+ (d**l)
     n =n//10
print(count)

if count ==temp:
   print("armstrong")
else :
   print("not armstrong")
"""
"""
n= int(input("n ="))
temp=n
l= len(str(n))
count=0
while n>0 :
     d= n%10
     count= count+ (d**l)
     n =n//10
print(count)

if count ==temp:
   print("armstrong")
else :
   print("not armstrong")
"""
"""
n= int(input("n ="))
l= len(str(n))
count =0
for i in range(l):
     r= n%10
     if r%2 ==0:
        count= count+1
     n= n//10
print(count)
"""
"""
n= int(input("n ="))
count=0
while n>0:
    r= n%10
    if r%2==0:
      count+=1
    n= n//10
print(count)
"""
"""
n= int(input("n ="))
l= len(str(n))
count=0
for i in range(l):
    r= n%10
    if r%2 !=0:
        count+=1
    n=n//10
print(count)
"""
"""
n= int(input("n ="))
count =0
while n>0:
     r= n%10
     if r%2 !=0:
        count=count+1
     n= n//10
print(count)
"""
"""
n= int(input("n ="))
l= len(str(n))
count=0
for i in range(l):
     r= n%10
     if r%2 ==0:
       
        count=count+1
     n= n//10

if l== count:
   print("All even")
else:
   print("Not even") 
"""
"""
n= int(input("n ="))
count=0
while n>0 :
      r= n%10
      if r%2 ==0:
       
        count=count+1
      n= n//10
if count%2==0:
     print("All even")
else:
     print("Not even")
"""
"""
a= int(input("number1"))
b= int(input("number2"))

for i in range(a,b):
     if i%2 ==0:
         print(i,end =" ")
"""
"""
a= int(input("number1"))
b= int(input("number2"))

while a<b :
     if a%2 ==0:
       print(a, end =" ")
     a=a+1  
"""
"""
n= int(input("enter num"))    
d= int(input("enter digit"))
count=0
for i in range(len(str(n))) :
      r= n%10
      if r%d==0 :
           count= count+1
      n=n//10
print(count)
"""
"""
n= int(input("enter num"))    
d= int(input("enter digit"))
count=0
while n>0 :
      r= n%10
      if r%d==0 :
           count= count+1
      n=n//10
print(count)
"""
"""
n= int(input("enter num")) 
product =1
for i in range(len(str(n))):
       r= n%10
       product= product*r
       n= n//10
print(product)
"""
"""
n= int(input("enter num")) 
product =1
while n>0:
       r= n%10
       product= product*r
       n= n//10
print(product)
"""
"""
a= int(input("enter a"))    
b= int(input("enter b"))

if a<b :
    while a<b:
       
      a=a+1
      print(a)
    
elif a>b:
    while a>b:
      a=a-1
      print(a)
      
    
else:
   print("Both number are same")
"""
"""
a= int(input("enter a"))    
b= int(input("enter b"))
if a<b:
    for i in range(a,b):
         a=a+1
         print(a)
elif a>b:
    for i in range(a,b,-1):
         a=a-1
         print(a)
else:
   print("Both number are same")
"""
"""
current= int(input("current floor "))
destination = int(input("destination floor "))

if current<destination :
       while current<destination:
               current= current+1
               print(current)

elif current>destination:
       while current>destination:
               current = current-1
               print(current)

else:
      print("Already on same floor")
"""
"""
current= int(input("current floor "))
destination = int(input("destination floor "))

if current<destination :
       for i in range (current,destination):
               current= current+1
               print(current)

elif current>destination:
       for i in range (current,destination,-1):
               current = current-1
               print(current)

else:
      print("Already on same floor")


"""

# 25 june 2026
# loop practice questions

"""
1. Largest Digit in Number
A cybersecurity company checks numeric passwords used in smart lockers. To identify password strength, the system finds the highest digit present in the entered password. Higher digits indicate stronger variation in the password pattern.
Write a program to find the largest digit in a number using loops.

Input:
57294

Output:
Largest Digit = 9
"""

"""
n= int(input("n ="))
largest= 0
for i in range(len(str(n))):
       d= n%10 
       if d>largest :
           largest =d
       n= n//10
print(largest)
"""

"""
n= int(input("n ="))
largest =0
while n>0 :
      d = n%10
      if d> largest:
          largest=d
      n= n//10
print(largest)
"""

"""
2. Smallest Digit in Number
A manufacturing company prints serial numbers on products. During quality testing, the scanner needs to detect the smallest digit in the serial number to verify coding standards.
Write a program to find the smallest digit in a number using loops.

Input:
57294

Output:
Smallest Digit = 2
"""
"""
n= int(input("n ="))
smallest =n%10
for i in range(len(str(n))):
      d= n%10
      if d< smallest :
           smallest =d
      n =n//10
print(smallest)
"""
"""
n= int(input("n ="))
smallest =n%10
while n>0:
      d= n%10
      if d< smallest :
           smallest =d
      n =n//10
print(smallest)
"""

"""
3. First Digit of Number
A university receives thousands of application IDs. The first digit of each ID represents the department code, so the admission software must read the first digit quickly.
Write a program to find the first digit of a number using loops.

Input:
53892

Output:
First Digit = 5
"""
"""
n= int(input("n ="))
for i in range(len(str(n))):
      r= n%10
      n= n//10
print(r)
"""

"""
n= int(input("n ="))
while n>0:
      r= n%10
      n= n//10
print(r)
"""

"""
4. Numbers Divisible by 3 Between Two Numbers
A school is organizing a quiz competition. Only students whose roll numbers are divisible by 3 are selected for the first round. The teacher enters a roll number range and wants the system to display eligible roll numbers.
Write a program to display numbers divisible by 3 between two given numbers using loops.

Input:
10 25

Output:
12 15 18 21 24
"""
"""
a= int(input("a ="))
b= int(input("b ="))
while a<=b :
   if a%3 ==0 :
       print(a, end=" ")
   a=a+1
"""
"""
a= int(input("a ="))
b= int(input("b ="))
for i in range(a,b) :
   if a%3 ==0 :
       print(a, end=" ")
   a=a+1
"""
"""
5. Count Factors of Number
A mathematics learning app gives practice questions where students must know how many factors a number has. The app should automatically count the total factors of the entered number.
Write a program to count total factors of a number using loops.

Input:
12

Output:
Factors Count = 6
"""

"""
n= int(input("n ="))
count =0
i=1
while i<=n :
    if n%i ==0 :
        count= count+1
    i=i+1
print(count)
"""
"""
n= int(input("n ="))
count =0
for i in range(1,n+1) :
    if n%i ==0 :
        count= count+1
    
print(count)
"""

"""
6. Sum of Factors
A puzzle-based game rewards users based on the sum of all factors of a chosen number. The system calculates the total score using all factors of the entered number.
Write a program to find sum of factors using loops.

Input:
6

Output:
Sum = 12
"""

"""
n= int(input("n ="))
sum=0
i=1
while i<=n:
   if n%i ==0:
     sum = sum+i
   i+=1
print(sum)
"""

"""
n= int(input("n ="))
sum=0
for i in range(1,n+1):
  if n%i ==0:
     sum = sum+i
print(sum)
"""

"""

7. Power of a Number
A scientific calculator app is used by engineering students for repeated multiplication operations. It should calculate the value of a number raised to a given power.
Write a program to calculate n raised to power p using loops.

Input:
2 5

Output:
32
"""
"""
n= int(input("number =")) 
p= int(input("power ="))

for i in range(n,p+1):
   d = n**p
print(d) 
"""

"""
n= int(input("number =")) 
p= int(input("power ="))
i=1
while i<=p:
      d= n**p
      i= i+1
print(d)
"""

"""
8. Count Multiples of 5 Between Two Numbers
A supermarket gives coupons to customers whose token numbers are multiples of 5. The manager enters a token range and wants to know how many eligible token numbers exist.
Write a program to count numbers divisible by 5 between two given numbers using loops.

Input:
1 20

Output:
Count = 4
"""    

"""
a = int(input("a ="))
b = int(input("b ="))
count =0
while a<=b :
     if a%5== 0:
        count= count+1
     a =a+1      
print(count)
"""

"""
a = int(input("a ="))
b = int(input("b ="))
count =0
for i in range(a,b+1):
     if a%5== 0:
        count= count+1
     a =a+1      
print(count)
"""

"""
9. Neon Number LED Unlock Game
You're programming a new LED display game. The game level unlocks only when a neon number is entered.

A neon number is a number where the sum of the digits of its square is equal to the number itself.
Example: 9 → 9² = 81 → 8 + 1 = 9

Accept a number from the player.
Check whether it is a neon number using loops.

If true, display:
Glowing Success! You've found the Neon Number!

Otherwise display:
Try again! Not quite glowing yet.

Input:
9

Output:
Glowing Success! You've found the Neon Number!
"""

"""
n= int(input("n ="))
square= n*n
sum =0
for i in range(len(str(square))):
         r= square %10
         sum = sum+r
         square = square//10
print(sum)

if n == sum:
       print("Glowing Success! You've found the Neon Number!")
else:
       print("Try again! Not quite glowing yet.")
"""

"""
n= int(input("n ="))
square= n*n
sum =0
while square>0:
         r= square %10
         sum = sum+r
         square = square//10
         
print(sum)

if n == sum:
       print("Glowing Success! You've found the Neon Number!")
else:
       print("Try again! Not quite glowing yet.")
"""

"""
10. Student ID Validity Checker (Count Odd Digits)
A school management system assigns numeric IDs to students. The administration wants to verify IDs by checking how many odd digits are present in each ID number. IDs with more odd digits are sent for manual review.

Write a program to count the number of odd digits in a given student ID using loops.

Input:
572943

Output:
Odd Digits Count = 3
"""

"""
n=int(input("n ="))
count =0
for i in range(len(str(n))):
      r=n%10
      if r%2 !=0:
            count= count+1
      n=n//10
print(count)
"""

"""
n=int(input("n ="))
count =0
while n>0:
      r=n%10
      if r%2 !=0:
            count= count+1
      n=n//10
print(count)
"""












































