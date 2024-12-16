first_number = int(input("Enter the first number: "))
second_number = int(input("Enter the second number: "))
operation = input("Choose the operation (+, -, *, /): ")

match operation:
    case if operation == "+":
         print(f"The result is{(first_number+second_number)}")
    case if operation == "-":
         print(f"The result is{(first_number-second_number)}")
    case if operation == "*":
         print(f"The result is{(first_number*second_number)}")
    case if operation == "/":
         print(f"The result is{(first_number/second_number)}")
    case if (operation == "/" and second_number==0):
        return "Cannot divide zero."                
