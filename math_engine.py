def addition(num1, num2):
    """Returns the addition of two numbers"""
    return num1 + num2


def substraction(num1, num2):
    """Return the difference of two nubers"""
    return num1 - num2


def multiply(num1, num2):
    """Returns the product of two numbers"""
    return num1 * num2


def division(num1, num2):
    """
    The function multiplies two numbers, then returns after dividing the
    second of the numbers
    """
    result = multiply(num1, num2)
    try:
        return result / num1
    except ZeroDivisionError:
        return 999


def get_result(number1, number2, operation):
    """Returns the result of a given mathematical operation"""
    if operation[-1] == " + ":
        return addition(number1, number2)
    elif operation[-1] == " - ":
        return substraction(number1, number2)
    elif operation[-1] == " x ":
        return multiply(number1, number2)
    elif operation[-1] == " : ":
        return int(division(number1, number2))
