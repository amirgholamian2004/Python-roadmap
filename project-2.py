warehouse = [[12, 0, 5, 8], [3, 15, 0, 7], [0, 0, 9, 20] ]
#each list is for one shelf in the warehouse.
#each number is the amount of products in a row.
total = 0
empty_slots = 0
most_inventory = 0
for shelf_index, shelf in enumerate(warehouse):
    for row_index, value in enumerate(shelf) :
        total += value
        if value == 0 :
           empty_slots += 1
        if value > most_inventory:
            most_inventory =  value
            most_inventory_shelf_number = shelf_index
            most_inventory_product_row_number = row_index

print(f" Total inventory is: {total}")
print(f" Number of Empty slots are: {empty_slots}")
print(f" Number of Most Inventory is: {most_inventory}")
print(f" in shelf: {most_inventory_shelf_number}, row: {most_inventory_product_row_number}")

while True:
    answer = input("Enter shelf number(or enter DONE to exit): ")
    shelf_number = int(answer)
    if answer == "DONE" or answer == "done":
        break
    if not answer.isdigit():
        print("Please enter a valid shelf number!")
        continue
    if shelf_number <= 0 or shelf_number > len(warehouse):
        print("Please enter a valid shelf number!")
        continue

    print(f"Shelf number: {shelf_number}", warehouse[shelf_number-1])


