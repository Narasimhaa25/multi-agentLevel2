# calculator_tool.py
import re

def calculate(user_input: str):
    """
    Perform basic arithmetic based on natural language or operators.
    Supports:
    - Addition: add, plus, sum, and
    - Subtraction: subtract, minus, difference of
    - Multiplication: multiply, times
    - Division: divide, by
    """
    user_input = user_input.lower()

    # Map words/phrases to operators
    replacements = {
        r"\b(add|plus|sum)\b": "+",
        r"\b(and)\b": "+",
        r"\b(subtract|minus|difference of)\b": "-",
        r"\b(multiply|times)\b": "*",
        r"\b(divide|by)\b": "/"
    }

    for pattern, symbol in replacements.items():
        user_input = re.sub(pattern, symbol, user_input)

    # Extract only numbers and operators
    match = re.findall(r"[0-9\+\-\*/]+", user_input)
    if not match:
        return "Could not detect a valid arithmetic expression."

    # Join all parts into a single expression
    expr = "".join(match)

    try:
        result = eval(expr)
        return f"Result: {result}"
    except Exception as e:
        return f"Error: {e}"