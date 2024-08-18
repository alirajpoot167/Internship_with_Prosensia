# 1. Tuple Basics
names = ('Alice', 'Bob', 'Charlie')
print(names[1])  

# 2. Tuple and Max Function
def max_in_tuple(t):
    return max(t)
numbers = (4, 7, 1)
print(max_in_tuple(numbers))  

# 3. Immutable Property
fruits = ('apple', 'banana', 'cherry')
print("Tuples are immutable, you can't change their elements.")
print("For example, trying to change 'banana' to 'orange' will raise an error.")

# 4. Tuple Operations
my_list = [1, 2, 3]
my_tuple = (1, 2, 3)
print("Tuples don't have an append method, you can't add elements to them.")
print("For example, trying to append 4 to my_tuple will raise an error.")
my_list.append(4)
print(my_list)  

# 5. Tuple Assignment
def swap_values(a, b):
    return b, a
a = 5
b = 10
a, b = swap_values(a, b)
print(f"a = {a}, b = {b}") 

# 6. Dictionary and Tuples
def dict_to_tuples(d):
    return list(d.items())
my_dict = {'x': 1, 'y': 2, 'z': 3}
print(dict_to_tuples(my_dict))  

# 7. Sorting Tuples
def sort_dict_by_values(d):
    return sorted(d.items(), key=lambda x: x[1], reverse=True)
my_dict = {'a': 10, 'b': 1, 'c': 22}
print(sort_dict_by_values(my_dict))

# 8. Tuple Comparison
def compare_tuples(t1, t2):
    return [a == b for a, b in zip(t1, t2)]
t1 = (1, 2, 3)
t2 = (3, 2, 1)
print(compare_tuples(t1, t2))  

# 9. Top N Frequent Words
import collections
import re
def top_n_frequent_words(file_name, n):
    with open(file_name, 'r') as f:
        text = f.read()
    words = re.findall(r'\b\w+\b', text.lower())
    word_counts = collections.Counter(words)
    return word_counts.most_common(n)
print(top_n_frequent_words('romeo.txt', 3)) 

# 10. List Comprehension with Tuples
def dict_to_sorted_tuples(d):
    return sorted((v, k) for k, v in d.items())
my_dict = {'a': 10, 'b': 1, 'c': 22}
print(dict_to_sorted_tuples(my_dict)) 