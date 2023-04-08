# # Create a program to buy donut from DodoDonut's
# ### When opened, the program will show:

#   Welcome, DodoDonut's here!\
  
#   What would you like to do?
#   1. View Menu
#   2. Order Donut(s)
#   3. View All Order
#   4. Finish Order
#   5. Quit
#   Input (1..4): _

# ### When user choose 1, show:

#   DodoDonut's
#   MENU
  
#   Basic Donuts @IDR 7,000
#   1. Chocolate Donut
#   2. Strawberry Donut
#   3. Cheese Donut

#   Signature Donuts @IDR 9,000
#   1. Tiramisu Donut
#   2. Matcha Donut
#   3. Opera Donut
#   4. Vla Donut

#   Queen's Brunch Donuts @IDR 12,000
#   1. Sakura Donut
#   2. Dark Chocolate & Cream Donut
#   3. Chocolava Donut
#   4. Red Velvet Donut
#   5. Unicorn Donut
       
#   --------------------------------------------------------------------------

# ### When user choose 2:
#   - there's only 20 tables in the store. Check if there's an empty table and use the first available number
#   - ask user to input their name
#     * name should only contains letters & space with a minimum of 3 letters
#   - show the user's table number 
#   - ask user to input chosen menu
#     * user should type the chosen menu, case insensitive
#     * ask them to input the order quantity
#     * user should be able to input as many order as possible until user input 'done'
#   - show user the chosen menu prices, service tax (10%) and grand total (chosen menu price + service tax)

# ### When user choose 3, show
#   - The list of booked tables, booking name, and total

# ### When user choose 4, show:
#   The list of booked tables, booking name, and total
#   - Ask them to input the table number's order they want to finish
#   - Ask them whether they're sure to finish the booking
#     * if yes, finish the booking
#     * if no, do not do anything

# ### When user choose 5, show 
#   - a thank you screen and close the program

donut_menu = [["Chocolate Donut", 7000],["Strawberry Donut", 7000],["Cheese Donut", 7000],["Tiramisu Donut", 9000],["Matcha Donut", 9000],["Opera Donut", 9000],["Vla Donut", 9000],["Sakura Donut", 12000],["Dark Chocolate & Cream Donut", 12000],["Chocolava Donut", 12000],["Red Velvet Donut", 12000],["Unicorn Donut", 12000]]

item_name = 0
item_price = 1
  
cart = []
cart_item = 0
cart_quantity = 1
    
def show_menu(donut_menu):
  for idx in range(len(donut_menu)):
    print(f"{idx + 1}. {donut_menu[idx][item_name]} (Rp {donut_menu[idx][item_price]})")
    
def total_amount(donut_menu, cart):
  price = 0
  for idx in range(len(cart)):
    cart_item_idx = cart[idx][cart_item]
    price_per_item = donut_menu[cart_item_idx][item_price]
    quantity = cart[idx][cart_quantity]
    price = price + (price_per_item * quantity)
    tax = price*0.1
    total_price = price + tax
  return total_price


tables = [[1,[ ]],[2,[ ]],[3,[ ]],[4,[ ]],[5,[ ]],[6,[ ]],[7,[ ]],[8,[ ]],[9,[ ]],[10,[ ]],[11,[ ]],[12,[ ]],[13,[ ]],[14,[ ]],[15,[ ]],[16,[ ]],[17,[ ]],[18,[ ]],[19,[ ]],[20,[ ]]]

table_num = 0
booking_name = 1

orders = []

#orders = [[1,[]],[2,[]],[3,[]],[4,[]],[5,[]],[6,[]],[7,[]],[8,[]],[9,[]],[10,[]],[11,[]],[12,[]],[13,[]],[14,[]],[15,[]],[16,[]],[17,[]],[18,[]],[19,[]],[20,[]]]

table_num = 0
donut_order = 1

cart = []

def show_table(tables):
  for x in tables:
    print(x)

print("Welcome Dodonut's here!")
print("Available tables")
print(tables)
table_order = int(input("Input (available number): ")) - 1
booking_name = input("Please input your name: ")
print("\nWhat would you like to buy today?")
show_menu(donut_menu)
is_exit = False

# While do
while not is_exit:
  donut_order = int(input("Input: ")) - 1
  product_name = donut_menu[donut_order][item_name]
  quantity = int(input(f"How many {product_name} would you like to buy? "))
    
  total = 0
  cart.append([donut_order, quantity])
  total += total_amount(donut_menu, cart)
  buy_again_choice = input("Do you want to buy something else? (yes/no): ")
  if buy_again_choice == "no":
    is_exit = True

print("\nConfirming order")
print("Customer name: ", booking_name)
print("For table number: ", table_order + 1)
orders.append([table_order + 1, booking_name])
print(orders)
print("Thank you for purchasing! Your total is Rp", int(total))

finish = input("Are you sure? (yes/no): ")
if finish == "yes":
  print("Booked succesfully!")
  print("Thank you!")
elif finish == "no":
  None
else:
  None
