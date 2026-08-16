import time


time_left=900
while time_left > 895:
    time.sleep(1)
    time_left-=1
    print(f"\r{time_left}", end="")
