def safe_divide(numerator,denominator):
    try:
        float_numerator = float(numerator)
        float_denominator = float(denominator)
        return f"The result of the division is {float_numerator / float_denominator}"
    except ValueError:
        return "Error: Please enter numeric values only."
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."