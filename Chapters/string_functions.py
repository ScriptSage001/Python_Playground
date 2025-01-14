def string_functions():
    # Sample string
    sample_text = "Hello, Python Beginners!"

    # 1. len() - Returns the length of the string
    print("len():", len(sample_text))

    # 2. lower() - Converts all characters to lowercase
    print("lower():", sample_text.lower())

    # 3. upper() - Converts all characters to uppercase
    print("upper():", sample_text.upper())

    # 4. strip() - Removes leading and trailing whitespace
    whitespace_text = "   Extra spaces   "
    print("strip():", whitespace_text.strip())

    # 5. replace() - Replaces occurrences of a substring
    print("replace('Python', 'World'):", sample_text.replace("Python", "World"))

    # 6. split() - Splits the string into a list based on a delimiter
    print("split():", sample_text.split())

    # 7. join() - Joins a list of strings with a delimiter
    words = ["Join", "these", "words"]
    print("join():", " ".join(words))

    # 8. capitalize() - Capitalizes the first character
    print("capitalize():", sample_text.capitalize())

    # 9. title() - Converts the first character of each word to uppercase
    print("title():", sample_text.title())

    # 10. find() - Finds the first occurrence of a substring
    print("find('Python'):", sample_text.find("Python"))

    # 11. count() - Counts the occurrences of a substring
    print("count('e'):", sample_text.count("e"))

    # 12. startswith() - Checks if the string starts with a specific substring
    print("startswith('Hello'):", sample_text.startswith("Hello"))

    # 13. endswith() - Checks if the string ends with a specific substring
    print("endswith('Beginners!'):", sample_text.endswith("Beginners!"))

    # 14. isdigit() - Checks if all characters are digits
    numeric_text = "12345"
    print("isdigit():", numeric_text.isdigit())

    # 15. isalpha() - Checks if all characters are alphabetic
    alpha_text = "HelloWorld"
    print("isalpha():", alpha_text.isalpha())

    # 16. isalnum() - Checks if all characters are alphanumeric
    alnum_text = "Hello123"
    print("isalnum():", alnum_text.isalnum())

    # 17. lstrip() - Removes leading whitespace
    print("lstrip():", whitespace_text.lstrip())

    # 18. rstrip() - Removes trailing whitespace
    print("rstrip():", whitespace_text.rstrip())

    # 19. rfind() - Finds the last occurrence of a substring
    print("rfind('e'):", sample_text.rfind("e"))

    # 20. swapcase() - Swaps the case of each character
    print("swapcase():", sample_text.swapcase())

    # 21. zfill() - Pads the string with zeros
    print("zfill(10):", "42".zfill(10))

    # 22. center() - Centers the string within a given width
    print("center(30, '*'):", sample_text.center(30, '*'))

    # 23. ljust() - Left-aligns the string within a given width
    print("ljust(30, '-'):", sample_text.ljust(30, '-'))

    # 24. rjust() - Right-aligns the string within a given width
    print("rjust(30, '.'):", sample_text.rjust(30, '.'))

    # 25. encode() - Encodes the string using a specified encoding
    print("encode():", sample_text.encode("utf-8"))

    # 26. format() - Formats the string
    print("format():", "Hello, {}!".format("World"))

    # 27. maketrans() and translate() - Maps and replaces characters
    translation_table = str.maketrans("HPe", "123")
    print("translate():", sample_text.translate(translation_table))

# Run the function
if __name__ == "__main__":
    string_functions()