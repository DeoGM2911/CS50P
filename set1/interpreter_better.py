while True:
    prompt = input("What is the expression? \n")
    #format x y z where x and z are integers and y is an operation ( + - * /)
    if prompt == '1': break
    #for testing purposes
    elements = prompt.split(' ')
    #Re-prompt the expression if the input format is not correct
    try:
        x = float(elements[0])
        y = elements[1]
        z = float(elements[2])
    except:
        print("Error with math expression! Please try again!")
        continue
    def power(x: float,z: float):
        """This is to create an interpreter for power operation

        Args:
            x (float): the base
            z (float): the power

        Returns:
            x to the power of z
        """
        list = []
        result = 1
        for i in range(int(z)):
            list.append(int(x))
        for value in list:
            result = result * value
        return float(result)
    #The interpreter starts here
    if y == '+':
        print(f"The answer is {x+z}")
    elif y == '-':
        print(f"The answer is {x-z}")
    elif y == '*':
        print(f"The answer is {x*z}")
    elif y == '/':
        print(f"The answer is {x/z}")
    elif y == '**':
        print(f"The answer is {power(x,z)}")
    else:
        print("Error with math expression")