import re

pattern = re.compile(r'a.*b$')

def match_string(text):
    if pattern.fullmatch(text):
        print("Match found")
    else:
        print("Match not found")
match_string("acb")    
match_string("azb")   
match_string("a123b")  
match_string("ac")     
