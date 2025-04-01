print("Welcome! To Expense Calculator Program Designed for Students")
print("--"*30)
print("Lets First Calculate: Income Source")

Allowance = float(input("Enter the Monthly Allowance from Family: "))
Part_time_Job = float(input("Enter the Part-time Job Income: "))
Scholarships = float(input("Enter the amount received from Scholarships/Grants: "))
Savings = float(input("Enter the Savings/Investments avaiable: "))
Total_Income = Allowance + Part_time_Job + Scholarships + Savings

print("--"*30)
print("Now, lets calculate the Fixed Expenses")

Rent = float(input("Enter the cost of PG/Hostel: "))
Electricity = float(input("Enter the cost of Electricity Bill: "))
Water = float(input("Enter the Water Bill: "))
Mobile = float(input("Enter the Mobile/Internet Bill: "))
Insurance = float(input("Enter the cost of Health/Rental Insurance: "))
Total_Fixed_Expenses = Rent + Electricity + Water + Mobile + Insurance

print("--"*30)
print("Now, its the time to calculate the Variable Expenses")

Groceries = float(input("Enter the cost of Monthly Groceries: "))
Dining_Food = float(input("Enter the Dining out/Food Delivery cost: "))
Entertainment = float(input("Enter the Movies/Games/Streaming Services, etc. Cost: "))
Shopping = float(input("Enter the cost of Shopping (Clothes,Accessories,etc. ): "))
Personal_Care = float(input("Enter the cost of Gym,Salon,etc. : "))
Total_Variable_Expenses = Groceries + Dining_Food + Entertainment + Shopping + Personal_Care

print("--"*30)
print("Time to Calculate the Academic Expenses")

Tuition_Fees = float(input("Enter the monthly cost of Tuition Fees: "))
Books = float(input("Enter the cost of Books & Study Materials: "))
Total_Academic = Tuition_Fees + Books

Total_Expenses = Total_Fixed_Expenses + Total_Variable_Expenses + Total_Academic

print("--"*30)
print("Final Report of the Student Living Expense Calculator")
print("Total Income: ",Total_Income)
print("Total Expense: ",Total_Expenses)

if Total_Income > Total_Expenses:
    print("Hurrah!!, We have some money left! ",Total_Income-Total_Expenses)
elif Total_Income == Total_Expenses:
    print("Budget accomplished Successfully!!!")
else:
    print("We are RUNNING OUT OF MONEY!! ",Total_Expenses-Total_Income)