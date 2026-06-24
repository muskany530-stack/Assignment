"""
1. Smart Voting & ID Verification System
   A government system verifies whether a citizen can vote and whether they have a valid ID.

* If age ≥ 18 → Eligible to vote
* If ID proof is available → Allowed inside booth

Input:
Enter age: 22
Do you have ID (yes/no): yes

Output:
Eligible to vote
Allowed inside booth
"""
"""
age = int(input("enter age :"))
id = input(" Do You have any ID (yes/no) :")

if age>=18 :
      if id.lower() == "yes":
         print("Eligible to vote ")
         print("Allowed inside booth")
      else:
         print(" Not allowed inside the booth")
else:
    print(" Not Eligible to vote")
"""
"""
2. Student Performance Analyzer
   A school wants to evaluate students based on marks.

* If marks ≥ 40 → Pass
* If marks ≥ 75 → Distinction

Input:
Enter marks: 80

Output:
Pass
Distinction
"""
"""
marks= int(input("Enter marks :"))
if marks >= 40 :
    print("Pass")
if marks>= 75 :
    print("Distinction")
"""
"""
3. E-Commerce Offer Engine
   An online store provides multiple offers independently:

* If cart value ≥ 500 → Free delivery
* If cart value ≥ 1000 → 10% discount coupon

Input:
Enter cart value: 1200

Output:
Free delivery applied
Discount coupon unlocked
"""
"""
value= int(input("enter cart value :"))
if value >=500 :
    print(" free delivery")

if value >=1000 :
    print(" 10% discount coupon")
"""
"""
4. Gym Membership Eligibility Checker
   A gym checks multiple conditions:

* If age ≥ 18 → Allowed for gym
* If BMI > 25 → Suggest weight loss program

Input:
Enter age: 25
Enter BMI: 27

Output:
Gym access granted
Enroll in weight loss program
"""
"""
age = int(input("enter the age :"))
BMI = int(input("enter the BMI :"))
if age>=18 :
   print("Gym access granted")
else :
   print(" Not allowed for gym")
if BMI> 25 :
   print("enrolled in  weight loss program")
else :
   print(" enrolled in  weight gain program")
"""
"""
5. Banking Security System
   A bank validates login attempt:

* If username is "admin" → Valid user
* If password length ≥ 8 → Strong password

Input:
Enter username: admin
Enter password: secure123

Output:
Valid user
Strong password
"""
"""
username= input("enter username")
password= input("enter password")

if username == " admin":
    print("valid user")
if password == " secure123":
    print("strong password")
"""
"""
6. Weather Monitoring System
   A system checks weather conditions:

* If temperature ≥ 30 → Hot day
* If humidity ≥ 70 → High humidity alert

Input:
Enter temperature: 32
Enter humidity: 75

Output:
Hot day
High humidity alert
"""
"""
temp= int(input("enter temperature :"))
humidity = int(input("enter humidity :"))
if temp >=30 :
   print(" Hot Day")
if humidity >=70 :
   print(" High humidity alert")
"""
"""
7. Salary Benefits System
   A company provides benefits:

* If salary ≥ 30000 → Eligible for PF
* If salary ≥ 50000 → Eligible for bonus

Input:
Enter salary: 55000

Output:
PF applicable
Bonus applicable
"""
"""
salary =int(input(" enter salary "))
if salary>= 30000:
    print("Eligible for PF")
if salary >= 50000 :
    print("Eligible for bonus")
"""
"""
8. Number Property Checker
   A system evaluates number properties:

* If number % 2 == 0 → Even number
* If number % 5 == 0 → Divisible by 5

Input:
Enter number: 20

Output:
Even number
Divisible by 5
"""
"""
number = int(input("enter a number"))
if number%2 ==0 :
    print(" Even number")
if number%5 ==0 :
    print(" Divisible by 5")
"""
"""
9. Library Access System
   A library checks:

* If membership is active → Entry allowed
* If books issued < 3 → Can issue more books

Input:
Membership active (yes/no): yes
Books issued: 2

Output:
Entry allowed
Can issue more books
"""
"""
membership = input("Membership Active (yes/no)")
books = int(input("Books issued"))
if membership == "yes" :
    print("Entry allowed")
if books<=3 :
    print(" Can issue more books ")
"""
"""
10. Online Exam System
    System evaluates exam conditions:

* If marks ≥ 40 → Pass
* If attendance ≥ 75 → Eligible for certificate

Input:
Enter marks: 60
Enter attendance: 80

Output:
Pass
Eligible for certificate
"""
"""
marks= int(input("enter marks :"))
attendance = int(input("enter attendance :"))
if marks >=40 :
   print(" Pass ")
if attendance >=75 :
   print(" Eligible for certificate ")
"""
"""
1.1. A bank wants to automate its loan approval process. The system should take salary,
credit score, and number of existing loans as input. If the salary is greater than or equal to 30000,
then it should check the credit score. If the credit score is greater than or equal to 750,
 the loan should be approved. Otherwise, it should check the number of existing loans.
If the existing loans are less than 2, the loan should be conditionally approved; otherwise, it should be rejected.
If the salary is less than 30000, the loan should be rejected. Display the final loan status.

Input:
Salary = 40000
Credit Score = 720
Existing Loans = 1

Output:
Loan Status = Conditional Approval
"""
"""
salary= int(input(" enter salary:"))
credit_score= int(input(" enter score :"))
existing_loan = int(input(" enter existing loan :"))

if salary >= 30000:
      if credit_score >= 750 :
            print(" loan should be approved")
      else :
            print(" check the number of existing loans")
            if existing_loan <=2 :
                  print(" loan conditionally approved")
            else :
                  print(" it should be rejected")
else:
    print("loan should be rejected")
   
"""
"""
2. An e-commerce website provides discounts based on the cart value and user type.
The system should take cart value and user type (premium or regular) as input.
 If the cart value is greater than or equal to 5000, then check the user type. If the user is premium,
 apply a 20% discount; otherwise, apply a 10% discount. If the cart value is less than 5000,
then check if it is greater than or equal to 2000. If yes, apply a 5% discount; otherwise,
no discount is applied. Display the final payable amount.

Input:
Cart Value = 6000
User Type = Premium

Output:
Final Amount = 4800
"""
"""
cart_value = int(input("enter cart value "))
user_type = input(" enter user type")

if cart_value>=5000 :
     if user_type == "premium" :
        discount = cart_value * 20/100
        total_amount = cart_value - discount
        print("Total amount", total_amount)
     else :
        discount = cart_value *10/100
        total_amount = cart_value - discount
        print("Total amount", total_amount)
else:
     if cart_value >=2000:
        discount = cart_value*5/100
        total_amount = cart_value - discount
        print("Total amount", total_amount)
     else:
        print(" No discount applied")
"""
"""
3. A smart electricity monitoring system categorizes usage levels for better energy management.
The system should take the number of units consumed as input. If the units are greater than or equal to 100, then check further.
 If the units are greater than or equal to 300, assign "High Usage". Otherwise, check again.
If the units are greater than or equal to 200, assign "Moderate Usage"; otherwise, assign "Normal Usage".
 If the units are less than 100, assign "Low Usage". Display the usage category.

Input:
Units = 220

Output:
Usage Category = Moderate Usage
"""
"""
units = int(input("enter cart units "))

if units >=100:
   if units >=300:
       print(" High usage")
   else :
       pass

       if units >=200:
              print(" Moderate usage")
       else:
              print(" normal usage") 

else :
   print(" Low usage")  
"""
"""
4. A gym provides personalized plans based on age, weight, and fitness goal.
The system should take age, weight, and goal (weight loss or muscle gain) as input.
 If the age is greater than or equal to 18, then check the weight. If the weight is greater than or
 equal to 80, then check the goal. If the goal is "weight loss", assign "Cardio Plan"; otherwise, assign
"Strength Plan". If the weight is less than 80, assign "General Fitness Plan". If the age is less than 18, display
 "Not Allowed". Display the recommended plan.

Input:
Age = 25
Weight = 85
Goal = weight loss

Output:
Plan = Cardio Plan
"""
"""
age = int(input("enter the age"))
weight = int(input(" enter the weight"))
goal = (input("enter the goal")) 

if age>=18 :
      if weight>=80 :
           if goal == "weightloss":
              print("Cardio plan")
           else :
              print("Strength Plan") 
      else:
        print("General fitness plan")
else:
  print("Not allowed")
"""
"""
5. An ATM system processes withdrawal requests. The system should take account balance,
 withdrawal amount, and PIN status (correct or incorrect) as input. If the balance is
greater than or equal to the withdrawal amount, then check the withdrawal limit.
If the withdrawal amount is less than or equal to 10000, then check the PIN.
 If the PIN is correct, display "Transaction Successful"; otherwise, display "Invalid PIN".
If the withdrawal amount exceeds 10000, display "Limit Exceeded". If the balance is less than the
 withdrawal amount, display "Insufficient Balance".

Input:
Balance = 20000
Withdrawal Amount = 8000
PIN = correct

Output:
Transaction Successful
"""
"""
balance = int(input("enter the balance"))
withdrawal_amount = int(input(" enter the withdrawal amount"))
PIN = (input("enter the PIN"))

if balance>= withdrawal_amount :
      if withdrawal_amount <= 10000 :
            if PIN == "correct":
                   print("Transaction successfull")
            else :
                   print("Invalid PIN")
      else:
        print(" limit exceeded")
else:
   print("Insufficient balance")
"""
"""
6. A movie theatre calculates ticket prices based on age, show time, and day type.
 The system should take age, show time (morning/evening), and day type (weekday/weekend) as input.
If the age is less than 18, then check the show time. If the show time is morning, ticket price is 100; otherwise, ticket price is 150.
 If the age is 18 or above, then check the show time. If the show time is evening,
then check the day type. If it is weekend, ticket price is 300; otherwise, 250.
 If the show time is not evening, ticket price is 200. Display the ticket price.

Input:
Age = 25
Show Time = evening
Day = weekend

Output:
Ticket Price = 300
"""
"""
age = int(input("enter the age"))
show_time = (input(" enter the show time"))
day = (input("enter the day"))

if age<18 :
     if show_time == "morning":
           print(" Ticket price is 100")
     else:
           print("ticket price is 150")
else:
     if show_time =="evening":
         if day =="weekend":
            print("ticket price is 300")
         else:
            print("ticket price is 250")
     else:
            print("ticket price is 200")
"""
"""
7. A company calculates employee bonuses based on experience,
 performance rating, and salary. The system should take experience (in years), rating, and salary as input.
If the experience is greater than or equal to 5, then check the rating. If the rating is greater than or equal to 4, then check the salary.
 If the salary is less than 50000, assign a 20% bonus; otherwise, assign a 10% bonus. If the rating is less than 4, assign a 5% bonus.
 If the experience is less than 5, no bonus is given. Display the bonus amount.

Input:
Experience = 6
Rating = 4
Salary = 40000

Output:
Bonus = 8000
"""
"""
experience = int(input("enter the experience"))
rating = int(input(" enter the rating"))
salary = int(input("enter the salary"))

if experience>=5 :
     if rating >= 4:
          if salary <= 50000:
              bonus= salary*20/100
              print("Bonus",bonus)
          else:
              bonus= salary* 10/100
              print("Bonus",bonus)
     else:
        bonus= salary*5/100
        print("Bonus",bonus)
else:
   print("no bonus")
"""
"""
8. A warehouse management system needs to identify the highest stock level among six different storage units to prioritize dispatch.
 The system should take the quantity of items stored in six units as input. It should compare all six values using nested conditions
 and determine which unit has the maximum stock. Display the highest stock value among all six units.

Input:
Unit1 = 120
Unit2 = 450
Unit3 = 300
Unit4 = 275
Unit5 = 500
Unit6 = 390

Output:
"""
u1= int(input("enter unit 1"))
u2= int(input("enter unit 2"))
u3= int(input("enter unit 3"))
u4= int(input("enter unit 4"))
u5= int(input("enter unit 5"))
u6= int(input("enter unit 6"))

if u1>u2 :
      if u1>u3:
           if u1>u4:
               if u1>u5:
                    if u1>u6:
                         print("unit1 is greater")
                    else:
                         print(" unit6 is greater")
               else:
                    print("unit5 is greater")
           else :
                print("unit4 is greater")
       else:
            print("unit3 is greater") 
else:
    print("unit2 is greater")

if u2>u3 :
       if u2>u4:
               if u2>u5:
                    if u2>u6:
                         print("unit2 is greater")
                    else:
                         print(" unit6 is greater")
               else:
                    print("unit5 is greater")
           else :
                print("unit4 is greater")
else:
   print("unit3 is greater")    

if u3>u4 :
      
         if u3>u5:
              if u3>u6:
                  print("unit3 is greater")
              else:
                  print(" unit6 is greater")
         else:
                  print("unit5 is greater")
           
else:
   print("unit4 is greater") 

if u4>u5:
      print("unit4 is greater")
else:
      print("unit5 is greater")

if u5>u6:
      print("unit5 is greater")
else:
      print("unit6 is greater ")

             
   
  
      

           


         
            








     