#!/usr/bin/env python3
from brain_games.engine import game_engine
from brain_games.games.prime import prime, QUESTION


def main():
    game_engine(QUESTION, prime)


if __name__ == '__main__':
    main()
