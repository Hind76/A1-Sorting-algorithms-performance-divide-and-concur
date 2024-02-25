def merge_sort(chocolates, key='weight'):
    # Base case: If the list has 0 or 1 element, it's already sorted
    if len(chocolates) <= 1:
        return chocolates

    # Find the midpoint of the list
    mid = len(chocolates) // 2

    # Recursively sort the left and right halves of the list
    left_half = merge_sort(chocolates[:mid], key)
    right_half = merge_sort(chocolates[mid:], key)

    # Merge the sorted left and right halves
    return merge(left_half, right_half, key)


def merge(left, right, key):
    # Initialize an empty list to store the merged result
    result = []
    left_index, right_index = 0, 0

    # Merge the two lists by comparing elements based on the specified key
    while left_index < len(left) and right_index < len(right):
        if left[left_index][key] < right[right_index][key]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1

    # Add any remaining elements from the left and right lists
    result.extend(left[left_index:])
    result.extend(right[right_index:])

    return result


# Test cases
chocolates_1 = [
    {'weight': 5, 'price': 2, 'type': 'Almond chocolate', 'ID': '002'},
    {'weight': 7, 'price': 4, 'type': 'Peanut butter chocolate', 'ID': '005'},
    {'weight': 6, 'price': 3, 'type': 'Dark chocolate', 'ID': '007'},
    {'weight': 4, 'price': 5, 'type': 'Milk chocolate', 'ID': '009'},
    {'weight': 8, 'price': 6, 'type': 'White chocolate', 'ID': '011'}
]

chocolates_2 = [
    {'weight': 10, 'price': 8, 'type': 'Hazelnut chocolate', 'ID': '012'},
    {'weight': 3, 'price': 4, 'type': 'Caramel chocolate', 'ID': '013'},
    {'weight': 6, 'price': 5, 'type': 'Coconut chocolate', 'ID': '014'},
    {'weight': 9, 'price': 6, 'type': 'Fruit chocolate', 'ID': '015'},
    {'weight': 7, 'price': 7, 'type': 'Mint chocolate', 'ID': '016'}
]

chocolates_3 = [
    {'weight': 8, 'price': 10, 'type': 'Strawberry chocolate', 'ID': '017'},
    {'weight': 2, 'price': 3, 'type': 'Orange chocolate', 'ID': '018'},
    {'weight': 5, 'price': 4, 'type': 'Raspberry chocolate', 'ID': '019'},
    {'weight': 7, 'price': 2, 'type': 'Blueberry chocolate', 'ID': '020'},
    {'weight': 4, 'price': 6, 'type': 'Cherry chocolate', 'ID': '021'}
]

# Sort chocolates by weight
sorted_chocolates_by_weight_1 = merge_sort(chocolates_1, key='weight')
print("Sorted chocolates by weight:")
for chocolate in sorted_chocolates_by_weight_1:
    print(chocolate)

# Sort chocolates by price
sorted_chocolates_by_price_1 = merge_sort(chocolates_1, key='price')
print("\nSorted chocolates by price:")
for chocolate in sorted_chocolates_by_price_1:
    print(chocolate)

# Additional test cases
print("\nAdditional Test Cases:")
sorted_chocolates_by_weight_2 = merge_sort(chocolates_2, key='weight')
print("\nSorted chocolates by weight:")
for chocolate in sorted_chocolates_by_weight_2:
    print(chocolate)

sorted_chocolates_by_price_3 = merge_sort(chocolates_3, key='price')
print("\nSorted chocolates by price:")
for chocolate in sorted_chocolates_by_price_3:
    print(chocolate)
