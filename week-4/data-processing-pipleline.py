"""
This module provides a simple data pipeline:

Whart this program will do:
1. Filter even numbers from a list.
2. Compute their squares.
3. Index and print the combined results.

How to use:
1. Run the program using 'python3 week-4/data-processing-pipleline.py' command.
2. The program will display the results.
"""

# Return a list of even integers from the input.
def get_even_numbers(numbers):
    return [x for x in numbers if x % 2 == 0]

# Return a list of squares for the input numbers.
def compute_squares(numbers):
    return [x * x for x in numbers]

# Pair each original number with its square, then add a 1-based index.
def build_indexed_pairs(orig_numbers, squared_numbers):
    return [
        (idx, orig, sq)
        for idx, (orig, sq) in enumerate(zip(orig_numbers, squared_numbers), start=1)
    ]

# Print each (index, original, square) tuple in a friendly format.
def display_results(indexed_data):
    for idx, orig, sq in indexed_data:
        print(f"Index: {idx}, Number: {orig}, Square: {sq}")


def main():
    numbers = [1, 2, 3, 4, 5, 6]
    even_numbers = get_even_numbers(numbers)
    squares = compute_squares(even_numbers)
    indexed_pairs = build_indexed_pairs(even_numbers, squares)
    display_results(indexed_pairs)
    
main()
