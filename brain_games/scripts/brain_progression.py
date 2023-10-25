#!/usr/bin/env python3
from brain_games.engine import game_engine
from brain_games.games.progression import game_progression, QUESTION


def main():
    game_engine(QUESTION, game_progression)


if __name__ == '__main__':
    main()
