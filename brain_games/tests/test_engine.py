from unittest.mock import patch
from io import StringIO
from brain_games.engine import playing_game


class MockGame:
    DESCRIPTION = 'Mock game description'

    @staticmethod
    def generate_round_data():
        return 'Question: What is 2 + 2?', '4'  # Пример выдачи данных игры


@patch('brain_games.engine.prompt')
def test_playing_game_correct_answer(mock_prompt):
    answers = ['John', '4', '4', '4']
    mock_prompt.string.side_effect = answers

    with patch('sys.stdout', new_callable=StringIO) as fake_out:
        playing_game(MockGame)
        output = fake_out.getvalue().strip()

    assert 'Welcome to the Brain Games!' in output
    assert 'Hello, John!' in output
    assert 'Question: What is 2 + 2?' in output
    assert 'Correct!' in output
    assert 'Let\'s try again' not in output
    assert 'Congratulations' in output


@patch('brain_games.engine.prompt')
def test_playing_game_wrong_answer(mock_prompt):
    answers = ['John', '5', '4', '4']
    mock_prompt.string.side_effect = answers

    with patch('sys.stdout', new_callable=StringIO) as fake_out:
        playing_game(MockGame)
        output = fake_out.getvalue().strip()

    assert 'Welcome to the Brain Games!' in output
    assert 'Hello, John!' in output
    assert 'Question: What is 2 + 2?' in output
    assert 'Correct!' not in output
    assert "'5' is wrong answer ;(." in output
    assert 'Correct answer was' in output
    assert 'Let\'s try again' in output
    assert 'Congratulations' not in output
