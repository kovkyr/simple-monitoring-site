from .models import Squad, Host
import time

def check_hosts():
    with open("/tmp/test.txt", "a") as f:
        f.write("test1\n")
    time.sleep(300)
    with open("/tmp/test.txt", "a") as f:
        f.write("test2\n")
