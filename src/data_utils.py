"""Data structure utility functions."""


def flatten(nested):
    """Flatten a nested list into a single list.

    Example:
        flatten([1, [2, [3, 4]], 5]) -> [1, 2, 3, 4, 5]
    """
    result = []
    for item in nested:
        if isinstance(item, list):
            result.extend(flatten(item))
        else:
            result.append(item)
    return result


def chunk(lst, size):
    """Split list lst into chunks of given size.

    Raises:
        ValueError: If size is less than 1.
    """
    if size < 1:
        raise ValueError("size must be at least 1")
    return [lst[i:i + size] for i in range(0, len(lst), size)]


def unique(lst):
    """Return a list with duplicate elements removed, preserving order."""
    seen = set()
    result = []
    for item in lst:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result


def group_by(lst, key_func):
    """Group elements of lst by the result of key_func.

    Returns:
        dict mapping key -> list of elements with that key.
    """
    result = {}
    for item in lst:
        key = key_func(item)
        result.setdefault(key, []).append(item)
    return result


def merge_dicts(*dicts):
    """Merge multiple dictionaries. Later dicts override earlier ones."""
    result = {}
    for d in dicts:
        result.update(d)
    return result


def deep_get(d, *keys, default=None):
    """Safely retrieve a nested value from a dictionary.

    Example:
        deep_get({"a": {"b": 1}}, "a", "b") -> 1
        deep_get({"a": {}}, "a", "missing") -> None
    """
    current = d
    for key in keys:
        if not isinstance(current, dict):
            return default
        current = current.get(key, default)
        if current is default:
            return default
    return current


def frequency(lst):
    """Return a dict mapping each element to its occurrence count."""
    result = {}
    for item in lst:
        result[item] = result.get(item, 0) + 1
    return result
