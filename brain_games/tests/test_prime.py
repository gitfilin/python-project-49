import pytest
from unittest.mock import patch
from brain_games.games.prime import generate_round_data, is_prime


@pytest.mark.parametrize("number, expected", [
    (2, True),
    (3, True),
    (4, False),
    (5, True),
    (10, False),
    (13, True),
    (25, False),
    (29, True),
    (1, False),
    (0, False),
])
def test_is_prime(number, expected):
    assert is_prime(number) == expected


@pytest.mark.parametrize("random_value, expected_answer", [
    (2, 'yes'),
    (3, 'yes'),
    (4, 'no'),
    (5, 'yes'),
    (10, 'no'),
    (13, 'yes'),
])
def test_generate_round_data(random_value, expected_answer):
    with patch('random.randint', return_value=random_value):
        data, right_answer = generate_round_data()
        assert data == random_value
        assert right_answer == expected_answer
