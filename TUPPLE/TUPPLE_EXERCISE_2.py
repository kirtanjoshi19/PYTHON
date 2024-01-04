

# Create fruits, vegetables, and animal products tuples
fruits = ('Apple', 'Banana', 'Orange')
vegetables = ('Carrot', 'Spinach', 'Broccoli')
animal_products = ('Chicken', 'Eggs', 'Milk')

# Join the three tuples and assign it to a variable called food_stuff_tp
food_stuff_tp = fruits + vegetables + animal_products

# Change the food_stuff_tp tuple to a food_stuff_lt list
food_stuff_lt = list(food_stuff_tp)

# Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list
middle_index = len(food_stuff_lt) // 2
middle_item_tp = food_stuff_tp[middle_index]
middle_items_lt = food_stuff_lt[middle_index-1:middle_index+2]

# Slice out the first three items and the last three items from food_stuff_lt list
first_three_items_lt = food_stuff_lt[:3]
last_three_items_lt = food_stuff_lt[-3:]

# Delete the food_stuff_tp tuple completely
del food_stuff_tp

# Check if an item exists in tuple
nordic_countries = ('Denmark', 'Finland', 'Iceland', 'Norway', 'Sweden')

# Check if 'Estonia' is a nordic country
estonia_check = 'Estonia' in nordic_countries

# Check if 'Iceland' is a nordic country
iceland_check = 'Iceland' in nordic_countries

# Displaying the results


print("First Three Items from List:", first_three_items_lt)
print("Last Three Items from List:", last_three_items_lt)
print("Estonia is a Nordic Country:", estonia_check)
print("Iceland is a Nordic Country:", iceland_check)
