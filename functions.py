def greeting(name):
    print('Hello', name)

# Main Program
name1 = input('Enter your name:\n')
greeting(name1)
name2 = input('Enter your name:\n')
greeting(name2)


# Creating our addition function
def addition(a, b):
    return a + b

# Addition Main Program

def main():
    num1 = float(input('Enter your 1st number:\n'))
    num2 = float(input('Enter your 2nd number:\n'))

    # Calling out the function
    result = addition(num1, num2)
    print('The result is', result)

main()