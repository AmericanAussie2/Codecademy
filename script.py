lovely_loveseat_description = """
Lovely Loveseat. Tufted polyester
blend on wood. 32 inches high x 40 
inches wide x 30 inches deep. Red or
white.
""" 
# Price for loveseat
lovely_loveseat_price = 254.00
# Adding another piece of furniture
stylish_settee_description = "Stylish Settee. Faux leather on birch. 29.50 inches high x 54.75 inches wide x 28 inches deep. Black."
# Price for the Stylish Settee
stylish_settee_price = 180.50
# Last item before business
luxurious_lamp_description = "Luxurious Lamp.Glass and iron. 36 inches tall. Brown with cream shade."
luxurious_lamp_price = 52.15
# Calculating sales tax
sales_tax = .088
# Running tally of expenses
customer_one_total = 0
# List of descriptions of things they're purchasing
customer_one_itemization = ""

customer_one_total += lovely_loveseat_price
customer_one_itemization += lovely_loveseat_description

customer_one_total += luxurious_lamp_price
customer_one_itemization == luxurious_lamp_description

customer_one_tax = customer_one_total * sales_tax
customer_one_total += customer_one_tax

print("Customer One Items:")
print(customer_one_itemization)
print("Customer One Total:")
print(customer_one_total)

customer_two_total = 0


