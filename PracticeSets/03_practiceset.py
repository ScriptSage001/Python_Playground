# 1. Write a python program to display a user entered name followed by Good Afternoon using input () function.
name = input("Enter your name: ")
print(f"Good Afternoon, {name}.")

# 2. Write a program to fill in a letter template given below with name and date.
# letter = '''
# Dear <|Name|>,
# You are selected!
# <|Date|>
# '''

letter = '''Dear <|Name|>,
                    You are selected!
<|Date|>'''

print(letter.replace('<|Name|>', "Kaustab Samanta").replace('<|Date|>', "07 March, 2022"))

# 3. Write a program to detect double space in a string.
sampleText = "Kaustab is a good  boy."
print(sampleText.find("  ") >= 0)

# 4. Replace the double space from problem 3 with single spaces.
sampleText = "Kaustab is a good  boy."
print(sampleText.replace("  ", " "))

# 5. Write a program to format the following letter using escape sequence characters.
# letter = "Dear Kaustab, This python course is nice. Thanks!"

letter = "Dear Kaustab,\n\tThis python course is nice.\n\t\tThanks!"
print(letter)
