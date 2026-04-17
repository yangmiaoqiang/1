"""Comprehensive tests for string_utils module."""
import pytest
from src.string_utils import (
    count_vowels,
    count_words,
    is_anagram,
    is_palindrome,
    remove_duplicates,
    reverse,
    to_camel_case,
    to_snake_case,
    truncate,
)


class TestReverse:
    def test_regular_string(self):
        assert reverse("hello") == "olleh"

    def test_single_char(self):
        assert reverse("a") == "a"

    def test_empty_string(self):
        assert reverse("") == ""

    def test_palindrome_unchanged(self):
        assert reverse("racecar") == "racecar"

    def test_with_spaces(self):
        assert reverse("hello world") == "dlrow olleh"

    def test_with_numbers(self):
        assert reverse("abc123") == "321cba"


class TestIsPalindrome:
    def test_simple_palindrome(self):
        assert is_palindrome("racecar") is True

    def test_not_palindrome(self):
        assert is_palindrome("hello") is False

    def test_case_insensitive(self):
        assert is_palindrome("Racecar") is True
        assert is_palindrome("Level") is True

    def test_with_spaces(self):
        assert is_palindrome("a man a plan a canal panama") is True

    def test_empty_string(self):
        assert is_palindrome("") is True

    def test_single_char(self):
        assert is_palindrome("a") is True

    def test_two_same_chars(self):
        assert is_palindrome("aa") is True

    def test_two_different_chars(self):
        assert is_palindrome("ab") is False


class TestCountVowels:
    def test_basic(self):
        assert count_vowels("hello") == 2

    def test_all_vowels(self):
        assert count_vowels("aeiou") == 5

    def test_no_vowels(self):
        assert count_vowels("rhythm") == 0

    def test_case_insensitive(self):
        assert count_vowels("HELLO") == 2
        assert count_vowels("AeIoU") == 5

    def test_empty_string(self):
        assert count_vowels("") == 0

    def test_with_numbers_and_symbols(self):
        assert count_vowels("h3ll0!") == 0
        assert count_vowels("a1e2i3") == 3


class TestCountWords:
    def test_single_word(self):
        assert count_words("hello") == 1

    def test_multiple_words(self):
        assert count_words("hello world") == 2
        assert count_words("one two three four") == 4

    def test_empty_string(self):
        assert count_words("") == 0

    def test_extra_spaces(self):
        assert count_words("  hello   world  ") == 2

    def test_single_char_words(self):
        assert count_words("a b c") == 3


class TestTruncate:
    def test_no_truncation_needed(self):
        assert truncate("hello", 10) == "hello"

    def test_exact_length(self):
        assert truncate("hello", 5) == "hello"

    def test_truncation(self):
        assert truncate("hello world", 5) == "hello..."

    def test_custom_suffix(self):
        assert truncate("hello world", 5, suffix="!") == "hello!"

    def test_empty_suffix(self):
        assert truncate("hello world", 5, suffix="") == "hello"

    def test_empty_string(self):
        assert truncate("", 5) == ""

    def test_zero_max_length(self):
        assert truncate("hello", 0) == "..."

    def test_negative_max_length(self):
        with pytest.raises(ValueError, match="non-negative"):
            truncate("hello", -1)


class TestToSnakeCase:
    def test_camel_case(self):
        assert to_snake_case("camelCase") == "camel_case"

    def test_pascal_case(self):
        assert to_snake_case("PascalCase") == "pascal_case"

    def test_already_lower(self):
        assert to_snake_case("lowercase") == "lowercase"

    def test_single_word(self):
        assert to_snake_case("Hello") == "hello"

    def test_multiple_capitals(self):
        assert to_snake_case("myVariableName") == "my_variable_name"

    def test_empty_string(self):
        assert to_snake_case("") == ""


class TestToCamelCase:
    def test_basic(self):
        assert to_camel_case("snake_case") == "snakeCase"

    def test_single_word(self):
        assert to_camel_case("hello") == "hello"

    def test_multiple_parts(self):
        assert to_camel_case("my_variable_name") == "myVariableName"

    def test_empty_string(self):
        assert to_camel_case("") == ""

    def test_leading_underscore(self):
        assert to_camel_case("_private") == "Private"


class TestRemoveDuplicates:
    def test_basic(self):
        assert remove_duplicates("aabbcc") == "abc"

    def test_no_duplicates(self):
        assert remove_duplicates("abc") == "abc"

    def test_empty_string(self):
        assert remove_duplicates("") == ""

    def test_single_char(self):
        assert remove_duplicates("a") == "a"

    def test_all_same(self):
        assert remove_duplicates("aaaa") == "a"

    def test_non_consecutive_duplicates(self):
        assert remove_duplicates("abba") == "aba"

    def test_with_spaces(self):
        assert remove_duplicates("aa  bb") == "a b"


class TestIsAnagram:
    def test_basic_anagram(self):
        assert is_anagram("listen", "silent") is True

    def test_not_anagram(self):
        assert is_anagram("hello", "world") is False

    def test_case_insensitive(self):
        assert is_anagram("Listen", "Silent") is True

    def test_same_string(self):
        assert is_anagram("abc", "abc") is True

    def test_different_lengths(self):
        assert is_anagram("abc", "abcd") is False

    def test_empty_strings(self):
        assert is_anagram("", "") is True

    def test_single_chars(self):
        assert is_anagram("a", "a") is True
        assert is_anagram("a", "b") is False
