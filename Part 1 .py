# Define a function to distribute chocolates iteratively
def distribute_chocolates_iter(chocolates, students):
    # Check if there are enough chocolates for each student
    if len(chocolates) < len(students):
        return "Not enough chocolates to distribute to all students."

    # Initialize an empty dictionary to store the distribution
    distribution = {}
    # Iterate over each student and distribute one chocolate to each
    for i, student in enumerate(students):
        distribution[student] = chocolates[i]  # Assign a chocolate to the student

    return distribution


# Define a function to distribute chocolates recursively
def distribute_chocolates_recursive(chocolates, students, distribution=None):
    # Base case: If no more chocolates or students are left, return the distribution
    if distribution is None:
        distribution = {}
    if len(students) == 0 or len(chocolates) == 0:
        return distribution

    # Recursive step: Distribute chocolates to students
    chocolate = chocolates.pop(0)  # Take the first chocolate
    student = students.pop(0)  # Take the first student
    distribution[student] = chocolate  # Assign the chocolate to the student

    # Recursive call with updated lists
    return distribute_chocolates_recursive(chocolates, students, distribution)


# Define a function to distribute chocolates iteratively
def distribute_chocolates_iter(chocolates, students):
    # Check if there are enough chocolates for each student
    if len(chocolates) < len(students):
        return "Not enough chocolates to distribute to all students."

    # Initialize an empty dictionary to store the distribution
    distribution = {}
    # Iterate over each student and distribute one chocolate to each
    for i, student in enumerate(students):
        distribution[student] = chocolates[i]  # Assign a chocolate to the student

    return distribution


# Define a function to distribute chocolates recursively
def distribute_chocolates_recursive(chocolates, students, distribution=None):
    # Base case: If no more chocolates or students are left, return the distribution
    if distribution is None:
        distribution = {}
    if len(students) == 0 or len(chocolates) == 0:
        return distribution

    # Recursive step: Distribute chocolates to students
    chocolate = chocolates.pop(0)  # Take the first chocolate
    student = students.pop(0)  # Take the first student
    distribution[student] = chocolate  # Assign the chocolate to the student

    # Recursive call with updated lists
    return distribute_chocolates_recursive(chocolates, students, distribution)


# Test cases
chocolates = [
    {'weight': 5, 'price': 2, 'type': 'Almond chocolate', 'ID': '002'},
    {'weight': 7, 'price': 4, 'type': 'Peanut butter chocolate', 'ID': '005'},
    {'weight': 6, 'price': 3, 'type': 'Dark chocolate', 'ID': '007'},
    {'weight': 4, 'price': 5, 'type': 'Milk chocolate', 'ID': '009'},
    {'weight': 8, 'price': 6, 'type': 'White chocolate', 'ID': '011'}
]

students = ['Ali', 'Fatima', 'Youssef', 'Layla', 'Omar']

# Test case with exact number of chocolates and students
print("Test case 1:")
print("Iterative distribution:")
print(distribute_chocolates_iter(chocolates[:len(students)], students))
print("Recursive distribution:")
print(distribute_chocolates_recursive(chocolates[:len(students)], students))
print()

# Test case with more chocolates than students
print("Test case 2:")
print("Iterative distribution:")
print(distribute_chocolates_iter(chocolates, students))
print("Recursive distribution:")
print(distribute_chocolates_recursive(chocolates, students))
print()

# Test case with more students than chocolates
students_more = ['Ali', 'Fatima', 'Youssef', 'Layla', 'Omar', 'Ahmed', 'Huda']
print("Test case 3:")
print("Iterative distribution:")
print(distribute_chocolates_iter(chocolates, students_more))
print("Recursive distribution:")
print(distribute_chocolates_recursive(chocolates, students_more))
print()

# Test case with shortage of chocolates
chocolates_shortage = chocolates[:3]
print("Test case 4:")
print("Iterative distribution:")
print(distribute_chocolates_iter(chocolates_shortage, students))
print("Recursive distribution:")
print(distribute_chocolates_recursive(chocolates_shortage, students))


