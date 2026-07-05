"""
1. Triple Operation Prime Verification System


A cybersecurity company generates a security score from entered access code.


Write a program to:


- Find sum of digits of the number

- Reverse the number

- Find absolute difference between original number and reverse

- Add digit sum and difference

- Check whether final result is Prime or Not Prime


Input:

4215


Output:

Sum of Digits = 12

Reverse = 5124

Difference = 909

Final Result = 921

Not Prime

"""
"""
n= int(input("n ="))
temp =n
sum= 0
l= len(str(temp))
for i in range(len(str(temp))):
     r= temp%10
     sum = sum+r
     temp= temp//10
print("sum =", sum)

rev=0
temp=n
for i in range(len(str(temp))) :
     rev=rev*10 + temp%10
     temp= temp//10
print("reverse =", rev)

diff = rev- n
print("difference =" , diff)

result = sum + diff
print("Result =", result)


if result<1 :
    print("not prime")
else: 
   flag=0
   i=2
   while i<result :
       if result %i ==0 :
          flag =1
          break
       i= i+1
   if flag ==0 :
      print("Prime number")
   else:
      print("Not prime number")
          
"""

"""
2. Multi Stage Prime Lock System


A smart locker opens only if final derived number is prime.


Write a program to:


- Find sum of digits

- Find product of digits

- Find difference between product and sum

- Count digits in difference

- Add digit count to difference

- Check whether final result is Prime or Not


Input:

234


Output:

Sum = 9

Product = 24

Difference = 15

Digits = 2

Final Result = 17

Prime
"""

"""
n= int(input("n ="))
l= len(str(n))
sum=0
temp=n
product =1
i=1
for i in range(l):
  r= temp% 10
  sum= sum+r
  product = product *r
  temp = temp//10
  i=i+1
print("sum is ", sum)
print("product is ", product)


diff = product - sum
print("Difference is", diff)
m= diff

count=0
i=0
while i<=(len(str(diff))):
     r1= diff %10
     count= count +1
     diff = diff//10
     i= i+1
print("count is" , count)


add = count + m
print("add", add)

i=1
while i<=(len(str(add))):
  if add %i ==0:
    print("Prime number")
    break
  i=i+1
"""

"""
3. Perfect Number Reward System


A gaming company rewards users if entered number is a Perfect Number.


(Perfect Number = sum of proper factors equals number)


Write a program using for-else loop to:


- Find sum of proper factors

- If sum equals number print Reward Unlocked

- Else print Try Again


Input:

6


Output:

Reward Unlocked
"""
"""
n= int(input("n ="))
temp =n
sum =0

for i in range(1,n):
      if n%i ==0:
        sum = sum+i
print("sum of factor", sum)

if sum ==temp:
    print("Reward unlocked")
else :
    print("Try again")
"""

"""
4.Unique Digit Security Scanner


A smart locker accepts only numbers whose all digits are unique.


Write a program using for-else loop to:


- Check every digit

- If any repeated digit found reject

- Else accept


Input:

57294


Output:

Valid Unique Code
"""


"""
n=int(input("enter the num="))
temp=n
flag=0

for i in range(len(str(n))):
    if temp >0:
      r=temp%10
      temp=temp//10

    t=temp
    if t >0:
      d=t%10

      if r==d:
        flag=1
        break
      t=t//10

      if flag==1:
        break

if flag == 1:
    print("Reject")
else:
    print("Valid Unique Code")
"""

"""

5.Number Stability Analyzer


A science lab studies whether digits are in increasing order.


Write a program using for-else loop:


- If every next digit is greater than previous print Stable Number

- Else Unstable Number


Input:

12359


Output:

Stable Number
"""
"""
n=int(input("enter the number="))
flag=0
for i in range(len(str(n))):
    r=n%10
    n=n//10
    r2=n%10
    n=n//10
    if r<r2:
       flag=1
       break
if flag==0:
   print("stable num")
else:
  print("unstable num")

"""
"""
  

6.

Next Prime Cabin Number Generator


A luxury hotel gives only prime numbered cabins to VIP guests.


Manager enters the last allotted cabin number.

System must find the next available prime cabin number.


Write a program using loops.


Input:

24


Output:

Next Prime Cabin = 29
"""
"""
n=int(input("enter the number="))
num=n+1
flag=0
while True:
    flag=0

    for i in range(2,num):
        if num%i==0:
           flag=1
           break
    if flag==0:
       print("next prime cabin",num)
       break
    num=num+1
"""
"""

7.

 Alternate Digit Prime Checker


A math lab adds alternate digits from right side.


Write a program to:


- Find sum of alternate digits

- Check whether sum is Prime or Not


Input:

12345


Output:

Alternate Sum = 9

Not Prime
"""
"""
n=int(input("enter the number"))
num=n
sum=0

for i in range(len(str(num))):
    r=num%10
    sum=sum+r
    num=num//100
print("alternate sum=",sum)

flag=0
if sum<=1:
   print("not prime")
else:
   for i in range(2,sum):
         if sum%i==0:
             flag=1
             break
   if flag==0:
      print("prime number")

   else:
      print("not prime")
"""
"""

8.

 ATM Note Counter


A bank ATM dispenses ₹100 notes.


Write a program to:


- Read withdrawal amount

- Count how many ₹100 notes needed using loop


Input:

700


Output:

Notes = 7
"""
"""
n=int(input("enter the amount"))

for i in range(len(str(n))):
    d=n%10
    n=n//10
print(d)
"""
"""
9.
9.

 Bike Service Kilometer Checker


A bike needs service every 3000 km.


Write a program to:


- Read travelled kilometers

- Print every service checkpoint till entered km


Input:

10000


Output:

3000 6000 9000
"""
"""
n= int(input("n ="))
i= 3000

if n<i :
   print("no service required")

while i<=n :
      print(i)
      i =i +3000
"""
"""
10.

Lift Mode Operation – Advanced Smart Elevator System
A smart building elevator works in multiple intelligent modes based on the mode number entered by the control panel.  
The system must automatically execute floor movement instructions using loops.

Write a program:

- If mode = 1  
  Normal Up Mode activated.  
  Read current floor and destination floor.  
  Print all floors from current to destination in ascending order.

- Else if mode = 2  
  Down Mode activated.  
  Read current floor and destination floor.  
  Print all floors from current to destination in descending order.

- Else if mode = 3  
  Energy Saving Mode activated.  
  Read destination floor.  
  Lift starts from ground floor (0) and stops only on alternate floors till destination.

- Else  
  Emergency Mode activated.  
  Print "Emergency Alarm" 4 times using loop.


Input:

3
6

Output:

0 2 4 6

Input:

1

2

7


Output:

2 3 4 5 6 7



Input:

2

8

3


Output:

8 7 6 5 4 3



Input:

5


Output:

Emergency Alarm

Emergency Alarm

Emergency Alarm

Emergency Alarm
"""

mode=int(input("enter the mode="))
current_floor,destination=map(int,input("Enter current floor and destination floor").split(","))
if mode==3:
    i=current_floor-3
    while i<=destination:
          print(i,end=" ")
          i=i+2
elif mode==2:
    i=current_floor
    while  i>=destination:
         print(i,end=" ")
         i=i-1
elif mode==1:
    i=current_floor
    while  i<=destination:
         print(i,end=" ")
         i=i+1         
else:
     i=1
     while i<=4:
          print("Emergency" )
          i=i+1
         
  
        

    

        



