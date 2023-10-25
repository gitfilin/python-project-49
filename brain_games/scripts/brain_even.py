#!/usr/bin/env python3
from brain_games.engine import game_engine
from brain_games.games.even import game_even, QUESTION


def main():
    game_engine(QUESTION, game_even)


if __name__ == '__main__':
    main()