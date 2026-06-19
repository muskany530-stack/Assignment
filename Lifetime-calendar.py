input_age = int(input(" enter age"))
days = input_age // 365
remaining= input_age %24
hours = remaining // 24
minutes= remaining //60
print(" You've lived Approximately ")
print( " Days:",days, " Hours :", hours, " Minutes", minutes)