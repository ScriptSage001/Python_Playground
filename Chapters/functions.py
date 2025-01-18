def take_input_do_average():
    a = int(input("Enter a number: "))
    b = int(input("Enter another number: "))
    avg = average(a, b)
    print("The average is: ", avg)

def average(a, b, c = 0):
    if c == 0:
        avg = (a + b)/2
    else:
        avg = (a + b + c)/3
    return avg

take_input_do_average()