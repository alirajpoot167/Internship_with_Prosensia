                        ###  String to Integer with Fallback  ###

def string_to_int_with_fallback(input_string, default_value):
    try:
        return int(input_string)
    except ValueError:
        return default_value

# Example usage
print(string_to_int_with_fallback("123", 0))  # Output: 123
print(string_to_int_with_fallback("abc", 0))  # Output: 0

                        ###  Integer to String with Formatting  ###

def int_to_formatted_string(value, format_specifier):
    return format(value, format_specifier)

# Example usage
print(int_to_formatted_string(123, "04d"))       # Output: "0123"
print(int_to_formatted_string(123, ".2e"))       # Output: "1.23e+02"
print(int_to_formatted_string(123, "b"))         # Output: "1111011"

                        ###  Float to Integer with Multiple Rounding Options  ###

import math

def float_to_int_with_rounding(value, strategy):
    if strategy == "up":
        return math.ceil(value)
    elif strategy == "down":
        return math.floor(value)
    elif strategy == "nearest":
        return round(value)
    else:
        raise ValueError("Invalid rounding strategy")

# Example usage
print(float_to_int_with_rounding(5.7, "up"))      # Output: 6
print(float_to_int_with_rounding(5.7, "down"))    # Output: 5
print(float_to_int_with_rounding(5.7, "nearest")) # Output: 6

                        ###  List of Strings to List of Integers with Error Logging  ###

def strings_to_ints_with_logging(strings):
    ints = []
    errors = []
    for s in strings:
        try:
            ints.append(int(s))
        except ValueError as e:
            errors.append((s, str(e)))
    return ints, errors

# Example usage
strings = ["123", "abc", "456", "def"]
ints, errors = strings_to_ints_with_logging(strings)
print(ints)   # Output: [123, 456]
print(errors) # Output: [('abc', 'invalid literal for int() with base 10: 'abc''), ('def', 'invalid literal for int() with base 10: 'def'')]

                        ###  Addition with Type Enforcement  ###

class NotANumberError(Exception):
    pass

def add_numbers(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise NotANumberError("Both inputs must be numbers")
    return a + b

# Example usage
print(add_numbers(5, 3))   # Output: 8
# print(add_numbers(5, "3")) # Raises NotANumberError

                        ###  Cumulative Subtraction with List Validation  ###

class InvalidListError(Exception):
    pass

def cumulative_subtraction(numbers):
    if not all(isinstance(n, (int, float)) for n in numbers):
        raise InvalidListError("All elements must be numbers")
    if len(numbers) < 2:
        raise InvalidListError("List must contain at least two elements")
    result = numbers[0]
    for num in numbers[1:]:
        result -= num
    return result

# Example usage
print(cumulative_subtraction([10, 3, 2]))   # Output: 5
# print(cumulative_subtraction([10, "3", 2])) # Raises InvalidListError

                        ###  Cumulative Subtraction with List Validation  ###

class InvalidListError(Exception):
    pass

def cumulative_subtraction(numbers):
    if not all(isinstance(n, (int, float)) for n in numbers):
        raise InvalidListError("All elements must be numbers")
    if len(numbers) < 2:
        raise InvalidListError("List must contain at least two elements")
    result = numbers[0]
    for num in numbers[1:]:
        result -= num
    return result

# Example usage
print(cumulative_subtraction([10, 3, 2]))   # Output: 5
# print(cumulative_subtraction([10, "3", 2])) # Raises InvalidListError

                        ###   Exponentiation Table  ###

def exponentiation_table(base, exp_range):
    table = []
    for i in range(1, exp_range + 1):
        result = base ** i
        table.append(f"{base}^{i} = {result}")
    return table

# Example usage
print(exponentiation_table(2, 5))
# Output: ['2^1 = 2', '2^2 = 4', '2^3 = 8', '2^4 = 16', '2^5 = 32']

                        ###  Safe Division with Custom Error Handling  ###

class DivisionByZeroError(Exception):
    pass

def safe_division(numerator, denominator, precision):
    if denominator == 0:
        raise DivisionByZeroError("Division by zero is not allowed")
    return round(numerator / denominator, precision)

# Example usage
print(safe_division(10, 3, 2))  # Output: 3.33
# print(safe_division(10, 0, 2))  # Raises DivisionByZeroError

                        ###   Advanced String Split and Conditional Join  ###

def advanced_split_and_join(input_string, delimiter1, delimiter2):
    parts = input_string.split(delimiter1)
    return delimiter2.join([part for part in parts if len(part) > 3])

# Example usage
print(advanced_split_and_join("this,is,a,test,string", ",", ";"))  # Output: "this;test;string"

                        ###  Enhanced Palindrome Check with Character Frequency Analysis  ###

import re
from collections import Counter

def enhanced_palindrome_check(input_string):
    cleaned_string = re.sub(r'[^a-zA-Z0-9]', '', input_string).lower()
    is_palindrome = cleaned_string == cleaned_string[::-1]
    char_frequency = Counter(cleaned_string)
    return is_palindrome, dict(char_frequency)

# Example usage
print(enhanced_palindrome_check("A man, a plan, a canal, Panama!"))
# Output: (True, {'a': 10, 'm': 2, 'n': 4, 'p': 1, 'l': 2, 'c': 1})
