"""String utility functions."""


def reverse(s):
    """Return the reversed version of string s."""
    return s[::-1]


def is_palindrome(s):
    """Return True if s is a palindrome (case-insensitive, ignoring spaces)."""
    cleaned = s.replace(" ", "").lower()
    return cleaned == cleaned[::-1]


def count_vowels(s):
    """Return the number of vowels in string s (case-insensitive)."""
    return sum(1 for ch in s.lower() if ch in "aeiou")


def count_words(s):
    """Return the number of words in string s."""
    return len(s.split())


def truncate(s, max_length, suffix="..."):
    """Truncate string s to max_length characters, appending suffix if truncated.

    Raises:
        ValueError: If max_length is negative.
    """
    if max_length < 0:
        raise ValueError("max_length must be non-negative")
    if len(s) <= max_length:
        return s
    return s[:max_length] + suffix


def to_snake_case(s):
    """Convert a camelCase or PascalCase string to snake_case."""
    result = []
    for i, ch in enumerate(s):
        if ch.isupper() and i > 0:
            result.append("_")
        result.append(ch.lower())
    return "".join(result)


def to_camel_case(s):
    """Convert a snake_case string to camelCase."""
    parts = s.split("_")
    return parts[0] + "".join(word.capitalize() for word in parts[1:])


def remove_duplicates(s):
    """Return s with consecutive duplicate characters removed."""
    if not s:
        return s
    result = [s[0]]
    for ch in s[1:]:
        if ch != result[-1]:
            result.append(ch)
    return "".join(result)


def is_anagram(s1, s2):
    """Return True if s1 and s2 are anagrams of each other (case-insensitive)."""
    return sorted(s1.lower()) == sorted(s2.lower())
