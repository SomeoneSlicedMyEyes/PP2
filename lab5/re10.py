import re

def camel_to_snake(text):
    snake_case = re.sub(r'(?<!^)(?=[A-Z])', '_', text).lower()
    return snake_case
print(camel_to_snake("SergeyMalyarov"))

