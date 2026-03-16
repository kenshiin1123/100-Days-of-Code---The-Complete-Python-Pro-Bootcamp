total_bill, tip_to_give, total_people, each_person_should_pay = 0.0, 0.0, 0.0, 0.0
print("Welcome to the tip calculator!")
total_bill = float(input("What was the total bill? $"))
tip_to_give = float(input("How much tip would you like to give? %"))
total_people = float(input("How many people to split the bill? "))

each_person_should_pay = (float(total_bill) / int(total_people))
percent_to_add = tip_to_give / 100
each_person_should_pay = (percent_to_add * float(each_person_should_pay)) + each_person_should_pay
print(f"Each person should pay: ${each_person_should_pay:.2f}")