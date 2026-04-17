"""Comprehensive tests for data_utils module."""
import pytest
from src.data_utils import (
    chunk,
    deep_get,
    flatten,
    frequency,
    group_by,
    merge_dicts,
    unique,
)


class TestFlatten:
    def test_already_flat(self):
        assert flatten([1, 2, 3]) == [1, 2, 3]

    def test_one_level_nested(self):
        assert flatten([1, [2, 3], 4]) == [1, 2, 3, 4]

    def test_deeply_nested(self):
        assert flatten([1, [2, [3, [4]]]]) == [1, 2, 3, 4]

    def test_empty_list(self):
        assert flatten([]) == []

    def test_nested_empty_lists(self):
        assert flatten([[], [1, 2], []]) == [1, 2]

    def test_mixed_types(self):
        assert flatten([1, ["a", [True]]]) == [1, "a", True]

    def test_single_nested(self):
        assert flatten([[1, 2, 3]]) == [1, 2, 3]


class TestChunk:
    def test_even_split(self):
        assert chunk([1, 2, 3, 4], 2) == [[1, 2], [3, 4]]

    def test_uneven_split(self):
        assert chunk([1, 2, 3, 4, 5], 2) == [[1, 2], [3, 4], [5]]

    def test_chunk_size_one(self):
        assert chunk([1, 2, 3], 1) == [[1], [2], [3]]

    def test_chunk_larger_than_list(self):
        assert chunk([1, 2], 5) == [[1, 2]]

    def test_empty_list(self):
        assert chunk([], 3) == []

    def test_chunk_size_zero(self):
        with pytest.raises(ValueError, match="at least 1"):
            chunk([1, 2, 3], 0)

    def test_chunk_size_negative(self):
        with pytest.raises(ValueError):
            chunk([1, 2, 3], -1)

    def test_exact_size(self):
        assert chunk([1, 2, 3], 3) == [[1, 2, 3]]


class TestUnique:
    def test_no_duplicates(self):
        assert unique([1, 2, 3]) == [1, 2, 3]

    def test_with_duplicates(self):
        assert unique([1, 2, 2, 3, 1]) == [1, 2, 3]

    def test_all_duplicates(self):
        assert unique([1, 1, 1]) == [1]

    def test_empty_list(self):
        assert unique([]) == []

    def test_single_element(self):
        assert unique([42]) == [42]

    def test_preserves_order(self):
        assert unique([3, 1, 2, 1, 3]) == [3, 1, 2]

    def test_strings(self):
        assert unique(["a", "b", "a", "c"]) == ["a", "b", "c"]

    def test_mixed_types(self):
        assert unique([1, "1", 1, "1"]) == [1, "1"]


class TestGroupBy:
    def test_group_by_length(self):
        result = group_by(["cat", "dog", "ant", "elephant"], len)
        assert result == {3: ["cat", "dog", "ant"], 8: ["elephant"]}

    def test_group_by_parity(self):
        result = group_by([1, 2, 3, 4, 5], lambda x: x % 2)
        assert result[0] == [2, 4]
        assert result[1] == [1, 3, 5]

    def test_empty_list(self):
        assert group_by([], str) == {}

    def test_all_same_key(self):
        result = group_by([1, 2, 3], lambda _: "all")
        assert result == {"all": [1, 2, 3]}

    def test_all_unique_keys(self):
        result = group_by([1, 2, 3], lambda x: x)
        assert result == {1: [1], 2: [2], 3: [3]}

    def test_group_dicts_by_field(self):
        data = [{"type": "a", "v": 1}, {"type": "b", "v": 2}, {"type": "a", "v": 3}]
        result = group_by(data, lambda d: d["type"])
        assert len(result["a"]) == 2
        assert len(result["b"]) == 1


class TestMergeDicts:
    def test_no_overlap(self):
        assert merge_dicts({"a": 1}, {"b": 2}) == {"a": 1, "b": 2}

    def test_overlap_later_wins(self):
        assert merge_dicts({"a": 1}, {"a": 2}) == {"a": 2}

    def test_three_dicts(self):
        result = merge_dicts({"a": 1}, {"b": 2}, {"c": 3})
        assert result == {"a": 1, "b": 2, "c": 3}

    def test_empty_dicts(self):
        assert merge_dicts({}, {}) == {}
        assert merge_dicts({"a": 1}, {}) == {"a": 1}
        assert merge_dicts({}, {"a": 1}) == {"a": 1}

    def test_single_dict(self):
        assert merge_dicts({"a": 1, "b": 2}) == {"a": 1, "b": 2}

    def test_no_dicts(self):
        assert merge_dicts() == {}

    def test_override_chain(self):
        result = merge_dicts({"x": 1}, {"x": 2}, {"x": 3})
        assert result["x"] == 3


class TestDeepGet:
    def test_single_level(self):
        assert deep_get({"a": 1}, "a") == 1

    def test_two_levels(self):
        assert deep_get({"a": {"b": 2}}, "a", "b") == 2

    def test_missing_key(self):
        assert deep_get({"a": 1}, "b") is None

    def test_missing_nested_key(self):
        assert deep_get({"a": {}}, "a", "b") is None

    def test_custom_default(self):
        assert deep_get({"a": 1}, "b", default=42) == 42

    def test_value_is_none(self):
        assert deep_get({"a": None}, "a") is None

    def test_non_dict_intermediate(self):
        assert deep_get({"a": "string"}, "a", "b") is None

    def test_empty_dict(self):
        assert deep_get({}, "a") is None

    def test_deeply_nested(self):
        d = {"a": {"b": {"c": {"d": 99}}}}
        assert deep_get(d, "a", "b", "c", "d") == 99


class TestFrequency:
    def test_basic(self):
        result = frequency([1, 2, 2, 3, 3, 3])
        assert result == {1: 1, 2: 2, 3: 3}

    def test_all_unique(self):
        result = frequency([1, 2, 3])
        assert result == {1: 1, 2: 1, 3: 1}

    def test_all_same(self):
        result = frequency([5, 5, 5])
        assert result == {5: 3}

    def test_empty_list(self):
        assert frequency([]) == {}

    def test_strings(self):
        result = frequency(["a", "b", "a"])
        assert result == {"a": 2, "b": 1}

    def test_single_element(self):
        assert frequency([42]) == {42: 1}
