#This is my script
#I have just edited this in nedit, that awsome!

#remember to log in using Cap"X"

#in Mobaxterm call: python file.py "H" "There are eggs in the garage."
# output: In there are eggs in the garage., h was found 2 times. Overall fraction: 0.069

import sys
import reusable as f # f stands for Function to Rick! 

# fro resuable import case_insensitive_search

char = sys.argv[1]
phrase = sys.argv[2]


    
f.case_insensitive_search(char, phrase)
