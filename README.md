# Create a program to buy donut from DodoDonut's
### When opened, the program will show:

  Welcome, DodoDonut's here!\
  
  What would you like to do?
  1. View Menu
  2. Order Donut(s)
  3. View All Order
  4. Finish Order
  5. Quit
  Input (1..4): _

### When user choose 1, show:

  DodoDonut's
  MENU
  
  Basic Donuts @IDR 7,000
  1. Chocolate Donut
  2. Strawberry Donut
  3. Cheese Donut

  Signature Donuts @IDR 9,000
  1. Tiramisu Donut
  2. Matcha Donut
  3. Opera Donut
  4. Vla Donut

  Queen's Brunch Donuts @IDR 12,000
  1. Sakura Donut
  2. Dark Chocolate & Cream Donut
  3. Chocolava Donut
  4. Red Velvet Donut
  5. Unicorn Donut
       
  --------------------------------------------------------------------------

### When user choose 2:
  - there's only 20 tables in the store. Check if there's an empty table and use the first available number
  - ask user to input their name
    * name should only contains letters & space with a minimum of 3 letters
  - show the user's table number 
  - ask user to input chosen menu
    * user should type the chosen menu, case insensitive
    * ask them to input the order quantity
    * user should be able to input as many order as possible until user input 'done'
  - show user the chosen menu prices, service tax (10%) and grand total (chosen menu price + service tax)

### When user choose 3, show
  - The list of booked tables, booking name, and total

### When user choose 4, show:
  The list of booked tables, booking name, and total
  - Ask them to input the table number's order they want to finish
  - Ask them whether they're sure to finish the booking
    * if yes, finish the booking
    * if no, do not do anything

### When user choose 5, show 
  - a thank you screen and close the program
