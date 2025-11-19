"""
Simple calculator module using functions.

This module demonstrates clean, pylint-friendly code
with proper naming, docstrings, and structure.
"""


def greet_user(name: str) -> str:
    """
    Return a greeting message for the given user.

    Args:
        name (str): Name of the user.

    Returns:
        str: Greeting message.
    """
    return f"Hello, {name}! Hope you're learning Python well."


def add_numbers(num1: int, num2: int) -> int:
    """
    Return the sum of two numbers.

    Args:
        num1 (int): First number.
        num2 (int): Second number.

    Returns:
        int: Sum of num1 and num2.
    """
    return num1 + num2


def main() -> None:
    """
    Main function to run the module.
    """
    user_name = "Vaibhavi"
    print(greet_user(user_name))

    result = add_numbers(10, 15)
    print("Result:", result)


if __name__ == "__main__":
    main()
