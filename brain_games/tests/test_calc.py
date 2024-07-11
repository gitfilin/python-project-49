import pytest
from unittest.mock import patch
from brain_games.games.calc import generate_round_data


@pytest.mark.parametrize("a, b, operator, expected_answer", [
    (3, 5, '+', '8'),
    (10, 4, '-', '6'),
    (7, 6, '*', '42'),
])
def test_generate_round_data(a, b, operator, expected_answer):
    with patch('random.randint', side_effect=[a, b]):
        with patch('random.choice', return_value=operator):
            data, right_answer = generate_round_data()
            assert data == f'{a} {operator} {b}'
            assert right_answer == expected_answer
