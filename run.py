import curses
from curses import wrapper
import random
import time


def get_username(stdscr):
    '''Asks for username and return username if it only contains letters'''
    stdscr.addstr('Choose a username: ')
    username = ''
    while True:
        key = stdscr.getkey()
        # Check if name only contains letters, else ask again
        if key.isalpha():
            stdscr.addch(key)
            username += key
        elif key in ('KEY_BACKSPACE', '\b', '\x7f'):
            stdscr.clear()
            username = username[:-1]
            stdscr.addstr(username)
        elif key in ('KEY_ENTER', '\n'):
            break
        else:
            stdscr.addstr('\nUsername can only contain letters and no spaces!')
            stdscr.addstr(f'\n{username}')
    stdscr.clear()
    return username


# Generate a sentence for user to copy
def get_random_sentence():
    '''Return a random sentence as a string from sentences.txt'''
    with open('sentences.txt', 'r', encoding='utf-8') as file:
        sentences = file.readlines()
        return random.choice(sentences)


def init_screen():
    pass


def calc_cps():
    pass


def calc_wpm():
    pass


def calc_accuracy():
    pass


def display_content():
    pass


def run():
    pass


def main():
    pass