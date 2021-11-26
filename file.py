#This is my script
#I have just edited this in nedit, that awsome!

#remember to log in using Cap"X"
import sys

char = sys.argv[1]
phrase = sys.argv[2]

def case_insensitive_search(char, phrase):
    """ Searches for char in phrase, regardless of case. returns true if found """
    char = char.lower()
    phrase = phrase.lower()
    count = phrase.count(char)
    fraction = count / len(phrase)
    print (f"In {phrase}, {char} was found {count} times. Overall fraction: {fraction:0.3f}") # variable name: format three decimal placed.
    return (char in phrase)
    
case_insensitive_search(char, phrase)
