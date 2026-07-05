"""
1. Utility Toolkit System

You are developing a Utility Toolkit Application for a small office. Employees use this tool to quickly perform common number operations like checking prime numbers, reversing numbers, etc.

The system should be menu-driven and must continue running until the user selects Exit. All operations should be handled using match-case.

Menu Options:
1 → Check Prime Number
2 → Check Palindrome Number
3 → Reverse a Number
4 → Count Digits
5 → Exit

Sample Run 1:
Input:
Enter your choice: 1
Enter number: 7

Output:
7 is a Prime Number

Sample Run 2:
Input:
Enter your choice: 2
Enter number: 121

Output:
121 is a Palindrome Number

Sample Run 3:
Input:
Enter your choice: 3
Enter number: 456

Output:
Reversed Number is: 654

Sample Run 4:
Input:
Enter your choice: 4
Enter number: 98765

Output:
Total digits: 5

Sample Run 5 (Invalid Choice):
Input:
Enter your choice: 9

Output:
Invalid choice. Please try again.

Sample Run 6 (Exit):
Input:
Enter your choice: 5

Output:
Exiting program... Thank you!

Requirements:

* Use while loop to repeat menu
* Use match-case for decision making
* Handle negative numbers properly
* Use only loops and conditions
"""
"""
while True :
      print("1. check prime number")
      print("2. check palindrome number")
      print("3. reverse a number")
      print("4. count digits")
      print("5. exit")

      choice = int(input("enter your choice "))
      match choice :
             case 1 :

                n= int(input("n = "))
                flag =0
                for i in range(2,n):
                      if n% i ==0 :
                          flag= 1
                          break
                if flag ==0 :
                       print("prime number")
                else:
                       print("not prime ")

             case 2 :
             
                 n= int(input(" n ="))
                 temp =n
                 rev=0
                 for i in range(len(str(n))):
                        rev = rev*10 + n%10
                        n= n//10
                 if rev == temp:
                        print("palindrome number")
                 else:
                        print("not palindrome number")
             
             case 3 :
             
                 n= int(input(" n ="))
                 temp =n
                 rev=0
                 for i in range(len(str(n))):
                        rev = rev*10 + n%10
                        n= n//10 
                 print("reverse =",rev)

             case 4 :
                 n= int(input("n ="))
                 count =0
                 for i in range(len(str(n))):
                        r= n%10
                        count = count+1
                        n = n//10
                 print("Digit Count =", count)
             
             case 5 :
                 print("EXIT..")
                 break
      again = input(" Do u want to continue").lower()
      match again :
          
               case "yes":  
                     continue
               case "no" :
                     break
               case _:
                     print("Enter yes or no")
                     break

print("Thanks")

"""

"""
2.
 Employee Salary Processor

Scenario:
You are developing an Employee Salary Processing System for a company’s HR department. The system is used to manage and calculate employee salary details such as allowances, tax deductions, and final payable salary.

The HR staff may not always follow the correct sequence while using the system. For example, they might try to calculate net salary or tax before entering the basic salary. Your program must handle such situations properly.

👉 Important Condition:
If the Basic Salary is not entered, the system should display:
"Please enter basic salary first"
and should not perform any further calculations.

The system should be menu-driven and must continue running until the user selects Exit. All operations should be handled using match-case.

Menu Options:
1 → Enter Basic Salary
2 → Calculate HRA (20%) and DA (10%)
3 → Calculate Net Salary
4 → Tax Deduction

* Salary > 50000 → 10% tax
* Otherwise → 5% tax
  5 → Display Salary Slip
  6 → Exit

---

Sample Run 1:
Input:
Enter your choice: 3

Output:
Please enter basic salary first

---

Sample Run 2:
Input:
Enter your choice: 1
Enter Basic Salary: 40000

Output:
Basic Salary recorded successfully

---

Sample Run 3:
Input:
Enter your choice: 2

Output:
HRA: 8000
DA: 4000

---

Sample Run 4:
Input:
Enter your choice: 3

Output:
Net Salary (before tax): 52000

---

Sample Run 5:
Input:
Enter your choice: 4

Output:
Tax Deduction: 5200

---

Sample Run 6:
Input:
Enter your choice: 5

Output:
----- Salary Slip -----
Basic Salary: 40000
HRA: 8000
DA: 4000
Net Salary: 52000
Tax: 5200
Final Salary: 46800

---

Sample Run 7 (Invalid Choice):
Input:
Enter your choice: 9

Output:
Invalid choice. Please try again.

---

Sample Run 8 (Exit):
Input:
Enter your choice: 6

Output:
Exiting program... Thank you!

"""
"""

while True :
         print("1. Enter basic salary")
         print("2. calculate HRA (20%) and DA (10%)")
         print("3. calculate Net salary")
         print("4. Tax deduction")
         print("5. display salary slip")
         print("6. Exit" )

         choice= int(input("Enter your choice :"))
         match choice :
                 case 1 :
                      basic_salary= input("Enter basic salary")

                      if basic_salary == " " :
                          print("Please enter basic salary first ")

                      else:
                          print("Basic salary recorded successfully!!")
                
                 case 2:
                      basic_salary= input("Enter basic salary")

                      if basic_salary == " " :
                          print("Please enter basic salary first ")

                      else:
                         salary= int(input("Enter basic salary"))
                        
                         hra= salary *20 /100
                         da = salary *10/100
                         print("HRA = ",hra)
                         print("DA =", da) 

                 case 3 :
                      basic_salary= input("Enter basic salary")

                      if basic_salary == " " :
                           print("Please enter basic salary first ")

                      else:
                           salary= int(input("Enter basic salary"))
                           hra=salary *20 /100
                           da = salary *10/100
                           net_salary = hra+ da + salary
                           print("Net salary =" ,net_salary)
                      

                 case 4 :
                      basic_salary= input("Enter basic salary")

                      if basic_salary == " " :
                          print("Please enter basic salary first ")

                      else:
                           salary=int( input("Enter basic salary"))
                           hra=salary *20 /100
                           da = salary *10/100
                           net_salary = hra+ da + salary

                           if net_salary > 50000 :
                               tax = net_salary* 10/100
                               print("Tax =",tax)
                           else:
                               tax = net_salary* 5/100
                               print("Tax =", tax)

                 case 5:
                         print("-- Salary Slip --")
                         print("salary ", salary)
                         print("HRA ", hra)
                         print("DA ", da)
                         print("Net salary ", net_salary)
                         print("Tax ", tax)
                         print("Final salary =", net_salary - tax)
                
                 case 6:
                         print("Existing program ... thank u")
                 case __ :
                         print("invalid choice")
                         break

         again = input("Do u want to continue").lower()
         match again:
             
                  case " sure" :
                        continue
                  case " no":
                        break
                  case __ :
                        print("Invalid note")
                        break
print("DONE  ") 

"""


"""
3.

 Smart Banking System

Scenario:
You are developing a Smart Banking System for a bank to help customers perform basic banking operations such as deposit, withdrawal, balance checking, and interest calculation.

Sometimes, users may try to withdraw money or check balance before depositing any amount. Your system must handle such situations properly.

👉 Important Condition:
If no amount has been deposited yet, the system should display:
"No balance available. Please deposit first"
and should not allow withdrawal, balance check, or interest calculation.

The system should be menu-driven and must continue running until the user selects Exit. All operations should be handled using match-case.

Menu Options:
1 → Deposit Money
2 → Withdraw Money
3 → Check Balance
4 → Apply Interest

* Balance > 50000 → 5% interest
* Otherwise → 3% interest
  5 → Exit

---

Sample Run 1:
Input:
Enter your choice: 2

Output:
No balance available. Please deposit first

---

Sample Run 2:
Input:
Enter your choice: 1
Enter amount to deposit: 10000

Output:
Amount deposited successfully

---

Sample Run 3:
Input:
Enter your choice: 3

Output:
Current Balance: 10000

---

Sample Run 4:
Input:
Enter your choice: 2
Enter amount to withdraw: 15000

Output:
Insufficient balance

---

Sample Run 5:
Input:
Enter your choice: 4

Output:
Interest added: 300
Updated Balance: 10300

---

Sample Run 6:
Input:
Enter your choice: 2
Enter amount to withdraw: 5000

Output:
Withdrawal successful

---

Sample Run 7 (Invalid Choice):
Input:
Enter your choice: 9

Output:
Invalid choice. Please try again.

---

Sample Run 8 (Exit):
Input:
Enter your choice: 5

Output:
Exiting system... Thank you!

---
"""
"""

while True :
            print("1. Deposit Money")
            print("2. Withdraw Money")
            print("3. Check balance")
            print("4. Apply Interest")
            print("5. Exit")
 
            choice = int(input("enter a choice :"))
            match choice :
                   
                  case 1 :    
                         depo_money = input("enter amount to deposit")
                         if depo_money == " " :
                              print("No balance available ,please deposit first")
                         else :
                              print("Amount deposited successfully!!")
  
                  case 2:
                         depo_money = input("enter amount to deposit")
                         if depo_money == " " :
                              print("No balance available ,please deposit first")
                         else:
                             d_money = int(input("enter amount to deposit"))
                             w_money = int(input("enter amount to withdraw"))
                         

                             if w_money > d_money :
                               print("Insufficient balance")
                             else :
                               print("Withdrawal successful")
                  case 3 :
                         depo_money = input("enter amount to deposit")
                         if depo_money == " " :
                              print("No balance available ,please deposit first")
                         else :
                              balance =0
                              balance = d_money - w_money
                              print("Current Balance :", balance)
                  case 4 :
                         depo_money = input("enter amount to deposit")
                         if depo_money == " " :
                              print("No balance available ,please deposit first")
                         else :
                            if balance >50000:
                              print("Interest =", balance *5/100)
                            else :
                              print("Interest =", balance *3/100)
                  case 5 :
                          print("Existing system...")
                  case __ :
                          print("invalid choice.")
                          break

            again = input("Do u want to continue").lower()
            match again:
             
                  case " sure" :
                        continue
                  case " no":
                        break
                  case __ :
                        print("Invalid note")
                        break
print("DONE  ") 

"""


"""
4. Electricity Bill Management System

You are developing an Electricity Bill Management System for a power distribution company. The system helps calculate electricity bills for customers based on their unit consumption.

Sometimes, the operator may try to calculate the bill or apply surcharge before entering the number of units consumed. Your system must handle such situations properly.

👉 Important Condition:
If units are not entered, the system should display:
"Please enter units consumed first"
and should not perform further calculations.

The system should be menu-driven and must continue running until the user selects Exit. All operations should be handled using match-case.

Menu Options:
1 → Enter Units Consumed
2 → Calculate Bill Amount

* First 100 units → ₹5 per unit
* Next 100 units → ₹7 per unit
* Above 200 units → ₹10 per unit
  3 → Apply Surcharge
* If bill > 2000 → 10% surcharge
* Otherwise → 5% surcharge
  4 → Display Final Bill
  5 → Exit

---

Sample Run 1:
Input:
Enter your choice: 2

Output:
Please enter units consumed first

---

Sample Run 2:
Input:
Enter your choice: 1
Enter units consumed: 250

Output:
Units recorded successfully

---

Sample Run 3:
Input:
Enter your choice: 2

Output:
Bill Amount: 1700

(Explanation: 100×5 = 500, 100×7 = 700, 50×10 = 500 → Total = 1700)

---

Sample Run 4:
Input:
Enter your choice: 3

Output:
Surcharge: 85

---

Sample Run 5:
Input:
Enter your choice: 4

Output:
----- Final Bill -----
Units: 250
Bill Amount: 1700
Surcharge: 85
Total Payable: 1785

---

Sample Run 6 (Invalid Choice):
Input:
Enter your choice: 9

Output:
Invalid choice. Please try again.

---

Sample Run 7 (Exit):
Input:
Enter your choice: 5

Output:
Exiting system... Thank you!

---
"""
while True :
       print("1. enter units consumed")
       print("2. calculate bill amount")
       print("3. apply surcharge")
       print("4. display final bill")
       print("5. Exit")

       choice= int(input("enter the choice :"))
       match choice :
              
             case 1:
                  units= input("enter units consumed")
                  if units == " " :
                         print("Please enter units consumed first")
                  else :
                         print("Units recorded successfully")

             case 2 :
                   units= input("enter units consumed")
                   if units == " " :
                         print("Please enter units consumed first")
                   else :

                       u= int(input("enter unit consumed"))
                       if u<=100 :
                         bill = 5*100
                         print("bill amount =",bill )

                       elif u>100 and u <=200 :
                         bill = 5*100 +7*(u-100)
                         print("bill amount =",bill)

                       else:
                         bill = 5*100 + 7*100 + 10*(u -100)
                         print("bill amount =",bill)

             case 3 :
                     units= input("enter units consumed")
                     if units == " " :
                         print("Please enter units consumed first")
                     else :
                    
                       if bill >= 2000:
                           surcharge =bill* 10/100
                           print("surcharge =" ,surcharge )
                       else:
                           surcharge = bill* 5/100
                           print("surcharge =",surcharge )

             case 4:
                      
                      print("--- Final Bill ---")
                      print("Units :",u)
                      print("Bill Amount :",bill)
                      print("Surcharge :", surcharge)
                      print("Total payable :", bill + surcharge)
             case 5 :
                     print("Existing program...")
             case __ :
                     print("invalid choice ")
                     break

       again = input("Do u want to continue").lower()
       match again:
             
                  case " sure" :
                        continue
                  case " no":
                        break
                  case __ :
                        print("Invalid note")
                        break
print("DONE  ") 

              





























































     



























