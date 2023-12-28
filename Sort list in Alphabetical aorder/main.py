# Function to sort a list in alphabetical order

def sort_list(lst: list):
    """
    Sorts a list in alphabetical order

    Args:
        lst (list): The list to be sorted

    Returns:
        list: The sorted list
    """
    lst.sort()
    return lst

list_to_sort = []

while True:
    item = input("Enter an item to add to the list (or 'done' to finish): ")
    if item == 'done':
        break
    list_to_sort.append(item)

print(sort_list(list_to_sort))