#!/usr/bin/env python3
from brain_games.engine import game_engine
from brain_games.games.gcd import game_gcd, QUESTION


def main():
    game_engine(QUESTION, game_gcd)


if __name__ == '__main__':
    main()
