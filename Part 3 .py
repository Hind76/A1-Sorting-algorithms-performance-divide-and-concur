def search_chocolate(chocolates, value, key='price'):
    """
    Function to find the student holding a chocolate with a specified price or weight.

    Args:
    chocolates (list): List of dictionaries representing chocolates assigned to students.
    value (int): The price or weight of the chocolate to search for.
    key (str): Key indicating whether to search by 'price' or 'weight'. Default is 'price'.

    Returns:
    str: Name of the student holding the specified chocolate, or 'Chocolate not found' if not found.
    """

    # Initialize start and end indices for binary search
    start = 0
    end = len(chocolates) - 1

    # Binary search loop
    while start <= end:
        # Calculate mid index
        mid = (start + end) // 2

        # Check if value matches the chocolate's price or weight
        if chocolates[mid][key] == value:
            return f"Student holding chocolate with {key}: {value} is {chocolates[mid]['student']}"
        elif chocolates[mid][key] < value:
            # If value is greater, search in the right half
            start = mid + 1
        else:
            # If value is smaller, search in the left half
            end = mid - 1

    # If chocolate not found
    return "Chocolate not found"


# Test cases
chocolates = [
    {'weight': 5, 'price': 2, 'student': 'Ali'},
    {'weight': 7, 'price': 4, 'student': 'Fatima'},
    {'weight': 6, 'price': 6, 'student': 'Youssef'},
    {'weight': 8, 'price': 8, 'student': 'Layla'},
    {'weight': 10, 'price': 10, 'student': 'Omar'},
    {'weight': 4, 'price': 3, 'student': 'Ahmed'},
    {'weight': 9, 'price': 7, 'student': 'Huda'},
    {'weight': 12, 'price': 14, 'student': 'Sara'}
]

# Test case 1: Search for a chocolate with price 4
print("Searching for chocolate with price 4:")
print(search_chocolate(chocolates, 4, key='price'))

# Test case 2: Search for a chocolate with weight 8
print("\nSearching for chocolate with weight 8:")
print(search_chocolate(chocolates, 8, key='weight'))

# Test case 3: Search for a chocolate with price 3 (not found)
print("\nSearching for chocolate with price 3:")
print(search_chocolate(chocolates, 3, key='price'))
