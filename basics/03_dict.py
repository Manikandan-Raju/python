"""basics/dict.py

Executable study notes: concise examples with explanatory comments.

Run this file directly to see outputs demonstrating:
- ascii letters listing
- dictionary creation with `enumerate` and dict comprehension
- merging dictionaries using unpacking
- list unpacking/extension
- counting character frequencies (pandas if available, else Counter)
- slicing behavior with step and negative step

This file is written to be safe if `pandas` is not installed.
"""

import string
from collections import Counter

try:
	import pandas as pd
	_HAS_PANDAS = True
except Exception:
	pd = None
	_HAS_PANDAS = False


def show_ascii_letters():
	# `string.ascii_letters` contains lowercase + uppercase ASCII letters
	letters = list(string.ascii_letters)
	print("ASCII letters (sample):", letters[:10], "...")
	return letters


def dict_from_enumerate():
	# Create a mapping from lowercase letter -> index using enumerate
	# dict comprehension: {key_expr: value_expr for ...}
	mapping = {char: idx for idx, char in enumerate(string.ascii_lowercase)}
	print("Example mapping (a->0, b->1, ...):", dict(list(mapping.items())[:6]))
	return mapping


def merge_dict_example(base_mapping):
	# Merge additional key-value pairs into a dict using unpacking `{**d1, **d2}`
	merged = {**base_mapping, 'yes': 1}
	print("Merged dictionary sample:", dict(list(merged.items())[:6]), "...", "plus 'yes':", merged.get('yes'))
	return merged


def list_unpack_example():
	# Use iterable unpacking to extend a list: [*old_list, new_item]
	numbers = [1, 2, 3]
	numbers = [*numbers, 4]  # creates a new list with 4 appended
	print("List after unpack/append:", numbers)
	return numbers


def value_counts_example(text):
	# Count characters in a string. Prefer pandas.Series.value_counts() for nice display
	chars = list(text)
	if _HAS_PANDAS:
		series = pd.Series(chars)
		print("Character frequencies (pandas.Series.value_counts):")
		print(series.value_counts())
	else:
		counts = Counter(chars)
		print("Character frequencies (collections.Counter):")
		for char, cnt in counts.most_common():
			print(f"{char}: {cnt}")


def slicing_examples():
	# Demonstrate slicing with negative step and different start/stop
	# Build an example list long enough for the slice used below
	lst = list(range(1, 11))  # [1,2,...,10]
	# Explanation: lst[7:2:-1] starts at index 7 (value 8), stops before index 2 (value 3), stepping -1
	# So it yields [8,7,6,5,4]
	example_slice = lst[7:2:-1]
	print("Example list:", lst)
	print("Slice lst[7:2:-1] ->", example_slice)
	return example_slice


def main():
	# Run each example in sequence with short comments printed above
	print("--- ASCII letters ---")
	show_ascii_letters()

	print("\n--- Dictionary from enumerate ---")
	mapping = dict_from_enumerate()

	print("\n--- Merge dict example ---")
	merge_dict_example(mapping)

	print("\n--- List unpack example ---")
	list_unpack_example()

	print("\n--- Character frequency example ---")
	sample = 'manikandan'
	value_counts_example(sample)

	print("\n--- Slicing examples ---")
	slicing_examples()


if __name__ == "__main__":
	main()