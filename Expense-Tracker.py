expenses = [] 

try:
    with open("expenses.txt", "r") as file:
        for line in file:
            name,amount = line.strip().split(",")
            expenses.append([name,int(amount)])

except FileNotFoundError:
    pass
while True:
    expense = input("Enter expense name:")
    amount = int(input("Enter amount:")) 
    
    expenses.append([expense,amount]) 
    
    more = input("Add another expense?(yes/no):") 
    
    if more == "no":
        break
    
print("\nYour expenses:")

for expense in expenses:
    print(expense[0], ":", expense[1]) 
    
total = 0

for expense in expenses:
    total += expense[1] 
    
print("Total expense:", total)
    
with open("expenses.txt", "w") as file:
    for expense in expenses:
        file.write(expense[0] + "," + str(expense[1]) + "\n")