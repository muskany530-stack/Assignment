"""
Assignment 1: Speed Calculator

Write a Python program that:

Accepts distance (in km) and time (in hours).
Calculates speed.

Input:
Distance = 120
Time = 2

Output:
Speed = 60 km/h
"""

"""
 distance= int(input(" enter the distance :"))
time= int(input(" enter the time :"))
speed= distance/ time
print(" Distance :", distance)
print(" Time :",time)
print(" Speed :", speed, " km/hr")
"""
"""
----------------------------------------
 Assignment 2: Salary Calculator

Write a Python program that:

Accepts daily wage and number of days.
Calculates total salary.

Input:
Daily wage = 500
Days = 26

Output:
Salary = 13000 
---------------------------------------------- 
"""
"""
daily_wage = int(input("enter the daily wage :"))
total_days= int(input("enter total days :"))
salary= daily_wage * total_days
print("Daily wage :",daily_wage)
print("Days :", total_days)
print("Salary :",salary)
"""
"""
----------------------------------------------
Assignment 3: Electricity Bill Calculator

Write a Python program that:

Accepts number of units.
Calculates bill (₹6 per unit).

Input:
Units = 100

Output:
Bill = 600
------------------------------------------
"""
"""
units = int(input("enter number of units :"))
per_unit_price= 6
total_bill = units * per_unit_price
print("Units :",units)
print("Total bill :",total_bill)
"""
"""
------------------------------------------
Assignment 4: Area of Rectangle

Write a Python program that:

Accepts length and breadth.
Calculates area.

Input:
Length = 10
Breadth = 5

Output:
Area = 50
------------------------------------------------
"""
"""
length= int(input("Enter the length :"))
breadth= int(input(" Enter the breadth :"))
area= length * breadth
print("Length =",length)
print("Breadth =",breadth)
print("Area =", area)
"""
"""
------------------------------------------------
Assignment 5: Average Marks Calculator

Write a Python program that:

Accepts marks of 3 subjects.
Calculates average.

Input:
Marks = 80, 90, 70

Output:
Average = 80.0
------------------------------------------------------------
"""
"""
num1 , num2 , num3 = map(int,input("Enter the marks :").split())
average = (num1 + num2 + num3)/3
print("Average =", average)
"""
"""
------------------------------------------------------------
Assignment 6: Discount Calculator

Write a Python program that:

Accepts total amount.
Calculates 10% discount and final price.

Input:
Amount = 1000

Output:
Discount = 100
Final = 900
----------------------------------------------------------------
"""
"""
amount= int(input(" enter total amount ="))
discount= amount* 10/100
final= amount-discount
print("Amount =",amount)
print("Discount =", discount)
print("Final =", final)
"""
"""
----------------------------------------------------------------
Assignment 7: Circle Area Calculator

Write a Python program that:

Accepts radius.
Calculates area of circle.

Input:
Radius = 7

Output:
Area = 153.86
------------------------------------------------------------------------
"""
"""
radius= int(input("enter the radius :"))
area = 3.14*radius*radius
print("Radius=",radius)
print("Area=", area)
"""
"""
------------------------------------------------------------------------
Assignment 8: Data Storage Converter

Write a Python program that:

Accepts value in MB.
Converts into GB.

Input:
MB = 2048

Output:
GB = 2.0
----------------------------------------------------------------------
"""
"""
mb = int(input(" value in mb"))
gb= mb/1000
print("MB =", mb)
print("GB =", gb)
"""
"""
----------------------------------------------------------------------
Assignment 9: Fuel Cost Calculator

Write a Python program that:

Accepts distance (km), mileage (km/litre), and petrol price.
Calculates total fuel cost.

Input:
Distance = 100
Mileage = 20
Petrol Price = 100

Output:
Cost = 500
"""
"""
distance= int(input("enter the distance"))
mileage= int(input(" enter the mileage"))
petrol= int( input("enter petrol price"))
total_fuel= distance/mileage
cost= total_fuel*petrol
print("Distance =", distance)
print("Mileage =", mileage)
print("Petrol =", petrol)
print("Cost =", cost)
"""
"""
Assignment 10: Percentage Calculator

Write a Python program that:

Accepts total marks and obtained marks.
Calculates percentage.

Input:
Total = 500
Obtained = 400

Output:
Percentage = 80%
"""
"""
total_marks= int(input("enter total marks"))
obtained_marks= int(input("enter obtained marks"))
percentage= obtained_marks/total_marks*100
print("Total ",total_marks)
print("Obtained ", obtained_marks)
print("Percentage ", percentage,"%")
"""
"""
Assignment 11: Time Duration Adder

Write a Python program that:

Accepts hours, minutes, seconds.
Converts into total seconds.

Input:
Hours = 1
Minutes = 2
Seconds = 30

Output:
Total Seconds = 3750
"""
"""
hours,minutes,seconds = map(int,input("enter hours minures and seconds").split())
hour= hours*3600
minute= minutes*60
second= seconds*1
total_seconds= hour + minute + second
print("Total seconds =", total_seconds )
"""
"""
Assignment 12: Change Return System

Write a Python program that:

Accepts amount.
Calculates ₹100, ₹50, ₹10 notes.

Input:
Amount = 380

Output:
₹100 x 3
₹50 x 1
₹10 x 3
"""
"""
amount= int(input(" enter amount"))
hundred= amount//100
remaining= amount %100
fifty= remaining//50
remain_fifty= remaining% 50
tens= remain_fifty//10
print(hundred)
print(fifty)
print(tens)
"""
"""
Assignment 13: Compound Interest Calculator

Write a Python program that:

Accepts principal, rate, and time.
Calculates compound interest.

Input:
Principal = 1000
Rate = 10
Time = 2

Output:
Amount = 1210.0
Compound Interest = 210.0
"""
"""
principal= int(input("enter principal amount"))
rate= int(input("enter rate"))
time=int(input("enter time "))
amount= principal*((1+(rate/100))**time)
compound_interest= amount-principal
print("Principal =", principal)
print("Rate =", rate)
print("Time =", time)
print("Amount =", amount)
print("Compound Interest =",compound_interest)
"""
"""
Assignment 14: Simple Profit or Loss Calculator

Write a Python program that:

Accepts cost price and selling price.
Calculates profit/loss and percentage.

Input:
Cost Price = 1000
Selling Price = 1200

Output:
Profit = 200
Profit % = 20.0
"""
"""
cost_price= int(input("enter the cost price"))
selling_price= int(input("enter the selling price"))
profit = selling_price - cost_price
profit_percent= (profit/cost_price)*100
print("Cost price =", cost_price)
print("Selling price =", selling_price)
print("Profit =", profit)
print("Profit % =", profit_percent)
"""
"""
Assignment 15: Average Speed for Multiple Trips

Write a Python program that:

Accepts distance1, time1, distance2, time2.
Calculates average speed.

Input:
Distance1 = 60
Time1 = 1
Distance2 = 40
Time2 = 1

Output:
Average Speed = 50 km/h
"""
dist1 = int(input(" enter distance1"))
dist2 = int(input(" enter distance2"))
time1 = int(input(" enter time1"))
time2 = int(input(" enter time2"))
avg_speed=(dist1+dist2)/(time1+time2)


print("Distance1 =",dist1)
print("Distance2 =",dist2)
print("Time1 =",time1)
print("Time2 =",time2)
print("Average speed", avg_speed ,"km/hr")






