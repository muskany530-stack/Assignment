"""
Assignment 1: Restaurant Bill Split

A group of friends went to a restaurant. The restaurant adds GST and service charge to the bill, and then the total is divided equally.

Input:
Total bill amount = 2500
GST = 5%
Service charge = 10%
Number of friends = 4

Expected Output:
Final Bill = 2875.0
Each Person Pays = 718.75

---
"""
"""
total_amount= int(input("enter the bill amount"))
gst=  int(input("enter the GST percent"))
service_charge=  int(input("enter the service charge"))
friends=  int(input("enter the Total number of friends"))

gst_tax = total_amount * gst/100
service_tax = total_amount *service_charge /100
total_bill= total_amount + gst_tax + service_tax
each_person = total_bill/friends
print("Final Bill",total_bill)
print("Each person Pays", each_person)
"""
"""
Assignment 2: Mobile EMI Calculation

You purchased a mobile phone using EMI. After paying a down payment, the remaining amount includes interest and is divided into monthly installments.

Input:
Mobile price = 30000
Down payment = 5000
Interest rate = 10%
Months = 10

Expected Output:
Remaining Amount = 25000
Total with Interest = 27500
Monthly EMI = 2750.0

---
"""
"""
price, down_payment, interest_rate, months= map(int, input(" enter the values").split())
remaining_amount= price - down_payment
total_amount=( remaining_amount * interest_rate/100)+ remaining_amount
monthly_emi = total_amount/months
print("Remaining Amount ", remaining_amount)
print("Total with Interest ", total_amount)
print("Monthly EMI ", monthly_emi)
"""
"""
---

Assignment 3: Student Marks Analysis

A student wants to calculate total marks, average, and percentage from 5 subjects.

Input:
Marks = 78, 85, 90, 88, 80

Expected Output:
Total = 421
Average = 84.2
Percentage = 84.2

---
"""
"""
mark1, mark2, mark3, mark4, mark5= map(int,input("enter the marks").split())
total= mark1+ mark2+ mark3+ mark4+ mark5
average= total/5
percentage= (total/500)*100
print("Total =",total)
print("Average =",average)
print("Percentage =",percentage)
"""
"""
---

Assignment 4: Travel Distance Calculation

A person is traveling at a constant speed. Time is given in hours and minutes. Convert total time into hours and calculate distance.

Input:
Speed = 60 km/hr
Time = 2 hours 30 minutes

Expected Output:
Total Time = 2.5 hours
Distance = 150.0 km

---
"""
"""
speed,hours, minutes=map(int,input("enter the speed and time in hr and min").split())
time= minutes/60
total_time= hours+time
distance= speed*total_time
print("Total time ", total_time,"hours")
print("Distance ", distance,"km")
"""
"""
---

Assignment 5: Salary Breakdown

An employee wants to calculate salary per day and per hour.

Input:
Monthly salary = 36000
Working days = 24
Working hours per day = 8

Expected Output:
Salary per day = 1500.0
Salary per hour = 187.5

---
"""
"""
monthly_salary= int(input("enter the salary"))
working_days= int(input("working days"))
working_hour= int(input(" working hours per day"))
s_per_day= monthly_salary/24
s_per_hour= s_per_day /8
print(" Salary per day =",s_per_day)
print(" Salary per Hour =",s_per_hour)
"""
"""
---

Assignment 6: Data Storage Conversion

A user wants to convert data from GB into MB and KB.

Input:
Data = 5 GB

Expected Output:
In MB = 5120.0
In KB = 5242880.0

---
"""
"""
Gb= int(input(" Data in GB"))
Mb= Gb*1024
Kb= Mb*1024
print("In MB =",Mb)
print("In KB =", Kb)
"""
"""
---

Assignment 7: Cricket Run Rate

In cricket, overs are given in decimal format (e.g., 48.3 means 48 overs and 3 balls). Convert overs into total balls and calculate run rate.

Input:
Total runs = 275
Overs = 48.3

Expected Output:
Total Balls = 291
Run Rate = 5.67

---
"""
"""
total_runs=int(input("enter the runs"))
overs= float(input("enter the overs"))
balls= int(input("enter the balls"))
total_balls= overs*6+balls
run_rate= total_runs/overs
print("Total balls =", total_balls)
print("Run rate =", run_rate)
"""
"""
Assignment 8: Compound Interest

A person invests money in a bank that provides compound interest annually.

Input:
Principal = 10000
Rate = 5%
Time = 2 years

Expected Output:
Amount after interest = 11025.0

---
"""
"""
p= int(input("Principal ="))
r=int(input("Rate ="))
t= int(input("Time ="))
amount=p*((1+r/100))**t
print("Amount after interest =", amount)
"""
"""
---

Assignment 9: Petrol Cost Calculation

You traveled a certain distance. Based on mileage and petrol price, calculate fuel used and total cost.

Input:
Distance = 450 km
Mileage = 15 km/litre
Petrol price = 110/litre

Expected Output:
Petrol Used = 30.0 litres
Total Cost = 3300.0

---
"""
"""
dist, mileage, petrol_price= map(int,input("enter the values").split())
petrol_used= dist/mileage
total_cost= petrol_used*petrol_price
print("Petrol used ",petrol_used)
print("Total Cost ", total_cost)
"""
"""
---

Assignment 10: Time Conversion

Convert total seconds into hours, minutes, and seconds.

Input:
Total seconds = 7384

Expected Output:
Hours = 2
Minutes = 3
Seconds = 4

---
"""

total_seconds= int(input(" enter total seconds"))
hours= total_seconds//3600
rem_hr = total_seconds % 3600
minutes= rem_hr // 60
rem_min= rem_hr % 60
seconds= rem_min
print("Hours =", hours)
print("Minutes =", minutes)
print("Seconds =", seconds)

"""
---

Assignment 11: Expression Evaluation

A billing system applies nested calculations with discounts and extra charges using brackets and unary operators.

Input:
50 + (10 * (+(2**3))) / 4 - (-6 % 4)

---
"""
"""
print(50+ (10*(+(2**3)))/ 4-(-6 % 4))
"""
"""
---

Assignment 12: Expression Evaluation

A gaming score system calculates bonus points using exponent and applies penalties using unary negative values and brackets.

Input:
100 - (20 * (3**2)) + (40 / (+5)) - (-3)

---
"""
"""
print(100 - (20 * (3**2)) + (40 / (+5)) - (-3))
"""
"""
---

Assignment 13: Expression Evaluation

A shopping application applies offers using exponent and grouped calculations with unary adjustments.

Input:
25 + (5 * (6**2) // 3) - (-(8 % 5)) + (+2)

---
"""
"""
print(25 + (5 * (6**2) // 3) - (-(8 % 5)) + (+2))
"""
"""
---

Assignment 14: Expression Evaluation

A travel fare calculator computes total fare using grouped operations, power calculations, and unary adjustments.

Input:
(80 / (4 * 2)) * (+(2**2)) + 15 - (-(9 % 2))

---
"""
"""
print( (80 / (4 * 2)) * (+(2**2)) + 15 - (-(9 % 2)) )
"""
"""
---

Assignment 15: Expression Evaluation

An electricity billing system uses nested brackets, exponent-based scaling, and unary corrections.

Input:
60 + (12 * (2**3) // (+(4))) - (-(10 % 3))

---
"""
"""
print(60 + (12 * (2**3) // (+(4))) - (-(10 % 3)))
"""
"""
Assignment 16: Expression Evaluation

A performance evaluation system calculates final score using grouped operations, exponent, division, and unary adjustments.

Input:
45 + (15 * (2**2)) - (20 / (+(5))) + (-(7 % 3))

---
"""
"""
print(45 + (15 * (2**2)) - (20 / (+(5))) + (-(7 % 3)))
"""

