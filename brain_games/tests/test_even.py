import pytest
from unittest.mock import patch
from brain_games.games.even import generate_round_data


@pytest.mark.parametrize("random_value, expected_answer", [
    (2, 'yes'),
    (3, 'no'),
    (4, 'yes'),
    (5, 'no'),
    (10, 'yes'),
    (11, 'no')
])
def test_generate_round_data(random_value, expected_answer):
    with patch('random.randint', return_value=random_value):
        data, answer_user = generate_round_data()
        assert data == random_value
        assert answer_user == expected_answer
