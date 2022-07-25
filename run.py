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


def init_screen(stdscr):
    '''Displays the start screen before the actual game starts'''
    stdscr.clear()
    username = get_username(stdscr)

    stdscr.addstr(f'Hello {username}')
    stdscr.addstr("\nThe rule is to copy the target sentence that will be "
                  "displayed upon game START without errors."
                  "\nOnce the you've reached the end with no errors hit "
                  "ENTER.\nTo start press any key...")

    # Wait until user presses any key
    stdscr.getkey()
    stdscr.clear()


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