def safe_divide(balance, num_people):
    try :
        return f'{balance / num_people:.1f}'
    except ZeroDivisionError:
        return "num_people cannot be zero!!!"

print(safe_divide(1000, 0.05))
print(safe_divide(1000, 0))


while True:
    balance_input = (input("Enter a balance or enter exit to quit->  "))
    if balance_input.lower() == "exit":
        break
    people_input = (input("Enter a number of people or enter exit to quit->  "))
    if people_input.lower() == "exit":
        break
    try:
        balance = int(balance_input)
        people = int(people_input)
        print('safe_divide is :', safe_divide(balance, people))
    except ValueError:
        print("you have to enter numbers only!!!")
        continue

