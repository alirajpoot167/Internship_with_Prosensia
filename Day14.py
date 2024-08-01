### Complex Number Conversion and Operations  ###

def complex_operations(complex_str, complex_num):
    try:
        c1 = complex(complex_str)
        c2 = complex(complex_num)
        addition = c1 + c2
        subtraction = c1 - c2
        multiplication = c1 * c2
        division = c1 / c2
        return (addition, subtraction, multiplication, division)
    except ValueError as e:
        return f"Error converting input to complex number: {e}"
    except ZeroDivisionError as e:
        return f"Error in division: {e}"

# Example usage:
result = complex_operations("3+4j", "1+2j")
print(result)

###  Binary String to Integer and Back ###

def binary_conversion(binary_str, fixed_length):
    try:
        integer_value = int(binary_str, 2)
        binary_str_back = bin(integer_value)[2:].zfill(fixed_length)
        return binary_str_back
    except ValueError as e:
        return f"Error converting binary string: {e}"

# Example usage:
binary_result = binary_conversion("1011", 8)
print(binary_result)

###  Dictionary to JSON String and Back with Error Handling ###

import json

def dict_to_json_and_back(dictionary):
    try:
        json_str = json.dumps(dictionary)
        dict_back = json.loads(json_str)
        return dict_back
    except (TypeError, json.JSONDecodeError) as e:
        return {"original_input": dictionary, "error": str(e)}

# Example usage:
json_result = dict_to_json_and_back({"key": "value"})
print(json_result)

### Matrix Addition with Type and Dimension Enforcement  ###

class MatrixDimensionError(Exception):
    pass

class MatrixTypeError(Exception):
    pass

def matrix_addition(matrix1, matrix2):
    if not all(isinstance(i, list) for i in (matrix1 + matrix2)):
        raise MatrixTypeError("All elements must be lists.")
    
    if len(matrix1) != len(matrix2) or any(len(row1) != len(row2) for row1, row2 in zip(matrix1, matrix2)):
        raise MatrixDimensionError("Matrices must have the same dimensions.")
    
    if not all(isinstance(element, (int, float)) for row in matrix1 + matrix2 for element in row):
        raise MatrixTypeError("All elements must be numbers.")
    
    result = [[a + b for a, b in zip(row1, row2)] for row1, row2 in zip(matrix1, matrix2)]
    return result

# Example usage:
matrix_result = matrix_addition([[1, 2], [3, 4]], [[5, 6], [7, 8]])
print(matrix_result)

### Prime Factorization with Cumulative Multiplication  ###

def prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors

def prime_factors_with_multiplication(n):
    factors = prime_factors(n)
    cumulative_product = 1
    for factor in factors:
        cumulative_product *= factor
    return factors, cumulative_product

# Example usage:
prime_result = prime_factors_with_multiplication(28)
print(prime_result)

###  Formatted String Interpolation with Custom Placeholders  ###

def interpolate_string(template, values):
    for key, value in values.items():
        template = template.replace(f"{{{key}}}", str(value))
    return template

# Example usage:
formatted_string = interpolate_string("Hello, {name}! You are {age} years old.", {"name": "Alice", "age": 30})
print(formatted_string)

###  Advanced Anagram Check with Frequency Analysis  ###

import re
from collections import Counter

def clean_string(s):
    return re.sub(r'[^A-Za-z0-9]', '', s).lower()

def are_anagrams(str1, str2):
    cleaned_str1 = clean_string(str1)
    cleaned_str2 = clean_string(str2)
    return Counter(cleaned_str1) == Counter(cleaned_str2)

def anagram_check_with_frequency(str1, str2):
    cleaned_str1 = clean_string(str1)
    cleaned_str2 = clean_string(str2)
    freq1 = Counter(cleaned_str1)
    freq2 = Counter(cleaned_str2)
    return are_anagrams(str1, str2), {"freq1": dict(freq1), "freq2": dict(freq2)}

# Example usage:
anagram_result = anagram_check_with_frequency("Astronomer", "Moon starer")
print(anagram_result)

### Nested Data Structure Flattening with Type Preservation   ###

def flatten(nested_list):
    flat_list = []
    max_depth = 1
    def flatten_helper(lst, depth):
        nonlocal max_depth
        if depth > max_depth:
            max_depth = depth
        for item in lst:
            if isinstance(item, list):
                flatten_helper(item, depth + 1)
            else:
                flat_list.append(item)
    flatten_helper(nested_list, 1)
    return flat_list, max_depth

# Example usage:
flatten_result = flatten([1, [2, [3, [4]], 5]])
print(flatten_result)

###   String and Number Pattern Matching  ###

import re

def match_pattern(string, pattern):
    regex_pattern = ''.join(['[A-Za-z]' if c.isalpha() else '[0-9]' for c in pattern])
    return bool(re.fullmatch(regex_pattern, string))

# Example usage:
pattern_result = match_pattern("a1b2", "a1b2")
print(pattern_result)

###  Data Normalization and Statistical Analysis  ###

import statistics

class NonNumericError(Exception):
    pass

class EmptyListError(Exception):
    pass

def normalize_and_analyze(numbers):
    if not numbers:
        raise EmptyListError("Input list is empty.")
    
    if not all(isinstance(num, (int, float)) for num in numbers):
        raise NonNumericError("All elements must be numbers.")
    
    min_val = min(numbers)
    max_val = max(numbers)
    range_val = max_val - min_val
    
    normalized = [(num - min_val) / range_val for num in numbers]
    
    mean_val = statistics.mean(normalized)
    median_val = statistics.median(normalized)
    variance_val = statistics.variance(normalized)
    
    return {
        "normalized": normalized,
        "mean": mean_val,
        "median": median_val,
        "variance": variance_val
    }

# Example usage:
stats_result = normalize_and_analyze([1, 2, 3, 4, 5])
print(stats_result)

