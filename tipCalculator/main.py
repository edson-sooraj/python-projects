#Greetings
print("Welcome to the tip calculator!")
#Total amount input
bill = float(input("What was the total bill?\n$"))
#Tip offer
tip = int(input("How much tip would you like to give? 10, 12, or 15?\n$"))
#Dividing the bill with n people
people = int(input("With how many people you will split the bill?\n"))
#Calculation
bill_with_tip = tip / 100 * bill + bill

#Divide the total bill with number of people
bill_per_person = bill_with_tip / people
#final amount
final_amount = round(bill_per_person, 2)
final_amount = "{:.2f}".format(bill_per_person)
#Amount each person has to pay
print(f"Each person should pay ${final_amount} ")
