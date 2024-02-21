import re

pattern = re.compile(r'ab*')

def match_string(text):
    if pattern.fullmatch(text):
        print("Match found")
    else:
        print("Match not found")
match_string("ab")    
match_string("abb")   
match_string("a") 
match_string("ac")   
