def set_functions():
    # Sample set
    sample_set = {1, 2, 3, 4, 5}

    # 1. add() - Adds an element to the set
    sample_set.add(6)
    print("add(6):", sample_set)

    # 2. update() - Adds multiple elements to the set
    sample_set.update([7, 8, 9])
    print("update([7, 8, 9]):", sample_set)

    # 3. remove() - Removes an element from the set (raises KeyError if not found)
    sample_set.remove(9)
    print("remove(9):", sample_set)

    # 4. discard() - Removes an element if it exists (does not raise an error if not found)
    sample_set.discard(10)
    print("discard(10):", sample_set)

    # 5. pop() - Removes and returns an arbitrary element from the set
    popped_element = sample_set.pop()
    print("pop():", popped_element, "; Set after pop:", sample_set)

    # 6. clear() - Removes all elements from the set
    temp_set = sample_set.copy()
    temp_set.clear()
    print("clear():", temp_set)

    # 7. copy() - Returns a shallow copy of the set
    copied_set = sample_set.copy()
    print("copy():", copied_set)

    # 8. union() - Returns a new set with all elements from both sets
    another_set = {4, 5, 6, 7}
    union_set = sample_set.union(another_set)
    print("union({4, 5, 6, 7}):", union_set)

    # 9. intersection() - Returns a new set with elements common to both sets
    intersection_set = sample_set.intersection(another_set)
    print("intersection({4, 5, 6, 7}):", intersection_set)

    # 10. difference() - Returns a new set with elements in the first set but not in the second
    difference_set = sample_set.difference(another_set)
    print("difference({4, 5, 6, 7}):", difference_set)

    # 11. symmetric_difference() - Returns a new set with elements in either set but not in both
    symmetric_diff_set = sample_set.symmetric_difference(another_set)
    print("symmetric_difference({4, 5, 6, 7}):", symmetric_diff_set)

    # 12. issubset() - Checks if the set is a subset of another set
    print("issubset({1, 2, 3, 4, 5}):", sample_set.issubset({1, 2, 3, 4, 5, 6, 7}))

    # 13. issuperset() - Checks if the set is a superset of another set
    print("issuperset({3, 4}):", sample_set.issuperset({3, 4}))

    # 14. isdisjoint() - Checks if two sets have no elements in common
    print("isdisjoint({10, 11}):", sample_set.isdisjoint({10, 11}))

    # 15. len() - Returns the number of elements in the set
    print("len():", len(sample_set))

    # 16. in operator - Checks if an element exists in the set
    print("3 in sample_set:", 3 in sample_set)
    print("10 in sample_set:", 10 in sample_set)

    # 17. Set comprehension - Creates a new set with a condition
    squared_set = {x ** 2 for x in sample_set}
    print("Set comprehension {x ** 2 for x in sample_set}:", squared_set)

# Run the function
if __name__ == "__main__":
    set_functions()