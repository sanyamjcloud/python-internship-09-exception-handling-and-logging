import logging

# ---------------- LOGGING CONFIGURATION ----------------
logging.basicConfig(
    filename="error.log",
    level=logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# ---------------- CUSTOM EXCEPTION ----------------
class NegativeNumberError(Exception):
    """Raised when a negative number is entered"""
    pass


def divide_numbers(a, b):
    try:
        # Simulating runtime errors
        if a < 0 or b < 0:
            raise NegativeNumberError("Negative numbers are not allowed")

        result = a / b

    except ZeroDivisionError as e:
        logging.error("ZeroDivisionError occurred", exc_info=True)
        print("Error: Cannot divide by zero")

    except ValueError as e:
        logging.error("ValueError occurred", exc_info=True)
        print("Error: Invalid input type")

    except NegativeNumberError as e:
        logging.error(e, exc_info=True)
        print(f"Custom Error: {e}")

    except Exception as e:
        logging.error("Unexpected error occurred", exc_info=True)
        print("An unexpected error occurred")

    else:
        print(f"Division successful. Result = {result}")

    finally:
        print("Execution completed")


# ---------------- MAIN PROGRAM ----------------
try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    divide_numbers(num1, num2)

except Exception as e:
    logging.error("Input error in main block", exc_info=True)
    print("Failed to read input")
