# tuple_functions_demo.py

def tuple_functions():
    # Sample tuple
    sample_tuple = (1, 2, 3, 4, 5, 3, 3)

    # 1. len() - Returns the length of the tuple
    print("len():", len(sample_tuple))

    # 2. count() - Counts the occurrences of a value
    print("count(3):", sample_tuple.count(3))

    # 3. index() - Returns the index of the first occurrence of a value
    print("index(4):", sample_tuple.index(4))

    # 4. max() - Returns the maximum value in the tuple
    print("max():", max(sample_tuple))

    # 5. min() - Returns the minimum value in the tuple
    print("min():", min(sample_tuple))

    # 6. sum() - Returns the sum of all elements in the tuple
    print("sum():", sum(sample_tuple))

    # 7. any() - Returns True if any element in the tuple is True
    print("any():", any(sample_tuple))

    # 8. all() - Returns True if all elements in the tuple are True
    print("all():", all(sample_tuple))

    # 9. enumerate() - Returns an enumerate object (used for iteration)
    print("enumerate():", list(enumerate(sample_tuple)))

    # 10. tuple comprehension using generator expression - Simulates list comprehension (indirect example)
    squared_tuple = tuple(x ** 2 for x in sample_tuple)
    print("tuple comprehension (x ** 2 for x in sample_tuple):", squared_tuple)

    # 11. Joining tuples
    another_tuple = (6, 7, 8)
    joined_tuple = sample_tuple + another_tuple
    print("Joining tuples:", joined_tuple)

    # 12. Slicing tuples
    sliced_tuple = sample_tuple[1:4]
    print("Slicing tuples (1:4):", sliced_tuple)

    # 13. Nested tuple example
    nested_tuple = (sample_tuple, another_tuple)
    print("Nested tuple:", nested_tuple)

    # 14. Unpacking tuple
    a, b, c, *rest = sample_tuple
    print("Unpacking tuple (a, b, c, *rest):", a, b, c, rest)

    # 15. Immutable property demonstration
    try:
        sample_tuple[0] = 10
    except TypeError as e:
        print("Immutable property demonstration:", e)

# Run the function
if __name__ == "__main__":
    tuple_functions()