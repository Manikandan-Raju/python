"""Slicing examples and safe iteration notes.

This file demonstrates common slice operations, negative indices,
step values, and the difference between slicing (safe) and indexing
(which can raise IndexError). It also shows a safe pattern to iterate
with bounds checking.
"""

my_list = ['p', 'r', 'o', 'g', 'r', 'a', 'm']


def show_examples():
    print("my_list:", my_list)

    # Basic slices
    print("my_list[2:5] ->", my_list[2:5])        # -> ['o', 'g', 'r']
    print("my_list[5:]  ->", my_list[5:])         # -> ['a', 'm']
    print("my_list[:]   ->", my_list[:])          # -> ['p', 'r', 'o', 'g', 'r', 'a', 'm']

    # Negative indices: -1 is last element

    print("my_list[-3::1] ->", my_list[-3::1])    # -> ['r', 'a', 'm'] (third-last to end)
    print("my_list[-3::-1] ->", my_list[-3::-1])  # -> ['r', 'g', 'o', 'r', 'p'] (third-last backwards)
    print("my_list[::2] ->", my_list[::2])        # -> ['p', 'o', 'r', 'm'] (every second element)
    print("my_list[::-2] ->", my_list[::-2])        # -> ['m', 'a', 'r', 'p'] (every second element)
    print("my_list[:0:-2] ->", my_list[:0:-2])        # -> ['m', 'a', 'r', 'p'] (every second element)




    # Out-of-range slice boundaries are handled gracefully (no IndexError)
    print("my_list[1:15] ->", my_list[1:15])      # -> ['r', 'o', 'g', 'r', 'a', 'm']

    # Various step examples
    print("my_list[:-3:1] ->", my_list[:-3:1])    # -> ['p', 'r', 'o', 'g'] (up to index -3)
    print("my_list[:-3:-1] ->", my_list[:-3:-1])  # -> ['m', 'a'] (from end backwards until before -3)
    print("my_list[0:-3:1] ->", my_list[0:-3:1])  # -> ['p', 'r', 'o', 'g']
    print("my_list[-3:-7:-2] ->", my_list[-3:-7:-2])  # -> ['r', 'o']
    print("my_list[-8:-3:1] ->", my_list[-8:-3:1])  # -> ['p', 'r', 'o', 'g'] (out-of-range start treated as 0)
    print("my_list[-6:-3:1] ->", my_list[-6:-3:1])  # -> ['p', 'r', 'o', 'g'] (out-of-range start treated as 0)
    print("my_list[6:1:1] ->", my_list[6:1:1])  # -> ['r', 'g', 'o'] (reverse-order slice from index4 down to index2)
    print("my_list[6:1:2] ->", my_list[6:1:2])  # -> ['r', 'g', 'o'] (reverse-order slice from index4 down to index2)
    print("my_list[4:1:-1] ->", my_list[4:1:-1])  # -> ['r', 'g', 'o'] (reverse-order slice from index4 down to index2)


def safe_index_iteration():
    # Demonstrate safe access vs unsafe indexing
    print("\nIteration with safe indexing (using enumerate and try/except):")
    for i in range(15):
        try:
            value = my_list[i]
        except IndexError:
            print(f"Index {i} is out of range; stopping iteration.")
            break
        print(f"index {i}: {value}")


def main():
    show_examples()
    safe_index_iteration()


if __name__ == '__main__':
    main()
