import pytest
from unittest.mock import patch
from brain_games.games.gcd import generate_round_data


@pytest.mark.parametrize("a, b, expected_gcd", [
    (48, 18, 6),
    (101, 10, 1),
    (27, 36, 9),
    (20, 25, 5),
    (42, 56, 14),
])
def test_generate_round_data(a, b, expected_gcd):
    with patch('random.randint', side_effect=[a, b]):
        data, right_answer = generate_round_data()
        assert data == f'{a} {b}'
        assert right_answer == str(expected_gcd)
