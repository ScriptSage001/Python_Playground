text = 'This is a sample text to be added to a file created using Python File I/O'
next_line = '\nThis is another sample text to be added to a file created using Python File I/O append operation'
update_line = 'This line will replace the previous text using \'w+\' operation (truncates if exists or creates a new one)'
multi_line_text = text + next_line + '\nThis is another line for the multi line text.'

# file = open('text_file.txt', 'w')
# file.write(text)
# file.close()

# file = open('text_file.txt', 'r')
# print(file.read())
# file.close()

# with open('text_file.txt', 'a') as file:
#     file.write(next_line)

# with open('text_file.txt', 'w+') as file:
#     file.write(update_line)
#     file.seek(0) # Moves the file pointer back to the file beginning
#     print(file.read())

# with open("text.txt", "w+") as file:
#     file.write(multi_line_text)
#     file.seek(0)
#     print(file.readlines(), type(file.readlines())) # Prints all the lines as list

# with open("text.txt", "r") as file:
#     while True:
#         line = file.readline() # Gets a single line, next execution prints the next line.
#         if line == '':
#             break
#         print(line)
