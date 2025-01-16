def dictionary_functions():
    # Sample dictionary
    sample_dict = {"a": 1, "b": 2, "c": 3, "d": 4}

    # 1. keys() - Returns a view object of dictionary keys
    print("keys():", sample_dict.keys())

    # 2. values() - Returns a view object of dictionary values
    print("values():", sample_dict.values())

    # 3. items() - Returns a view object of key-value pairs
    print("items():", sample_dict.items())

    # 4. get() - Returns the value for a specified key (or a default if not found)
    print("get('a'):", sample_dict.get("a"))
    print("get('z'):", sample_dict.get("z"))
    print("get('z', 'default'):", sample_dict.get("z", "default"))

    # 5. update() - Updates the dictionary with key-value pairs from another dictionary or iterable
    sample_dict.update({"e": 5, "f": 6})
    print("update({'e': 5, 'f': 6}):", sample_dict)

    # 6. pop() - Removes the specified key and returns the value
    popped_value = sample_dict.pop("f")
    print("pop('f'):", popped_value, "; Dictionary after pop:", sample_dict)

    # 7. popitem() - Removes and returns the last key-value pair
    last_item = sample_dict.popitem()
    print("popitem():", last_item, "; Dictionary after popitem:", sample_dict)

    # 8. setdefault() - Returns the value of a key, and sets it with a default if not present
    default_value = sample_dict.setdefault("g", 7)
    print("setdefault('g', 7):", default_value, "; Dictionary after setdefault:", sample_dict)

    # 9. clear() - Removes all elements from the dictionary
    temp_dict = sample_dict.copy()
    temp_dict.clear()
    print("clear():", temp_dict)

    # 10. copy() - Returns a shallow copy of the dictionary
    copied_dict = sample_dict.copy()
    print("copy():", copied_dict)

    # 11. len() - Returns the number of items in the dictionary
    print("len():", len(sample_dict))

    # 12. in operator - Checks if a key exists in the dictionary
    print("'a' in sample_dict:", "a" in sample_dict)
    print("'z' in sample_dict:", "z" in sample_dict)

    # 13. Dictionary comprehension - Creates a new dictionary with condition
    squared_dict = {k: v ** 2 for k, v in sample_dict.items()}
    print("Dictionary comprehension {k: v ** 2 for k, v in sample_dict.items()}:", squared_dict)

    # 14. Iterating over a dictionary
    print("Iterating over keys and values:")
    for key, value in sample_dict.items():
        print(f"Key: {key}, Value: {value}")

    # 15. Merging two dictionaries (Python 3.9+)
    another_dict = {"h": 8, "i": 9}
    merged_dict = sample_dict | another_dict
    print("Merging dictionaries (| operator):", merged_dict)

# Run the function
if __name__ == "__main__":
    dictionary_functions()