#!/usr/bin/env python3
from brain_games.engine import game_engine
from brain_games.games.calc import game_calc, QUESTION


def main():
    game_engine(QUESTION, game_calc)


if __name__ == '__main__':
    main()
