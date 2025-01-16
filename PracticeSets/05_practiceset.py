# 1. Write a program to create a dictionary of Bengali words with values as their English
# translation. Provide user with an option to look it up!

# lang_translator = {
#     'Tumi': 'You',
#     'Keno': 'Why',
#     'K': 'Who',
#     'Brishti': 'Rain',
#     'Raat': 'Night'
# }
# print('Here are some Bengali words which I can translate to english:', lang_translator.keys())
# word = input('Enter the word you want to translate:')
# print('The translation of:', word, 'in English is:', lang_translator[word])

# 2. Write a program to input eight numbers from the user and display all the unique numbers (once).

# unique_nums = set()
# print('Enter 8 numbers.')
# unique_nums.add(int((input("Enter a number:"))))
# unique_nums.add(int((input("Enter a number:"))))
# unique_nums.add(int((input("Enter a number:"))))
# unique_nums.add(int((input("Enter a number:"))))
# unique_nums.add(int((input("Enter a number:"))))
# unique_nums.add(int((input("Enter a number:"))))
# unique_nums.add(int((input("Enter a number:"))))
# unique_nums.add(int((input("Enter a number:"))))
# unique_nums.add(int((input("Enter a number:"))))
#
# print('Here are all the unique numbers you have entered:', unique_nums)

# 3. Can we have a set with 18 (int) and '18' (str) as a value in it?

# s = {18, '18'}
# print('A set with 18 (int) and \'18\' (str) as a value:', s)

# 4. What will be the length of following set s:
# s = set()
# s.add(20)
# s.add(20.0)
# s.add('20') # length of s after these operations?

# Ans: Length will be 2 as the 20 and 20.0 will be considered equal and be inserted once.

# 5. s = {} - What is the type of 's'?

# Ans: The type of s is Dictionary.

# 6. Create an empty dictionary. Allow 4 friends to enter their favorite language as
# value and use key as their names. Assume that the names are unique.

fav_lang_dict = {}

# print('Enter your favourite language one by one following the instructions:')
#
# name = input('Enter your name:')
# lang = input('Enter your favourite language:')
# fav_lang_dict.update({name:lang})
#
# name = input('Enter your name:')
# lang = input('Enter your favourite language:')
# fav_lang_dict.update({name:lang})
#
# name = input('Enter your name:')
# lang = input('Enter your favourite language:')
# fav_lang_dict.update({name:lang})
#
# name = input('Enter your name:')
# lang = input('Enter your favourite language:')
# fav_lang_dict.update({name:lang})
#
# print('Here are the favourite languages of all of you:', fav_lang_dict)

# 7. If the names of 2 friends are same; what will happen to the program in problem 6?

# Ans: Keys are supposed to be unique. So, there will be only one entry for the name and the value will be the one entered later.
# e.g., If we enter 'Ram': 'Hindi' and 'Ram': 'Bengali' then only the second one will be added.

# 8. If languages of two friends are same; what will happen to the program in problem 6?

# Ans: Values are not unique, so both of the records will be there.

# 9. Can you change the values inside a list which is contained in set S?
# s = {8, 7, 12, "Kaustab", [1,2]}

# Ans: No, sets are immutable. Also, list cannot be added to set.
