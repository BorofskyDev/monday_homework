
def calculate():
    while True:
        print("Make your choice -\n"
            "1. Add\n"
            "2. Subtract\n"
            "3. Multiply\n"
            "4. Divide\n"
            "5. Quit")
        option = int(input("Please enter in options 1, 2, 3, 4, or 5 : -\n"))
        num_1 = int(input("Enter your first number: "))
        num_2 = int(input("Enter your second number: "))

        if option == 1:
            print("{} + {} = " .format(num_1, num_2))
            print(num_1 + num_2)

        elif option == 2:
            print("{} - {} = ".format(num_1, num_2))
            print(num_1 - num_2)

        elif option == 3:
            print("{} - {} = ".format(num_1, num_2))
            print(num_1 * num_2)

        elif option == 4:
            print("{} - {} = ".format(num_1, num_2))
            print(num_1 / num_2)

        elif option == 5:
            break
            print("Cool, thanks")
        else:
            print("C'mon, really?")
