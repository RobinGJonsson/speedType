import curses
from curses import wrapper
import time


# Ask for user name
def get_username():
    '''Asks for username and return username if it only contains letters'''
    while True:
        username = input('Choose a username: ')
        # Check if name only contains letters, else ask again
        if username.isalpha():
            return username
        else:
            print('Username can only contain letters and no spaces!')



# Generate a sentence for user to copy

# display the sentence
# split the letters into a list
# And placed into a dictionary with value of none until button is pressed upon 
# which the value will change to true or false

# Check for buttons pressed

# While loop while end isn't reached, each loop waits for a key press 
# For each loop add 1 to i 
# i will represent the relevant key by calling the i index from the 
# characher list 
# So call the key from the dict with i 
# If they match the relevant character save them to a list, the char will 
# display green 
# If backspace, remove the last index from the correct list
# subtract 1 from i  
# When a wrong charachter is pressed it will be saved as wrong and display as red until user fix the error 

# Measure time between each key pressed 
    # Display as chartachers pressed per second and minute 
# Measure time between each word 
    # Display as chartachers pressed per second and minute 

# When all is correct display score
    # Accuracy
    # errors/correct 
    # words/charachters per minute 
    # words/charachters per minute 
    
    # Ask for new game yes/no
        # if no exit()
        # if yes call start game again

# Make GUI 
    # Displays sentence 
    # Display stats
    # Text area 
        # Color charachers based on correct/incorrect
    