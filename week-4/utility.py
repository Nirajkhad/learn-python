"""
This module provides simple function library for common tasks.

What this program will do:
1. Capitalize a word
2. Reverse a word
3. Sort a word
4. Reverse sort a word
5. Add numbers
6. Show user info

How to use:
1. Run the program using 'python3 week-4/utility.py' command.
2. The program will display the results.

"""

# Capitalize a word
def capitalize(word):
    return word.capitalize();

# Reverse a word
def reverse(word):
    return word[::-1];

# Sort a word
def sort(word):
    return "".join(sorted(word));

# Reverse sort a word
def reverse_sort(word):
    return "".join(sorted(word, reverse=True));

# Add numbers
def add_numbers(*args):
    return sum(args);

# Show user info
def show_info(**args):
    return args

def main():
    print(capitalize("hello"))
    print(reverse("hello"))
    print(sort("Hello my name is Niraj"))
    print(reverse_sort("Hello my name is Niraj"))
    print(add_numbers(1, 2, 3, 4, 5))
    print(show_info(name="Niraj", age=20))  

main()