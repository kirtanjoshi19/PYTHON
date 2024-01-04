# Create an empty dictionary called dog
dog = {}

# Add name, color, breed, legs, age to the dog dictionary
dog['name'] = 'Raja'
dog['color'] = 'Brown'
dog['breed'] = 'Labrador'
dog['legs'] = 4
dog['age'] = 3

# Create a student dictionary
student = {
    'first_name': 'Arun',
    'last_name': 'Kumar',
    'gender': 'Male',
    'age': 20,
    'marital_status': 'Single',
    'skills': ['Machine Learning', 'Data Analysis', 'Web Development'],
    'country': 'India',
    'city': 'Mumbai',
    'address': '123 Main Street'
}

# Get the length of the student dictionary
student_length = len(student)

# Get the value of skills and check the data type, it should be a list
skills_value = student['skills']
skills_type = type(skills_value)

# Modify the skills values by adding one or two skills
student['skills'].extend(['Artificial Intelligence', 'Python Programming'])

# Get the dictionary keys as a list
keys_list = list(student.keys())

# Get the dictionary values as a list
values_list = list(student.values())

# Change the dictionary to a list of tuples using items() method
items_list = list(student.items())

# Delete one of the items in the dictionary
del student['marital_status']

# Delete one of the dictionaries
del dog
