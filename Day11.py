                                 ### Data Type Conversion Tasks ###

    # 1. Convert String to Integer

def string_to_int(s):    # Function named as string_to_int
    try:
        return int(s)    # loop chalti rehay ge jab tak value milti raha ge
    except ValueError:   # Agr integer ka ilawa kuch aur datatype a jay to None show karo
        return None
    
    
print(string_to_int("789"))   # Output 123
print(string_to_int("xyz"))   # Output None   because No Integer here
print(string_to_int("44.44")) # Output None   because No Integer here
    
    # Convert Integer to String

def int_to_string(n):
    return str(n)

# Example usage:
print(int_to_string(123))  # Output: "123"
print(int_to_string(0))    # Output: "0"
print(int_to_string(-456)) # Output: "-456"

    # Convert Float to Integer

def float_to_int(f):
    return int(f)

# Example usage:
print(float_to_int(123.45))  # Output: 123
print(float_to_int(0.99))    # Output: 0
print(float_to_int(-456.78)) # Output: -457

    #  Convert List of Strings to List of Integers 

def list_of_strings_to_list_of_ints(lst):
    result = []
    for s in lst:
        try:
            result.append(int(s))
        except ValueError:
            continue
    return result

# Example usage:
print(list_of_strings_to_list_of_ints(["123", "456", "abc", "789"]))  # Output: [123, 456, 789]
print(list_of_strings_to_list_of_ints(["10", "20.5", "30", "xyz"]))   # Output: [10, 30]

                                    ###  Arithmetic Operations  ###

    # Addition of Two Numbers
    
def add_numbers(a, b):
    return a + b

# Example usage:
print(add_numbers(5, 3))  # Output: 8
print(add_numbers(-1, 4)) # Output: 3

    # Subtraction of Two Numbers
    
def subtract_numbers(a, b):
    return a - b

# Example usage:
print(subtract_numbers(5, 3))  # Output: 2
print(subtract_numbers(4, 10)) # Output: -6

    # Multiplication of Two Numbers

def multiply_numbers(a, b):
    return a * b

# Example usage:
print(multiply_numbers(5, 3))  # Output: 15
print(multiply_numbers(-1, 4)) # Output: -4

    # Division of Two Numbers
    
def divide_numbers(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return None

# Example usage:
print(divide_numbers(6, 3))  # Output: 2.0
print(divide_numbers(5, 0))  # Output: None

                                    ###  String Operations  ###

    #  Concatenate Two Strings
    
def concatenate_strings(s1, s2):
    return s1 + s2

# Example usage:
print(concatenate_strings("Hello, ", "world!"))  # Output: "Hello, world!"
print(concatenate_strings("foo", "bar"))         # Output: "foobar"
  
    #  Reverse a String

def reverse_string(s):
    return s[::-1]

# Example usage:
print(reverse_string("hello"))  # Output: "olleh"
print(reverse_string("Python")) # Output: "nohtyP"