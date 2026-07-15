'''
1.Vowel Counter in Customer Feedback

 A company wants to analyze customer feedback messages by counting how many vowels are present in the feedback.

Input: Enter feedback message: Hello Customer Service

Output: Total vowels: 8
'''
'''
s= input("enter string ")
count=0
for ch in s:
   if ch=='a' or ch=='e' or ch=='i' or ch=='o' or ch=='u' :
       count= count+1
print("Total Vowels = ", count)
'''

'''
2.
Space Counter in Chat Messages

A chat application wants to calculate how many spaces are used in a message.

Input: Enter chat message: Good morning everyone how are you

Output: Total spaces: 5
'''
'''
s= input("enter chat message ")
count=0
i=0
while i<len(s):
      if s[i-1]== " ":
          count=count+1
      i+=1
print("Total spaces =", count)

'''
'''

3.
Character Occurrence Checker in Product Review

An e-commerce website wants to know how many times a particular character appears in a product review.

Input: Enter product review: this product is really good Enter character to check: o

Output: Character 'o' occurs: 4 times
'''
'''
s= input("enter string ").lower()
i=0
while i<len(s):

   i+=1
print(s.count("o"))

'''
'''
4.
Consonant Counter in Student Name Record

A school management system wants to count how many consonants are present in student names.

Input: Enter student name: Ajay Singh Thakur

Output: Total consonants: 11

NOTE:

Ignore case sensitivity (treat A and a same)
Consider only English alphabets for vowel/consonant counting
Vowels: A, E, I, O, U
'''
'''
s= input("enter string ").lower()
count=0
for ch in s :
     if ch=='a' or ch=='e' or ch=='i' or ch=='o' or ch=='u':
         count= count
     elif ch == ' ':
         count=count
     else:
         count=count+1
print("Total consonants =", count)
'''

'''
5.
Advanced Password Security Checker

A cyber security company wants to verify whether employee passwords are highly secure before giving system access.

Conditions: Password must:

Start with an uppercase letter
End with a digit
Contain at least 2 digits
Contain at least 1 special character (@ # $ % & *)
Must not contain spaces
Length should be between 8 and 15 characters

Input: Enter password: Python@45

Output: Secure Password
'''
'''
s= input(" enter password :")

upper=0
end_digit=0
digit=0
special=0
space =0
length=0
for ch in s :
       

       
       if len(s)>=8 and len(s)<=15 :
              length=1

       if s[0] .isupper():
              upper=1

       if s[-1].isdigit():
              end_digit=1

       if ch.isdigit():
              digit= digit+1

       if ch== ' ':
              space= 1

       elif not ch.isalnum():
              special =1

if length ==1 and upper ==1 and digit>=2 and end_digit ==1 and space ==0 and special == 1:
           print('Valid password')
else:
           print('Invalid Password') 
'''
'''
6.
Railway Ticket PNR Analyzer

A railway department wants to verify whether a PNR number is valid.

Conditions:
- PNR must start with "PNR"
- Total length should be 12 characters
- Remaining characters should be digits

Input:
Enter PNR: PNR123456789

Output:
Valid PNR Number
'''
'''
s= input("Enter PNR :")
length=0
start_digit=0
digit=0

for ch in s:
         if len(s)<=12 :
                length=1
         if s.startswith("PNR"):
                start_digit=1
         elif ch.isdigit():
                digit=digit + 1
         else:
                digit= digit

if length ==1 and start_digit ==1 and digit<=9 :
           print("Valid PNR Number")
else:
           print("Not Valid ")
'''
'''
7.
Vehicle Number Plate Checker

The traffic department wants to validate vehicle registration numbers.

Conditions:
- First 2 characters should be alphabets
- Next 2 should be digits
- Total length should be 10

Input:
Enter vehicle number: MP04AB1234

Output:
Valid Vehicle Number
'''
'''
s= input("Enter Vehicle number :").upper()
index =0
sec_index =0
third_index =0
four_index =0
length=0

for ch in s:
       if s[0].isalpha():
             index=1
       if s[1].isalpha() :
             sec_index =1
       if s[2].isdigit() :
             third_index =1
       if s[3].isdigit() :
             four_index =1
       if len(s)==10:
             length=1
       else:
             print("Invalid vehicle number")

print("index =", index)
print("sec_index =", sec_index)
print("Third index =", third_index)
print("fourth index =", four_index)

if index==1 and sec_index==1 and third_index==1 and four_index==1 and length==1 :
        print(" Valid Vehicle Number")
else:
        print("Not Valid ")
'''