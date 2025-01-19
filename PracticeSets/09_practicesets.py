# 1. Write a program to read the text from a given file ‘poems.txt’ and find out whether it contains the word ‘twinkle’.

# poem = '''
# Twinkle, twinkle, little star,
# How I wonder what you are.
# Up above the world so high,
# Like a diamond in the sky.
#
# When the blazing sun is gone,
# When he nothing shines upon,
# Then you show your little light,
# Twinkle, twinkle, all the night.
#
# Then the traveller in the dark,
# Thanks you for your tiny spark,
# He could not see which way to go,
# If you did not twinkle so.
#
# In the dark blue sky you keep,
# And often through my curtains peep,
# For you never shut your eye,
# ‘Till the sun is in the sky.
#
# As your bright and tiny spark,
# Lights the traveller in the dark.
# Though I know not what you are,
# Twinkle, twinkle, little star.
#
# Twinkle, twinkle, little star.
# How I wonder what you are.
# Up above the world so high,
# Like a diamond in the sky.
#
# Twinkle, twinkle, little star.
# How I wonder what you are.
# How I wonder what you are.
# '''
#
# with open('poem.txt', 'w+') as file:
#     file.write(poem)
#     file.seek(0)
#     poem_from_file = file.readlines()
#
# isExists = False
#
# for line in poem_from_file:
#     if 'twinkle' in line:
#         isExists = True
#         break
#
# if not isExists:
#     print('The word \'twinkle\' does not exists in the poem.')
# else:
#     print('The word \'twinkle\' exists in the poem.')

# 2. The game() function in a program lets a user play a game and returns the score as an integer.
# You need to read a file ‘Hi-score.txt’ which is either blank or contains the previous Hi-score.
# You need to write a program to update the Hi score whenever the game() function breaks the Hi-score.

import random
from os.path import exists


def game():
    return random.randint(0, 100)

def play_game_append_high_score():
    while True:
        high_score = game()

        try:
            with open('Hi-score.txt', 'r+') as file:
                prev_high_score = file.read().strip()

                if not prev_high_score:
                    prev_high_score = 0
                else:
                    prev_high_score = int(prev_high_score)

                if high_score > prev_high_score:
                    file.seek(0)
                    file.write(str(high_score))
                    file.truncate()
                    print('New high score:', high_score)
                else:
                    print('Current score:', high_score, '| High score:', prev_high_score)

        except FileNotFoundError:
            with open('Hi-score.txt', 'w') as file:
                file.write(str(high_score))
            print('New high score:', high_score)

        res = input('Want to play again? (y/n): ')
        if res.lower() == 'n':
            break

# play_game_append_high_score()

# 3. Write a program to generate multiplication tables from 2 to 20 and write it to the different files.
# Place these files in a folder for a 13 – year old.

import os

def multiplication_table_generator(n):
    with open(f'multiplication_table/table_of_{n}.txt', 'a') as file:
        file.write(f'The multiplication table of: {n}\n')
        for i in range(1, 11):
            file.write(f'{i} * {n} = {n * i}\n')

def create_multiplication_table_and_save_in_file():
    os.makedirs('multiplication_table', exist_ok=True)
    for i in range(2, 21):
        multiplication_table_generator(i)

# create_multiplication_table_and_save_in_file()

# 4. A file contains a word “Donkey” multiple times. You need to write a program which replace this word
# with ##### by updating the same file.

def replace_word_in_file(file_path, target_word, replace_word):
    with open(file_path, 'r') as file:
        content = file.read()

    updated_content = content.replace(target_word, replace_word)

    with open(file_path, 'w') as file:
        file.write(updated_content)

# replace_word_in_file('donkey.txt', 'Donkey', '######')

# 5. Repeat program 4 for a list of such words to be censored.

def censor_words_in_file(file_path, words_to_censor, replace_word = '######'):
    with open(file_path, 'r') as file:
        content = file.read()

    for i in words_to_censor:
        content = content.replace(i, replace_word)

    with open(file_path, 'w') as file:
        file.write(content)

# words_to_censor = ['Donkey', 'badword1', 'badword2']
# censor_words_in_file('donkey.txt', words_to_censor)

# 6. Write a program to mine a log file and find out whether it contains ‘python’.

def find_word_in_log(file_path, target_word):
    with open(file_path, 'r') as file:
        for line in file:
            if target_word.lower() in line.lower():
                print(f"'{target_word}' found on the log file: {line.strip()}")
                return True

        print(f"'{target_word}' not found on the log file.")
        return False

# find_word_in_log('log.txt', 'python')

# 7. Write a program to find out the line number where python is present from ques 6.

def find_word_in_log_with_line_number(file_path, target_word):
    with open(file_path, 'r') as file:
        for line_number, line in enumerate(file, start = 1):
            if target_word.lower() in line.lower():
                print(f"'{target_word}' found on line {line_number}: {line.strip()}")
                return True

        print(f"'{target_word}' not found on the log file.")
        return False

# find_word_in_log_with_line_number('log.txt', 'python')

# 8. Write a program to make a copy of a text file “this.txt”

import os

def copy_file(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()

        file_name, file_extension = os.path.splitext(file_path)

        copy_file_path = f'{file_name}_copy{file_extension}'

        with open(copy_file_path, 'w') as file:
            file.write(content)

        print('Copied file:', copy_file_path)

    except FileNotFoundError:
        print('File not found')

# copy_file('this.txt')

# 9. Write a program to find out whether a file is identical & matches the content of another file.

def compare_files(file_path1, file_path2):
    try:
        with open(file_path1, 'rb') as file_one, open(file_path2, 'rb') as file_two:
            while True:
                chunk_one = file_one.read(4096)
                chunk_two = file_two.read(4096)

                if chunk_one != chunk_two:
                    print(f'The files {file_path1} and {file_path2} do not match')
                    return False

                if not chunk_one and not chunk_two:
                    print(f'The files {file_path1} and {file_path2} are identical')
                    return True

    except FileNotFoundError as e:
        print('File not found, error:', e)
        return False

# compare_files('this.txt', 'this_copy.txt')

# 10. Write a program to wipe out the content of a file using python.

def wipe_file_content(file_path):
    try:
        with open(file_path, 'w') as file:
            pass

        print(f"The content of the file '{file_path}' has been wiped out.")

    except FileNotFoundError:
        print(f"Error: The file '{file_path}' does not exist.")

# wipe_file_content('this_copy.txt')

# 11. Write a python program to rename a file to "renamed_by_python.txt".

import os


def rename_file(file_path):
    try:
        directory = os.path.dirname(file_path)

        new_file_path = os.path.join(directory, "renamed_by_python.txt")

        os.rename(file_path, new_file_path)

        print(f"The file has been renamed to '{new_file_path}'")

    except FileNotFoundError:
        print(f"Error: The file '{file_path}' does not exist.")

#rename_file('this_copy.txt')