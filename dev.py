import subprocess
import time
import sys

fileName = sys.argv[1]
while True:
    time.sleep(.5)
    print("Restarting script...")
    print("-------------------------------------------")
    subprocess.run(["python3", fileName])
    print("-------------------------------------------")
    print("Finished script.")
    print("===========================================")