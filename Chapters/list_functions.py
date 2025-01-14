# list_functions_demo.py

def list_functions():
    # Sample list
    sample_list = [1, 2, 3, 4, 5]

    # 1. append() - Adds an element to the end of the list
    sample_list.append(6)
    print("append(6):", sample_list)

    # 2. extend() - Adds all elements of an iterable to the end of the list
    sample_list.extend([7, 8])
    print("extend([7, 8]):", sample_list)

    # 3. insert() - Inserts an element at a specified position
    sample_list.insert(2, 99)
    print("insert(2, 99):", sample_list)

    # 4. remove() - Removes the first occurrence of a value
    sample_list.remove(99)
    print("remove(99):", sample_list)

    # 5. pop() - Removes and returns an element at a given index (default is the last element)
    popped_element = sample_list.pop()
    print("pop():", popped_element, "; List after pop:", sample_list)

    # 6. clear() - Removes all elements from the list
    temp_list = sample_list.copy()
    temp_list.clear()
    print("clear():", temp_list)

    # 7. index() - Returns the index of the first occurrence of a value
    print("index(3):", sample_list.index(3))

    # 8. count() - Counts the occurrences of a value
    print("count(3):", sample_list.count(3))

    # 9. sort() - Sorts the list in ascending order (or descending with reverse=True)
    unsorted_list = [5, 3, 1, 4, 2]
    unsorted_list.sort()
    print("sort():", unsorted_list)

    # 10. reverse() - Reverses the order of elements in the list
    unsorted_list.reverse()
    print("reverse():", unsorted_list)

    # 11. copy() - Creates a shallow copy of the list
    copied_list = sample_list.copy()
    print("copy():", copied_list)

    # 12. len() - Returns the length of the list
    print("len():", len(sample_list))

    # 13. max() - Returns the maximum value in the list
    print("max():", max(sample_list))

    # 14. min() - Returns the minimum value in the list
    print("min():", min(sample_list))

    # 15. sum() - Returns the sum of all elements in the list
    print("sum():", sum(sample_list))

    # 16. any() - Returns True if any element in the list is True
    print("any():", any(sample_list))

    # 17. all() - Returns True if all elements in the list are True
    print("all():", all(sample_list))

    # 18. enumerate() - Returns an enumerate object (used for iteration)
    print("enumerate():", list(enumerate(sample_list)))

    # 19. filter() - Filters elements based on a condition
    filtered_list = list(filter(lambda x: x % 2 == 0, sample_list))
    print("filter(lambda x: x % 2 == 0):", filtered_list)

    # 20. map() - Applies a function to all elements
    mapped_list = list(map(lambda x: x * 2, sample_list))
    print("map(lambda x: x * 2):", mapped_list)

    # 21. list comprehension - Generates a new list with a condition
    comprehension_list = [x ** 2 for x in sample_list if x % 2 == 0]
    print("list comprehension [x ** 2 for x in sample_list if x % 2 == 0]:", comprehension_list)

# Run the function
if __name__ == "__main__":
    list_functions()