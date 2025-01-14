# 1. Write a program to print Twinkle twinkle little star poem in python.
print('''
Twinkle, twinkle, little star,
How I wonder what you are.
Up above the world so high,
Like a diamond in the sky.

When the blazing sun is gone,
When he nothing shines upon,
Then you show your little light,
Twinkle, twinkle, all the night.

Then the traveller in the dark,
Thanks you for your tiny spark,
He could not see which way to go,
If you did not twinkle so.

In the dark blue sky you keep,
And often through my curtains peep,
For you never shut your eye,
‘Till the sun is in the sky.

As your bright and tiny spark,
Lights the traveller in the dark.
Though I know not what you are,
Twinkle, twinkle, little star.

Twinkle, twinkle, little star.
How I wonder what you are.
Up above the world so high,
Like a diamond in the sky.

Twinkle, twinkle, little star.
How I wonder what you are.
How I wonder what you are.
''')

# 2. Use REPL and print the table of 5 using it.

# 3. Install an external module and use it to perform an operation of your interest.
import pyjokes
print(pyjokes.get_joke())

# 4. Write a python program to print the contents of a directory using the os module.
import os

directory = 'C:\CodeBase\Python\Playground'
print(os.listdir(directory))

# 5. Label the program written in problem 4 with comments.
# Importing the OS module
import os

# Storing the directory path in variable named directory
directory = 'C:\CodeBase\Python\Playground'

# Listing the contents of the directory using the OS module
print(os.listdir(directory))