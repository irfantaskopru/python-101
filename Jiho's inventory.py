""" Our friend Jiho has been so successful in both the flower and grocery business that she has decided to open a furniture store."""

#Jiho has compiled a list of inventory items into a list called inventory and wants to know a few facts about it.

inventory = ["twin bed", "twin bed", "headboard", "queen bed", "king bed", "dresser", "dresser", "table", "table", "nightstand", "nightstand", "king bed", "king bed", "twin bed", "twin bed", "sheets", "sheets", "pillow", "pillow"]

# First, how many items are in the warehouse? 
inventory_len = len(inventory)

# Select the first element in inventory
first = inventory[0]

# Select the last element from inventory
last = inventory[-1]

# Select items from the inventory starting at index 2 and up to, but not including, index 6.
inventory_2_6 = inventory[2:6]

# Select the first 3 items of inventory
first_3 = inventory[:3]

# How many 'twin bed's are in inventory?
win_beds = inventory.count("twin bed")

# Remove the 5th element in the inventory
removed_item = inventory[4]

# There was a new item added to our inventory called "19th Century Bed Frame".
inventory.insert(10,"19th Century Bed Frame")

# Sort inventory.
inventory = sorted(inventory)

# Print inventory.
print(inventory)



