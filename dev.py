import subprocess
import time
while True:
    time.sleep(.5)
    print("Restarting script...")
    print("-------------------------------------------")
    subprocess.run(["python3", "contoursCounter.py"])
    print("-------------------------------------------")
    print("Finished script.")
    print("===========================================")

