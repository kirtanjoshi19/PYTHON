# Create an empty tuple
empty_tuple = ()

# Create a tuple containing names of sisters and brothers
sisters = ('Aisha', 'Sonia')
brothers = ('Rahul', 'Amit')

# Join brothers and sisters tuples and assign it to siblings
siblings = brothers + sisters

# How many siblings do you have?
num_siblings = len(siblings)

# Modify the siblings tuple and add the name of your father and mother
father_name = 'Rajesh'
mother_name = 'Sarita'
family_members = (father_name, mother_name) + siblings

# Displaying the results
print("Empty Tuple:", empty_tuple)
print("Sisters:", sisters)
print("Brothers:", brothers)
print("Siblings:", siblings)
print("Number of Siblings:", num_siblings)
print("Family Members:", family_members)
