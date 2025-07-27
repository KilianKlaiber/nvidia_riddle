import pytest
from main import find_shortest_substring, length, get_first_character


class TestFindShortestSubstring:
    """Test cases for the find_shortest_substring function."""

    def test_basic_case(self):
        """Test the basic example from the problem."""
        result = find_shortest_substring("ADOBECODEBANC", "ABC")
        assert result == "BANC"

    def test_exact_match(self):
        """Test when the entire text is the minimum window."""
        result = find_shortest_substring("ABC", "ABC")
        assert result == "ABC"

    def test_reverse_order(self):
        """Test when target letters appear in reverse order."""
        result = find_shortest_substring("CBA", "ABC")
        assert result == "CBA"

    def test_single_character(self):
        """Test with single character target."""
        result = find_shortest_substring("HELLO", "L")
        assert result == "L"

    def test_target_at_beginning(self):
        """Test when optimal window is at the beginning."""
        result = find_shortest_substring("ABCDEFGH", "ABC")
        assert result == "ABC"

    def test_target_at_end(self):
        """Test when optimal window is at the end."""
        result = find_shortest_substring("XYZABC", "ABC")
        assert result == "ABC"

    def test_scattered_letters(self):
        """Test with letters scattered throughout text."""
        result = find_shortest_substring("AXBYCZD", "ABC")
        assert result == "AXBYC"

    def test_multiple_valid_windows(self):
        """Test that algorithm finds the shortest among multiple valid windows."""
        # First ABC: positions 0,1,2 (length 3)
        # Second window: A at 3, B at 4, C at 2 -> BAC positions 2,3,4 (length 3)
        # Both have same length, should return first found
        result = find_shortest_substring("ABCABC", "ABC")
        assert result == "ABC"  # First occurrence

    def test_overlapping_solution(self):
        """Test case where letters overlap in optimal solution."""
        result = find_shortest_substring("AABBC", "ABC")
        assert result == "ABBC"

    def test_case_sensitivity(self):
        """Test that the algorithm is case sensitive."""
        result = find_shortest_substring("AaBbCc", "ABC")
        assert result == "AaBbC"


class TestEdgeCases:
    """Test edge cases and error conditions."""

    def test_empty_text(self):
        """Test with empty text string."""
        with pytest.raises(
            ValueError, match="Both text and target_letters must be non-empty"
        ):
            find_shortest_substring("", "ABC")

    def test_empty_target(self):
        """Test with empty target string."""
        with pytest.raises(
            ValueError, match="Both text and target_letters must be non-empty"
        ):
            find_shortest_substring("HELLO", "")

    def test_both_empty(self):
        """Test with both strings empty."""
        with pytest.raises(
            ValueError, match="Both text and target_letters must be non-empty"
        ):
            find_shortest_substring("", "")

    def test_missing_character(self):
        """Test when target contains character not in text."""
        with pytest.raises(
            ValueError, match="No substring found containing all letters: ABCZ"
        ):
            find_shortest_substring("ADOBECODEBANC", "ABCZ")


    def test_no_solution_short_text(self):
        """Test when text is shorter than target."""
        with pytest.raises(
            ValueError, match="No substring found containing all letters: ABCD"
        ):
            find_shortest_substring("ABC", "ABCD")


class TestHelperFunctions:
    """Test the helper functions used by the main algorithm."""

    def test_length_function(self):
        """Test the length calculation function."""
        test_dict = {"A": 0, "B": 3, "C": 5}
        assert length(test_dict) == 5  # 5 - 0 = 5

        test_dict2 = {"X": 10, "Y": 15, "Z": 12}
        assert length(test_dict2) == 5  # 15 - 10 = 5

        single_char = {"A": 42}
        assert length(single_char) == 0  # 42 - 42 = 0

    def test_get_first_character(self):
        """Test the get_first_character function."""
        test_dict = {"A": 5, "B": 2, "C": 8}
        assert get_first_character(test_dict) == "B"  # B has minimum index 2

        test_dict2 = {"X": 10, "Y": 5, "Z": 15}
        assert get_first_character(test_dict2) == "Y"  # Y has minimum index 5

        single_char = {"A": 42}
        assert get_first_character(single_char) == "A"


class TestPerformance:
    """Test performance characteristics."""

    def test_large_input(self):
        """Test with larger input to ensure reasonable performance."""
        # Create a large string with target letters scattered throughout
        large_text = "X" * 1000 + "A" + "Y" * 1000 + "B" + "Z" * 1000 + "C" + "W" * 1000
        result = find_shortest_substring(large_text, "ABC")
        # Should find the ABC spanning from position 1000 to 3002
        assert len(result) <= 2003  # Should be reasonable length

    def test_worst_case_scenario(self):
        """Test worst case where optimal window is at the very end."""
        # A and B at start, C at very end
        text = "AB" + "X" * 100 + "C"
        result = find_shortest_substring(text, "ABC")
        assert result == text  # Entire string should be the result


if __name__ == "__main__":
    pytest.main([__file__])
