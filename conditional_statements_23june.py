"""
1. Electricity Department Billing System


The electricity department of a city wants to automate the monthly bill generation process for its customers. The bill is calculated based on slab-wise unit consumption:

* First 100 units are charged at ₹5 per unit
* Next 100 units (101–200) are charged at ₹7 per unit
* Units above 200 are charged at ₹10 per unit

Write a Python program to calculate the total electricity bill based on the number of units consumed.

Input:
Enter units consumed: 250

Output:
Total Electricity Bill: ₹1950
"""
"""
unit= int(input(" enter units consumed :"))
if unit<100 :
   print("Total electricity bill", unit*5)

elif unit>=200 :
   print("Total electricity bill", 5*100 + 7*(unit-100))

else:
   print("Total electricity bill", 5*100 +7*100 + 10*(unit-200))
"""
"""
2. College Result Processing System


A college wants to generate grades for students automatically based on their marks in an exam. The grading criteria are as follows:

* 90 and above → Grade A
* 75 to 89 → Grade B
* 60 to 74 → Grade C
* 50 to 59 → Grade D
* Below 50 → Fail

Write a Python program to display the grade of a student.

Input:
Enter marks: 67

Output:
Grade: C
"""
"""
marks = int(input("enter the marks"))

if marks>=90 :
      print("Grade A")
elif marks<=89 and marks>=75:
      print("Grade B")
elif marks<=74 and marks>=60:
      print("Grade C")
elif marks<=59 and marks>=50:
      print("Grade D")
else:
      print("Fail")
"""
"""
3. Income Tax Department System

The Income Tax Department needs a system to calculate tax payable by citizens based on their annual income:

* Up to ₹2,50,000 → No tax
* ₹2,50,001 to ₹5,00,000 → 5% tax
* ₹5,00,001 to ₹10,00,000 → 20% tax
* Above ₹10,00,000 → 30% tax

Write a Python program to calculate the tax amount.

Input:
Enter annual income: 800000

Output:
Tax Payable: ₹110000
"""
"""
income = int(input("enter annual income"))

if income<= 250000:
     print("No tax")

elif income>= 250001 and income<= 500000 :
     tax= income*5/100
     print("Tax payable :", tax)

elif income>= 500001 and income<= 1000000:
     tax = income*20/100
     print("Tax payable :", tax)

else:
     tax = income*30/100
     print("Tax payable :", tax)
"""
"""
4. E-Commerce Discount Engine


An online shopping platform provides discounts to customers based on their total purchase amount:

* Above ₹5000 → 20% discount
* ₹2000 to ₹5000 → 10% discount
* Below ₹2000 → 5% discount

Write a Python program to calculate the final amount after discount.

Input:
Enter purchase amount: 4500

Output:
Final Amount: ₹4050
"""
"""
amount= int(input("enter the purchase amount"))

if amount>5000 :
   discount= amount* 20/100
   final_amount= amount- discount
   print("final amount", final_amount)

elif amount>2000 and amount<=5000 :
   discount= amount* 10/100
   final_amount= amount- discount
   print("final amount", final_amount)

else :
   discount= amount*5/100
   final_amount= amount- discount
   print("final amount", final_amount)
"""
"""
5. Cinema Ticket Booking System


A cinema hall charges ticket prices based on the age of the customer:

* Children (below 12 years) → ₹100
* Adults (12 to 60 years) → ₹200
* Senior citizens (above 60 years) → ₹150

Write a Python program to determine the ticket price.

Input:
Enter age: 10

Output:
Ticket Price: ₹100
"""
"""
age= int(input("enter the age :"))

if age<12 :
    print("Ticket Price : 100")
elif age>12 and age<60 :
    print("Ticket Price : 200")
else :
    print("Ticket Price : 150")
"""
"""
6. Company Bonus Distribution System


A company wants to calculate bonuses for employees based on their years of experience:

* More than 10 years → 20% bonus
* 5 to 10 years → 10% bonus
* 2 to 5 years → 5% bonus
* Less than 2 years → No bonus

Write a Python program to calculate the bonus amount.

Input:
Enter salary: 50000
Enter years of experience: 6

Output:
Bonus Amount: ₹5000
"""
"""
salary= int(input("Enter salary :"))
years= int(input("Enter years of experience :"))

if years>10 :
     bonus= salary*20/100
     print("Bonus Amount",bonus)

elif years>5 and years<10 :
     bonus= salary*10/100
     print("Bonus Amount",bonus)

elif years>2 and years<5 :
     bonus= salary*5/100
     print("Bonus Amount",bonus)
else :
     print("No Bonus")
"""
"""
7. Banking Withdrawal Limit System


A bank wants to set withdrawal limits based on the available account balance:

* Balance less than ₹1000 → Withdrawal not allowed
* ₹1000 to ₹5000 → Maximum withdrawal ₹1000
* Above ₹5000 → Maximum withdrawal ₹5000

Write a Python program to display the withdrawal limit.

Input:
Enter account balance: 3500

Output:
Maximum Withdrawal Limit: ₹1000
"""
"""
balance = int(input("enter account balance :"))

if balance<1000 :
     print(" withdrawal not allowed ")

elif balance>1000 and balance<5000 :
     print(" Maximum withdrawal rs 1000 ")

else:
     print("Maximum withdrawal rs 5000")
"""
"""
8. Weather Monitoring System

A weather monitoring system classifies the weather condition based on temperature:

* Below 0°C → Freezing
* 0°C to 20°C → Cold
* 21°C to 35°C → Warm
* Above 35°C → Hot

Write a Python program to classify the weather.

Input:
Enter temperature: 38

Output:
Weather Condition: Hot
"""
"""
temperature = int(input("enter the temperature :"))

if temperature<0 :
     print("weather condition : Freezing")

elif temperature>0 and temperature<20 :
     print("weather condition : Cold")

elif temperature>21 and temperature<35 :
     print("weather condition : Warm")

else :
     print("weather condition : Hot")
"""
"""
9. Student Attendance Eligibility System

A college determines whether a student is eligible to sit for exams based on attendance percentage:

* 75% and above → Eligible
* 60% to 74% → Eligible with warning
* Below 60% → Not eligible

Write a Python program to check eligibility.

Input:
Enter attendance percentage: 58

Output:
Status: Not Eligible
"""
"""
attendance= int(input("enter attendance percentage :"))

if attendance>75 :
     print("Eligible")

elif attendance>60 and attendance<74 :
     print("Eligible with warning")

else :
     print("Not eligible")
"""
"""
10. Mobile Data Plan Advisor


A telecom company suggests the most suitable data plan based on a user’s daily data usage:

* More than 3GB/day → Premium Plan
* 1GB to 3GB/day → Standard Plan
* Less than 1GB/day → Basic Plan

Write a Python program to recommend a plan.

Input:
Enter daily data usage: 0.8

Output:
Recommended Plan: Basic Plan
"""
"""
data= float(input(" Enter daily data usage :"))

if data>3 :
     print("Premium Plan")
elif data<1 and data>3 :
     print("Standard Plan")
else :
     print("Basic plan")
"""
"""
11. Railway Ticket Fare System


A railway system calculates ticket fare based on distance and travel class:

* Distance ≤100 km:
  Sleeper → ₹100, AC → ₹200
* Distance 101–500 km:
  Sleeper → ₹300, AC → ₹600
* Distance >500 km:
  Sleeper → ₹500, AC → ₹1000

Write a Python program to calculate ticket fare.

Input:
Enter distance: 350
Enter class: AC

Output:
Total Fare: ₹600
"""
"""
distance = int(input("Enter distance :"))
class = int(input("Enter class :"))

if distance<= 100 :
    print
"""
"""
12. Restaurant Bill with GST System

A restaurant applies GST based on the total bill amount:

* Up to ₹1000 → 5% GST
* ₹1001 to ₹5000 → 12% GST
* Above ₹5000 → 18% GST
  Additionally, if the bill exceeds ₹3000, a service charge of ₹200 is added.

Write a Python program to calculate the final bill.

Input:
Enter bill amount: 4000

Output:
Final Bill Amount: ₹4680
"""
"""
bill= int(input("enter the bill amount :"))


if bill<1000:
     gst= bill*5/100
     

elif bill>1001 and bill<5000:
     gst= bill*12/100
     
else:
     gst= bill*18/100

final_bill = bill + gst
     
if bill>3000:
     final_bill =final_bill+200

print("final bill amount", final_bill) 
"""
"""
13. Employee Performance Appraisal System


A company evaluates employees based on performance rating (1–5):

* 5 → 25% salary hike
* 4 → 20% salary hike
* 3 → 10% salary hike
* 2 → 5% salary hike
* 1 → No hike
  If salary is below ₹20000 and rating is 4 or above, an additional ₹2000 bonus is given.

Write a Python program to calculate revised salary.

Input:
Enter salary: 18000
Enter rating: 4

Output:
Revised Salary: ₹23600
"""
"""
salary = int(input("enter salary"))
rating= int(input("enter rating"))

if rating==5 :
   total_salary= salary +(salary*25/100)
   
elif rating== 4:
   total_salary= salary + (salary*20/100)

elif rating==3 :
   total_salary = salary +(salary*10/100)

elif rating==2 :
   total_salary = salary+(salary*5/100)
   
else :
   print("No hike")

if salary<20000 and rating>=4 :
   revised_salary= total_salary + 2000

print(" Revised salary :",revised_salary)
"""
"""
14. Online Course Fee System

An online platform offers courses with fixed fees:

* Programming → ₹5000
* Design → ₹4000
* Marketing → ₹3000
  Discount is applied based on user type:
* Student → 20% discount
* Working Professional → 10% discount
* Others → No discount

Write a Python program to calculate final course fee.

Input:
Enter course category: Programming
Enter user type: Student

Output:
Final Course Fee: ₹4000
"""
"""
course = input("Enter the course category :")
user = input(" enter user type :")

if course== "programming":
    fees = 5000
elif course =="Design":
    fees =4000
elif course== "Marketing":
    fees =3000

if user =="student":
   discount = fees*20/100
elif user=="working professional" :
   discount = fees*10/100
else :
   discount =0

final_fees= fees-discount
print("Final course fees :", final_fees)
"""
"""
15. Smart Parking System

A smart parking system charges based on vehicle type and parking duration:

* Bike → ₹10/hour
* Car → ₹20/hour
* Bus → ₹50/hour
  If parking duration exceeds 5 hours, an additional ₹100 penalty is applied.

Write a Python program to calculate total parking fee.

Input:
Enter vehicle type: Car
Enter hours parked: 6

Output:
Total Parking Fee: ₹220
"""
"""
vehicle= input("enter vehicle type :")
hours = int(input("enter hours parked :"))

if vehicle =="bike" :
   park_fee = hours*10

elif vehicle =="car":
   park_fee = hours*20

else:
   park_fee = hours*50

if hours>=5 :
   park_fee = park_fee + 100

print("Park fee :", park_fee)
"""

# Nested if + if else questions

"""
1. Insurance Claim Approval System

An insurance company processes claims based on policy age, claim amount, and accident type. The approval depends on multiple levels of verification to reduce fraud.

If the policy age is at least 2 years, then check the claim amount. If the claim amount is up to 50000, then check the accident type. If it is minor, approve the claim; otherwise, approve it with inspection. If the claim amount is between 50001 and 200000, then check the accident type. If it is major, approve with investigation; otherwise reject. If the claim amount exceeds 200000, reject. If the policy age is less than 2 years, then check accident type. If minor, reject; otherwise mark as pending review.

Input:
Policy Age = 3
Claim Amount = 120000
Accident Type = major

Output:
Claim Status = Approved with Investigation
"""
"""
age = int(input("enter policy age :"))
amount = int(input("enter claim amount :"))
accident_type = input("enter accident type :").lower()

if age>=2 :
    if amount<=50000 :
         if accident_type=="minor":
               print("Approve the claim")
         else:
               print("Approve it by inspection")
    
    elif amount>=50001 and amount<=200000:
               if accident_type=="major":
                    print("Approve with investigation")
               else:
                    print("Rejected")
    
else :
    if accident_type=="minor":
        print("Rejected")
    else:
        print("Pending")
"""
"""
2. University Admission System

A university decides admission based on marks, entrance score, and category of the student.

If marks are 70 or above, then check entrance score. If entrance score is 80 or above, then check category. If general, admit; otherwise admit with scholarship. If entrance score is less than 80, then check if marks are 85 or above. If yes, admit under management quota; otherwise reject. If marks are below 70, then check if category is not general and marks are at least 60. If yes, check entrance score. If it is 70 or above, waitlist; otherwise reject. If none of these conditions match, reject.

Input:
Marks = 72
Entrance Score = 85
Category = general

Output:
Admission Status = Admitted
"""
"""
marks= int(input("Marks :"))
score = int(input("Enterance Score :"))
category = input("Category :")

if marks>=70 :
     if score>=80 :
          if category== "general":
                print("Admitted")
          else:
                print("Admit with scholarship")

     elif score<=80:
          if marks>=85:
               print("Admit under management quota")
          else:
               print("reject")

elif marks<=70 :
      if category!="general":
             if marks<=60:
                   if score>=70:
                       print("waitlist")
                   else:
                       print("reject")

else:
    print("Rejected")
"""
"""
3. Smart Loan Risk Categorization

A bank categorizes loan applicants into risk levels based on salary, credit score, and number of existing loans.

If salary is at least 30000, then check credit score. If credit score is 750 or above, then check number of loans. If zero, assign low risk. If loans are up to 2, assign medium risk; otherwise high risk. If credit score is below 750, then check if salary is at least 50000. If yes, check if credit score is at least 650. If yes, medium risk; otherwise high risk. If salary is less than 30000, mark as not eligible.

Input:
Salary = 40000
Credit Score = 760
Existing Loans = 1

Output:
Risk Level = Medium Risk
"""
"""
salary= int(input("Salary ="))
score = int(input("Credit Score ="))
loans= int(input(" Existing Loans ="))

if salary>=30000:
     if score>=750 :
           if loans ==0:
                print("Low risk")
           elif loans<=2 :
                print("Medium risk")
           else :
                print("High risk")

     else :
          if salary>=50000:
               if score>=650:
                   print("Medium risk")
               else:
                   print("high risk")

else:
    print("Not eligible")  
"""
"""
4. E-Learning Course Access System

An online learning platform grants access based on subscription type, course progress, and test score.

If subscription is premium, then check progress. If progress is at least 80, then check test score. If score is at least 70, unlock certificate; otherwise allow retry. If progress is less than 80, ask to complete course. If subscription is basic, then check progress. If progress is at least 50, allow limited access; otherwise lock content. If subscription is neither, deny access.

Input:
Subscription = premium
Progress = 85
Test Score = 65

Output:
Access Status = Retry Test
"""
"""
subscription = input("Subscription =")
progress= int(input("Progress ="))
test_score= int(input("Test Score ="))

if subscription =="premium":
       if progress>=80 :
             if test_score>=70:
                   print("Unlock certificates")
             else:
                   print("Retry test")
       elif progress<80 :
             print("Complete the course")

elif subscription == "Basic":
       if progress>=50 :
            print("limited access")
       else:
            print("lock content")
else:
    print("Deny Access") 
"""
"""
5. Smart Warehouse Dispatch System

A warehouse decides dispatch strategy based on stock availability, priority level, and delivery distance.

If stock is at least 100, then check priority. If high priority, then check distance. If distance is up to 200, dispatch immediately; otherwise use fast courier. If priority is not high, then check if stock is at least 300. If yes, bulk dispatch; otherwise normal dispatch. If stock is less than 100, then check if stock is at least 50. If yes, and priority is high, partially dispatch; otherwise hold. If stock is below 50, mark out of stock.

Input:
Stock = 120
Priority = high
Distance = 300

Output:
Dispatch Status = Dispatch via Fast Courier
"""
"""
stock= int(input("Stock ="))     
priority= (input("Priority =")).lower()    
distance= int(input("Distance =")) 

if stock>=100:
       if priority =="high" :   
               if distance<=200:
                    print("dispatch immediately")
               else:
                    print("use fast courier")
       elif priority !="high":
               if stock>=300:
                   print("bulk dispatch")
               else:
                   print("normal dispatch")

else  :
      if stock >50 :
           if priority =="high":
             print("partially dispatch")
          
           else:
             print("hold")
      else:
          print("out of stock")
"""
     

