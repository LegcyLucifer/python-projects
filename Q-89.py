# (89) How Do You Handle Exceptions with Try/Except/Finally in Python ? 

""" Structure :

        try Block:
            Contains the code that might raise an exception.
        except Block:
            Handles specific exceptions or a generic exception.
        finally Block:
            Contains code that runs regardless of whether an exception occurs or not (usually for cleanup tasks)."""
            
try:
    num = int(input("Enter a number: "))
    result = 10 / num
    print(f"Result is {result}")
except ValueError:
    print("Invalid input! Please enter a valid integer.")
except ZeroDivisionError:
    print("Division by zero is not allowed.")
finally:
    print("Execution of the try-except-finally block is complete.")