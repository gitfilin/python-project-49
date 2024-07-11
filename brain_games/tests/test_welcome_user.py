from unittest.mock import patch
from io import StringIO
from brain_games.cli import welcome_user


@patch('brain_games.cli.prompt')
def test_welcome_user(mock_prompt):
    # Set up mock for prompt.string
    mock_prompt.string.return_value = 'John'

    # Capture printed output
    with patch('sys.stdout', new_callable=StringIO) as fake_out:
        welcome_user()
        output = fake_out.getvalue().strip()

    # Check if the output matches expected
    assert 'Welcome to the Brain Games!' in output
    assert 'Hello, John!' in output
