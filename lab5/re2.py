import re

pattern = re.compile(r'ab{2,3}')

def match_string(text):
    if pattern.fullmatch(text):
        print("Match found")
    else:
        print("Match not found")
match_string("abb")  
match_string("abbb") 
match_string("ab")   
match_string("abbbb") 
