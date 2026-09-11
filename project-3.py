def total_price(*args):
   return sum(args)
print('Total :', total_price())
print('Total :', total_price(10, 20, 5))
print('Total :', total_price(100))

def print_order(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_order(customer="Ali", item="Laptop", quantity=2)
print_order(customer="Sara", item="Phone")

def create_invoice(customer, *prices, tax_rate = 0.09, **extra_info):
        print("Sum_price:", sum(prices), "tax_rate:", tax_rate)
        print(f"Total_price_with_tax for {customer}:", sum(prices) + sum(prices) * tax_rate)
        for key, value in extra_info.items():
            print(f"{key}: {value}")
create_invoice("Ali", 100, 100, tax_rate=0.09)
create_invoice("Sara", 50,tax_rate=0.05, discount_code="SAVE10%")