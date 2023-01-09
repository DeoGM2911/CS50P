def main():
    while True:
        #format x y z where x and z are integers and y is an operation ( + - * /)
        elements = input("What is the expression? \n").split(' ')
        #Re-prompt the expression if the input format is not correct
        try:
            # We can trim this down to one line, but for readability, I'll keep the variables x,z,y
            x = float(elements[0])
            z = float(elements[2])
            y = elements[1]
            print(intepreter(x,z,y))
        except ValueError:
            print("Error with math expression!")
            continue


# The function here is 
def intepreter(x: float,z: float, y: str):
    """This is to create an interpreter for operation
    Args:
        x (float) and z (float) are numbers
    Returns: the result of the operation with two variable x and z
        """
    if y == '+':
        return f"The answer is {x+z}"
    elif y == '-':
        return f"The answer is {x-z}"
    elif y == '*':
        return f"The answer is {x*z}"
    elif y == '/':
        return f"The answer is {x/z}"
    # Just for fun for the power operation
    elif y == '**':
        return f"The answer is {x**z}"
    else:
        return "Error with the operation"


main()