import re

def split_at_uppercase(text):
    words = re.findall('[A-Z][^A-Z]*', text)
    print(words)
split_at_uppercase("Arc Warden")
