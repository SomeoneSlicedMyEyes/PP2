import re

pattern = re.compile(r'[A-Z][a-z]+')

def find_sequences(text):
    matches = pattern.findall(text)
    print(matches)
find_sequences("Hello World HowAreYou") 
