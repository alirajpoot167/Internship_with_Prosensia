    # Task 1. Concatenation and Conversion

def concatenate_and_convert(str1, str2):
    concatenated = str1 + str2
    if concatenated.isdigit():
        return int(concatenated)
    return concatenated

    # Task 2. String Indexing

def get_char_at_index(s, index):
    try:
        return s[index]
    except IndexError:
        return "Index out of bounds"

    # Task 3. String Length

def string_lengths(str_list):
    return [len(s) for s in str_list]

    # Task 4. Looping Through Strings

def print_characters_with_index(s):
    for index, char in enumerate(s):
        print(f"Index {index}: {char}")

    # Task 5. Character Counting

def count_character(s, char):
    return s.count(char)

    # Task 6. String Slicing

def substring(s, start, end):
    # Adjust indices to be within valid range
    start = max(0, start)
    end = min(len(s), end)
    return s[start:end]

    # Task 7. String Comparison

def compare_strings(str1, str2):
    if str1 < str2:
        return "The first string comes before the second string."
    elif str1 > str2:
        return "The first string comes after the second string."
    else:
        return "Both strings are equal."

    # Task 8. String Methods

def transform_string(s):
    return {
        "lowercase": s.lower(),
        "uppercase": s.upper(),
        "titlecase": s.title()
    }

    # Task 9. Search and Replace

def search_and_replace(s, search_term, replacement_term):
    return s.replace(search_term, replacement_term)

    # Task 10. Whitespace Removal

def remove_whitespace(s):
    return ' '.join(s.split())

