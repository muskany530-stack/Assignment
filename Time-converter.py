input_seconds = int(input(" Enter total seconds"))
hours = input_seconds // 3600
remaining= input_seconds % 3600
minutes = remaining // 60
seconds = remaining % 60
print(" hours :",hours," minutes :", minutes," seconds :", seconds)