import pytest
from unittest.mock import patch
from brain_games.games.progression import (generates_progression,
                                           generate_round_data
                                           )


@pytest.mark.parametrize(
    "start_sequence, step, row_length, expected_progression",
    [
        (5, 3, 7, [5, 8, 11, 14, 17, 20, 23]),
        (10, 4, 6, [10, 14, 18, 22, 26, 30]),
    ])
def test_generates_progression(start_sequence, step, row_length,
                               expected_progression):
    # Patch random.randint to return fixed values
    with patch('random.randint') as mock_randint:
        mock_randint.side_effect = [start_sequence, step, row_length]
        progression = generates_progression()
        assert progression == expected_progression


@pytest.mark.parametrize(
    "start_sequence, step, row_length, random_index, \
    expected_data, missing_number",
    [
        (10, 4, 6, 3, '10 14 18 .. 26 30', 22),
        (1, 2, 5, 2, '1 3 .. 7 9', 5),
    ])
def test_generate_round_data(start_sequence, step, row_length, random_index,
                             expected_data, missing_number):
    # Patch random.randint to return fixed values
    with patch('random.randint') as mock_randint:
        mock_randint.side_effect = [
            start_sequence, step, row_length, random_index]
        data, right_answer = generate_round_data()
        assert data == expected_data
        assert right_answer == str(missing_number)
