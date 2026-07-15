'''
1.Email Username Validator

A company wants to check whether an employee email username is valid before creating an official account.

Conditions:
- Username should start with a letter
- Username can contain letters, digits, underscore (_)
- No spaces allowed
- Length should be between 5 and 12 characters

Input:
Enter username: ajay_123

Output:
Valid Username
'''
'''
s= input("Enter username : ")
length = len(s)

if 5>= length <=12 :
      print("Invalid Username")
else:
    x=0
    
    if 65<= ord(s[0])<=90 or 97<= ord(s[0])<= 122 :
     for i in range(0,length) :
       
       if s[i] in '1234567890' or s[i] == '_' or 65<= ord(s[i]) <=90 or 97<= ord(s[i])<= 122:
             continue
       else:
             x=1
             break
     if x==1 :
         print("Invalid  Username")
     else:
         print("Valid username")
'''

'''
s= input("Enter Username :").lower()
letter=0
username=0
space=0
length=0

for ch in s:
      if len(s)>=5 and len(s)<=12 :
            length=1
      if s[0].isalpha():
            letter=1
      if ch.isalnum() or ch=='_' :
            username =1
      if ch==' ':
            space=1
      
print("length",length)
print("letter",letter)
print("username",username)
print("space",space)


if letter ==1 and username==1 and space==0 and length==1:
         print("Valid username")
else:
         print("invalid username")
'''
'''
2.
Mobile Number Digit Counter

A telecom company wants to count how many digits are present in a customer contact number entered with spaces or symbols.

Input:
Enter contact number: +91 98765-43210

Output:
Total digits: 12
'''
'''
s= input("Enter contact number")
count=0

for i in s:
     if i.isdigit():
         count+=1
     if i==' ':
         count=count
     else:
         count= count
print("Total digits :",count)
'''
'''
s= input("Enter contact number =")


count=0
i=0
while i<len(s):
        
   if s[i] in '1234567890':
         count= count+1
   elif s[i] == ' ' and s[i] in '@!#$%^&*+-':
        count = count
   i+=1
print("Total digits :", count)

'''
'''
3.
Word Counter in Complaint Message

A customer care system wants to count how many words are present in a complaint message.

Input:
Enter complaint: Delivery was delayed again today

Output:
Total words: 5
'''
'''
s= input('Enter Complaint :')
count=0
st= ' '
i=0
while i<len(s):
       st=(s.strip())
       if s[i] == ' ' :
          count= count+1
       else:
          count= count
       i+=1
print("Total Words ",count+1)

'''

'''
4.
Employee ID Validator

A company wants to validate employee IDs before storing them in the database.

Conditions:
- ID must start with "EMP"
- Total length should be 8
- Remaining characters should be digits only

Input:
Enter Employee ID: EMP10234

Output:
Valid Employee ID
'''
'''
s= input('Enter employee ID :').upper()
emp=0
length=0
digit=0
i=0
while i<len(s):
     if s[0]=='E' and s[1]=='M' and s[2]=='P':
           emp=1
     if len(s)==8 :
           length=1
     if s[i] in '1234567890':
           digit=1
     i+=1
if emp==1 and length ==1 and digit ==1 :
         print('Valid Employee Id')
else:
         print('Invalid Id')
'''

'''
s= input("Enter Employee ID :")
start=0
length=0
digit=0

for i in s:
     if s.startswith("EMP"):
             start=1
     if len(s)==8:
             length=1
     if i.isdigit():
             digit+=1
     
print("start",start)
print("length",length)
print("digit",digit)

if start==1 and length==1 and digit==5 :
       print("Valid Employee ID")
else:
       print("Invalid")
'''
'''
5.
Palindrome Product Code Checker

A factory wants to identify whether a product code reads the same forward and backward.

Input:
Enter product code: MADAM

Output:
Palindrome Code

Input:
Enter product code: PRODUCT

Output:
Not a Palindrome Code
'''
'''
s= input("Enter Product code :").lower()
temp=s
rev=' '
for i in s:
    rev=(s[::-1])

if temp==rev :
    print("Palindrome code")
else:
    print("Not a Palindrome code")
'''
'''
6.

Product Code Verification System

An e-commerce company wants to verify whether two product codes are rearranged versions of each other.

Conditions:
- Ignore spaces
- Ignore case sensitivity

Input:
Enter first product code: Dormitory
Enter second product code: Dirty Room

Output:
Both Product Codes are Matching
'''
'''
s1 = input('Enter first code :').lower()
s2= input('Enter second code :').lower()

if len(s1)!= len(s2):
       print('Both Product codes Do not match')

else:
  
  x=1
  space =0
  i=0
  while i<len(s1):
        count1 =0
        count2 =0
        j=0
        while j<len(s1):
            if s1[i]==s1[j]:
               
               count1 = count+1
            else:
               count1=count1
               j+=1
        k=0
        while k<len(s2):
            if s1[j]== s2[k]:
                
                count2 = count+1
            else:
               count2=count2
               k+=1
        if count1 != count2 :
               x=0
               break
        else:
              
              continue
        i+=1
  if x==1 and space == 0:
     print("Both Product Codes are Matching")
  else:
     print("Not Matching")

'''

'''
7.
Smart City Citizen Information Formatter

The Smart City Management Department is developing a digital portal to store citizen information in a professional format. Many citizens enter their details using small letters, uppercase letters, mixed casing, or numbers, which creates problems while generating official documents like ID cards, electricity bills, tax records, certificates, and address proofs.

To solve this issue, the department wants a program that automatically converts only the first character of every word into uppercase while keeping the remaining characters unchanged.

The input may contain:
- Words already written in uppercase
- Mixed-case words
- Numbers
- Address details
- Department names
- City names

Task:
Read a complete string from the user and convert the first character of every word into uppercase.

Conditions:
- Words may contain spaces between them
- Do not use built-in title() function
- Digits should remain unchanged

Input:
Enter citizen information:
deepika padukone from smart city raisen madhya pradesh

Output:
Formatted Information:
Deepika Padukone From Smart City Raisen Madhya Pradesh


Test Case 2:
Input:
Enter citizen information:
DEEPIKA pADukone ward number 12

Output:
Formatted Information:
DEEPIKA PADukone Ward Number 12


Test Case 3:
Input:
Enter citizen information:
government engineering college bhopal zone 3

Output:
Formatted Information:
Government Engineering College Bhopal Zone 3


Test Case 4:
Input:
Enter citizen information:
python FULL stack developer batch 18

Output:
Formatted Information:
Python FULL Stack Developer Batch 18

'''
'''
s= input('Enter citizen information :')

result=' '
i=0
while i <len(s):
      ch=s[i]
      if (i==0 or s[i-1]==' ') and ch>='a' and ch<='z' :
           result= result+ chr(ord(ch)-32)
          
      else:
          result=result + ch         
      i+=1

print(result)
'''
'''
8.
Airport Passenger Name Formatting System

An international airport is developing an automated passenger management system. Many passengers enter their details in different formats such as lowercase, uppercase, mixed-case letters, and numbers while booking flight tickets online.

Due to inconsistent formatting, problems occur while generating boarding passes, security verification records, and passenger identity reports.

To solve this issue, the airport authority wants a program that automatically converts only the first character of every word into uppercase while keeping all remaining characters unchanged.

The input may contain:
- Passenger names
- Passport details
- Terminal names
- Seat numbers
- City names
- Mixed uppercase/lowercase letters
- Digits

Task:
Read a complete string from the user and convert the first character of every word into uppercase.

Conditions:
- Words may contain spaces
- Digits should remain unchanged
- Do not use built-in title() function

Input:
Enter passenger details:
deepika padukone flight ai202 terminal 3 mumbai

Output:
Formatted Details:
Deepika Padukone Flight Ai202 Terminal 3 Mumbai


Test Case 2:
Input:
Enter passenger details:
DEEPIKA pADukone gate number 12

Output:
Formatted Details:
DEEPIKA PADukone Gate Number 12


Test Case 3:
Input:
Enter passenger details:
international departure terminal delhi airport

Output:
Formatted Details:
International Departure Terminal Delhi Airport


Test Case 4:
Input:
Enter passenger details:
business class passenger seat b12

Output:
Formatted Details:
Business Class Passenger Seat B12
'''
'''
s= input("Enter Passenger details :")
result= ' '
i=0
while i<len(s):
      ch= s[i]
      if (i==0 or s[i-1]==' ') and ch>='a' and ch<='z':
             result = result + chr(ord(ch)-32)

      else:
            result= result +ch
      i+=1
print(result)

'''
