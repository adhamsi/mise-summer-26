# Form 1: import the module, access names with a prefix
import math

print(math.pi)        # 3.141592653589793
print(math.sqrt(16))  # 4.0

# Form 2: import specific names directly (no prefix needed)
from math import sqrt, pi

print(pi)        # 3.141592653589793
print(sqrt(16))  # 4.0
