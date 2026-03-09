print("Time to calculate that pizza price!")

# Ask for size
size = input("What size is that pizza (small or large): ").lower()

# Set base price per size
if size == "small":
    base_price == 8
elif size == "large":
    base_price = 12
else:
    print("That's not a size goofy, now you gotta start over!")
    exit()

# Ask for toppings
toppings = int(input("How many toppings ya want?: "))
topping_cost = toppings * 1

# Ask for distance
miles = float(input("How many miles away are ya?: "))

# Delivery fee calculation
if miles <= 5:
    delivery_fee = 2
else: 
    delivery_fee = 2 + (miles - 5) * 1

# Final calculation
total_cost = base_price + topping_cost + delivery_fee

# Display
print("\nWhat Ya Got")
print("Size:", size)
print("Base price $", base_price)
print("Topping cost:", topping_cost)
print("Delivery fee: $", delivery_fee)
print("Total cost: $", total_cost)