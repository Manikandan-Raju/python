# 03_type_hints.py
# Advanced typing: generics, Protocols, and runtime checks.

from typing import List, Dict, Protocol, runtime_checkable


@runtime_checkable
class HasLength(Protocol):
    def __len__(self) -> int:
        ...


def total_length(items: HasLength) -> int:
    return len(items)


print('List length:', total_length([1, 2, 3]))
print('String length:', total_length('hello'))


# Generic function example

def invert_mapping(mapping: Dict[str, int]) -> Dict[int, str]:
    return {value: key for key, value in mapping.items()}


print('Inverted:', invert_mapping({'a': 1, 'b': 2}))
