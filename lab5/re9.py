import re

def insert_spaces(text):
    modified_text = re.sub(r'(\w)([A-Z])', r'\1 \2', text)
    print(modified_text)
insert_spaces("ShadowFiend")
