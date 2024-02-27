import time
import math

def calculator(number, ms):
    time.sleep(ms / 1000) 
    sqrt_result = math.sqrt(number)
    return sqrt_result

number = 25100
ms = 2123
result = calculator(number, ms)
print(f"Square root of {number} after {ms} milliseconds is {result}")
