# Task 3: Run all 15 solutions and test each with the example and an extra case.
from solutions import (
    word_frequency, character_frequency, first_non_repeating_character,
    are_anagrams, first_repeating_character, move_zeros_to_end,
    second_highest_distinct, remove_duplicates_preserve_order,
    find_missing_number, two_sum_first_pair, closest_to_zero,
    common_elements, rotate_right, max_consecutive_pair_sum, all_unique_pairs
)
print(word_frequency("python is easy and python is powerful"))
print(word_frequency("hi hi there"))
print(character_frequency("banana"), character_frequency("hello"))
print(first_non_repeating_character("swiss"))
print(first_non_repeating_character("aabbc"))
print(are_anagrams("listen", "silent"))
print(are_anagrams("hello", "world"))
print(first_repeating_character("programming"))
print(first_repeating_character("abcda"))
print(move_zeros_to_end([0, 3, 0, 1, 2, 0, 4]))
print(second_highest_distinct([10, 20, 40, 30, 40, 20]))
print(second_highest_distinct([5, 5, 5]))
print(remove_duplicates_preserve_order([4, 2, 4, 5, 2, 7, 5]))
print(remove_duplicates_preserve_order(["a", "b", "a"]))
print(find_missing_number([1, 2, 4, 5, 6], 6))
print(find_missing_number([1, 2, 3, 5], 5))
print(two_sum_first_pair([2, 7, 11, 15], 9))
print(two_sum_first_pair([3, 2, 4], 6))
print(closest_to_zero([-8, -3, 2, 5, -2]))
print(closest_to_zero([-4, -1, 1, 3]))
print(common_elements([1, 2, 3, 4, 5], [3, 4, 5, 6, 7]))
print(common_elements([2, 2, 3], [3, 2]))
print(rotate_right([1, 2, 3, 4, 5], 2))
print(rotate_right([1, 2, 3], 4))
print(max_consecutive_pair_sum([4, 7, 2, 9, 5]))
print(max_consecutive_pair_sum([-5, -2, -8]))
print(all_unique_pairs([2, 4, 3, 5, 7, 8, 1], 9))
print(all_unique_pairs([1, 1, 2, 2, 3, 3], 4))
