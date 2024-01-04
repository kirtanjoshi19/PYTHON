# Declare an empty list
list1 = list()


# Declare a list with more than 5 items
lng = ['java','ruby','c#','express','python']


# Find the length of your list
# print(len(lng))


# Get the first item, the middle item and the last item of the list
firstitem = lng[0]
# print(firstitem)

middleitem = len(lng)//2
middleitem = lng[middleitem]
# print(middleitem)

lastitem = len(lng)-1
lastitem = lng[lastitem]
# print(lastitem)
# Declare a list called mixed_data_types, put your(name, age, height, marital status, address)4
mixed_data_types = {
    "name":"kirtan",
    "age":21,
    "height":6.1,
    "marital status":"Single",
    "address":"Prince Hostel"
}
# print(mixed_data_types)
# Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.
it_companies = ['Facebook','Google','Microsoft','Apple','IBM','Oracle','Amazon']


# Print the list using print()
# print(it_companies)


# Print the number of companies in the list
# print('The Number of IT Companies is:',len(it_companies))


# Print the first, middle and last company
firstcom = it_companies[0]
# print(firstcom)


middlecom = len(it_companies)//2
middlecom = it_companies[middlecom]
# print(middlecom)

lastcom = len(it_companies)-1
lastcom = it_companies[lastcom]
# print(lastcom)

# Add an IT company to it_companies
# it_companies.append('Infosys')            


# Insert an IT company in the middle of the companies list
middlecom = len(it_companies)//2
it_companies.insert(middlecom,'Tata')


# Change one of the it_companies names to uppercase (IBM excluded!)
temp = it_companies[7].upper()

# Join the it_companies with a string '#;  '
join = '#;'.join(it_companies)
print("Join:",join)

# Check if a certain company exists in the it_companies list.
if 'Samsung' in it_companies:
    print("\nSamsung is in the list of IT companies.")
else:
    print("\nSamsung is not in the list of IT companies.")

# Sort the list using sort() method
it_companies=['Facebook','Google','Microsoft','Apple','IBM','Oracle','Amazon']
it_companies.sort()
# print("\nSorted:",it_companies)

# Reverse the list in descending order using reverse() method
it_companies.reverse()
# print("\nReverse:",it_companies)

# Slice out the first 3 companies from the list
# print("\nSlice:",it_companies[0:3])

# Slice out the last 3 companies from the list
# print("\nSlice from last:",it_companies[-3::])

# Slice out the middle IT company or companies from the list
if len(it_companies)%2!=0:
    print("\nSlice from middle:",it_companies[len(it_companies)//2])

# Remove the first IT company from the list
# print("\nPOP:",it_companies.pop(0))

# Remove the middle IT company or companies from the list
# print("\nPOP from middle:",it_companies.pop(len(it_companies)//2))

# Remove the last IT company from the list
# print("\nPOP from last:",it_companies.pop(-1))

# Remove all IT companies from the list
# print("\n",it_companies.clear())

# Destroy the IT companies list
# del it_companies

# Join the following lists:
# front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
# back_end = ['Node','Express', 'MongoDB']
back_end = ['Node','Express', 'MongoDB']
fullstack=front_end+back_end
# print("\n",fullstack)

# After joining the lists in question 26. Copy the joined list and assign it to a variable full_stack. Then insert Python and SQL after Redux.
fullstack.insert(fullstack.index('Redux') + 1, "Python")
fullstack.insert(fullstack.index('Redux') + 2, "SQL")
print("\n",fullstack)