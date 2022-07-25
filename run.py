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


def calc_avg_word_len(sentence):
    '''Calculate the average word length of the sentense'''
    
    words = sentence.split(' ')
    word_len = 0
    for word in words:
        word_len += len(word)
    return round((word_len / len(words)), 0)


def calc_cps(elapsed_secs, chars_typed):
    '''Calculate and return the characters per second'''
    
    return round((chars_typed / elapsed_secs), 2)


def calc_wpm(elapsed_secs, avg_word_len, typed_len):
    '''Calculate the words per minute '''
    
    elapsed_minutes = elapsed_secs / 60
    return round((typed_len / elapsed_minutes) / avg_word_len, 2)


def calc_accuracy(correct_typed, total_chars_typed):
    '''Calculate the typing accuracy'''
   
    # Catch ZeroDivisionError before anything has yet been typed
    try:
        return f'{(round((len(correct_typed) / total_chars_typed), 2) * 100)}%'
    except ZeroDivisionError:
        return '---'


def display_content():
    pass


def run(stdscr):
    '''Run the game once initialized by main'''
    sentence = get_random_sentence()
    start_time = time.time()

    typed_str = ''
    total_chars_typed = 0
    correct_typed = []
    avg_word_len = calc_avg_word_len(sentence)

    while True:
        elapsed_secs = max(time.time() - start_time, 1)
        chars_typed = len(typed_str)

        cps = calc_cps(elapsed_secs, chars_typed)
        wpm = calc_wpm(elapsed_secs, avg_word_len, len(typed_str))
        accuracy = calc_accuracy(correct_typed, total_chars_typed)


def main(stdscr):
    '''Main function calls functions to initialize the game'''

    # Define colors to be used 
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)

    # Get the initial screen
    init_screen(stdscr)


wrapper(main)
