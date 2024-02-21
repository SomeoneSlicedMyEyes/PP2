import re

pattern = re.compile(r'[ ,.]')

def replace_chars(text):
    replaced_text = pattern.sub(':', text)
    print(replaced_text)
replace_chars("hello, glhf. i am good")
