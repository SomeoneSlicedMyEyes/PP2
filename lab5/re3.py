import re

pattern = re.compile(r'[a-z]+(?:_[a-z]+)*')

def find_sequences(text):
    matches = pattern.findall(text)
    print(matches)
find_sequences("hello_world how_are_you")
