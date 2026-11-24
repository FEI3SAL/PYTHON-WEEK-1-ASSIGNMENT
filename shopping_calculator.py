# Shopping Calculator Program

# Ask the user for item price and quantity
price = float(input("Enter the price of one item (KES): "))
quantity = int(input("How many items do you want? "))

# Calculate the total cost
total = price * quantity

# Display the shopping summary using an f-string
print(f"{quantity} items at KES {price:.2f} each = KES {total:.2f}")

print("Thank you for shopping!")