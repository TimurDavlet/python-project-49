#!/usr/bin/env python3
from brain_games import cli


def hello():
    print('Welcome to the Brain Games!')


def main():
    hello()
    cli.welcome_user()


if __name__ == '__main__':
    main()
