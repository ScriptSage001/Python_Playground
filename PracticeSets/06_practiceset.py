# 1. Write a program to find the greatest of four numbers entered by the user.

# num1 = int(input("Enter number1: "))
# num2 = int(input("Enter number2: "))
# num3 = int(input("Enter number3: "))
# num4 = int(input("Enter number4: "))
#
# if num1 > num2 and num1 > num3 and num1 > num4:
#     print('The greatest number is ', num1)
# elif num2 > num3 and num2 > num4 and num2 > num1:
#     print('The greatest number is ', num2)
# elif num3 > num4 and num3 > num1 and num3 > num2:
#     print('The greatest number is ', num3)
# elif num4 > num1 and num4 > num2 and num4 > num3:
#     print('The greatest number is ', num4)
# else:
#     print('All the numbers are equal')

# 2. Write a program to find out whether a student has passed or failed if it requires a
# total of 40% and at least 33% in each subject to pass. Assume 3 subjects and
# take marks as an input from the user.

# print('Please enter the obtained marks out of 100 for the specific subjects below:')
# math  = int(input("Math:"))
# science  = int(input("Science:"))
# english  = int(input("English:"))
#
# total_percentage = (math + science + english)/3
#
# if total_percentage >= 40 and math >= 33 and science >= 33 and english >= 33:
#     print('Congratulations! You are passed.')
# else:
#     print('Sorry! You are failed.')

# 3. A spam comment is defined as a text containing following keywords:
# “Make a lot of money”, “buy now”, “subscribe this”, “click this”. Write a program to detect these spams.

### Try 1
# spam_comments = ['make a lot of money', 'buy now', 'subscribe this', 'click this']
# comment = input("Enter a comment: ")
#
# if comment in spam_comments:
#     print('This is a Spam Comment!')
# else:
#     print('This is a Not a Spam Comment!')

### Try 2
# spam1 = 'make a lot of money'
# spam2 = 'buy now'
# spam3 = 'subscribe this'
# spam4 = 'click this'
#
# comment = input("Enter a comment: ")
#
# if spam1 in comment or spam2 in comment or spam3 in comment or spam4 in comment:
#     print('This is a Spam Comment!')
# else:
#     print('This is a Not a Spam Comment!')

# 4. Write a program to find whether a given username contains less than 10 characters or not.

# userName = input("Enter your username: ")
#
# if len(userName) < 10:
#     print("Invalid username. Username must be at least 10 characters.")
# else:
#     print("Your username is:", userName)

# 5. Write a program which finds out whether a given name is present in a list or not.

# names = ['Ram', 'Shyam', 'Jadu', 'Madhu']
# name = input("Enter your name: ")
#
# if name in names:
#     print('You are already listed!')
# else:
#     print('You are not listed!')

# 6. Write a program to calculate the grade of a student from his marks from the following scheme:
# 90 – 100 => Ex
# 80 – 90 => A
# 70 – 80 => B
# 60 – 70  =>C
# 50 – 60 => D
# <50 => F

# marks = int(input("Enter marks out of 100: "))
#
# if 90 <= marks <= 100:
#     print("Your grade is Ex")
# elif 80 <= marks < 90:
#     print("Your grade is A")
# elif 70 <= marks < 80:
#     print("Your grade is B")
# elif 60 <= marks < 70:
#     print("Your grade is C")
# elif 50 <= marks < 60:
#     print("Your grade is D")
# elif 0 <= marks < 50:
#     print("Your grade is F")
# else:
#     print("Invalid marks.")

# 7. Write a program to find out whether a given post is talking about “Kaustab” or not.

# post = 'Hi, I am going to talk about Python. Kaustab is now learning this.'
#
# if 'Kaustab'.lower() in post.lower():
#     print('This post is talking about Kaustab.')
# else:
#     print('This post is not talking about Kaustab.')