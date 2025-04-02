import random
import time
import os

def matrix_rain(rows=20, cols=50, delay=0.1):
    chars = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz@#$%^&*()"
    
    while True:
        screen = ["".join(random.choice(chars) for _ in range(cols)) for _ in range(rows)]
        os.system("cls" if os.name == "nt" else "clear")  # Clear screen (Windows: cls, Linux/Mac: clear)
        print("\n".join(screen))
        time.sleep(delay)

try:
    matrix_rain()
except KeyboardInterrupt:
    print("\nMatrix rain stopped!")
