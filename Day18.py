# Create an empty dictionary
my_dict = {}

# Add three key-value pairs to the dictionary
my_dict['key1'] = 'value1'
my_dict['key2'] = 'value2'
my_dict['key3'] = 'value3'

# Print the dictionary
print(my_dict)

def get_value(my_dict, key):
    if key in my_dict:
        print(my_dict[key])
    else:
        print(f"The key '{key}' is not found.")

# Example dictionary
example_dict = {'a': 1, 'b': 2, 'c': 3}

# Test the function
get_value(example_dict, 'b')  # Should print 2
get_value(example_dict, 'd')  # Should print a key not found message

# Example dictionary
example_dict = {'a': 1, 'b': 2, 'c': 3}

# Print the dictionary before the update
print("Before update:", example_dict)

# Update the value of a specific key
example_dict['b'] = 20

# Print the dictionary after the update
print("After update:", example_dict)

# Read a line of text from the user
line_of_text = input("Enter a line of text: ")

# Split the line into words
words = line_of_text.split()

# Create a dictionary to count word occurrences
word_count = {}

# Count the occurrences of each word
for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

# Print the dictionary of word counts
print(word_count)

def print_keys_values(my_dict):
    keys = list(my_dict.keys())
    values = list(my_dict.values())
    print("Keys:", keys)
    print("Values:", values)

# Example dictionary
example_dict = {'a': 1, 'b': 2, 'c': 3}

# Test the function
print_keys_values(example_dict)

# Example dictionary
example_dict = {'a': 1, 'b': 2, 'c': 3}

# Retrieve the value for a specified key
key = 'd'
value = example_dict.get(key, 0)

# Print the value
print(f"The value for key '{key}' is {value}")

# Create a nested dictionary for multiple students
students = {
    'student1': {
        'name': 'Alice',
        'age': 20,
        'grades': {
            'Math': 90,
            'Science': 85,
            'English': 88
        }
    },
    'student2': {
        'name': 'Bob',
        'age': 22,
        'grades': {
            'Math': 78,
            'Science': 82,
            'English': 80
        }
    }
}

# Print the nested dictionary
print(students)

def merge_dicts(dict1, dict2):
    merged_dict = dict1.copy()
    merged_dict.update(dict2)
    return merged_dict

# Example dictionaries
dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b': 20, 'd': 4}

# Merge the dictionaries
result_dict = merge_dicts(dict1, dict2)

# Print the resulting dictionary
print(result_dict)

# Example dictionary
example_dict = {'a': 1, 'b': 2, 'c': 3}

# Attempt to access a non-existent key
try:
    value = example_dict['d']
except KeyError:
    print("Error: The key 'd' does not exist in the dictionary.")


def find_most_common_word(file_path):
    # Initialize an empty dictionary to count word occurrences
    word_count = {}

    # Read the file
    with open(file_path, 'r') as file:
        for line in file:
            words = line.split()
            for word in words:
                word = word.lower().strip('.,!?;"()')
                if word in word_count:
                    word_count[word] += 1
                else:
                    word_count[word] = 1

    # Find the word with the highest count
    most_common_word = max(word_count, key=word_count.get)
    count = word_count[most_common_word]

    # Print the most common word and its count
    print(f"The most common word is '{most_common_word}' with {count} occurrences.")

# Example usage
file_path = 'example.txt'
find_most_common_word(file_path)
