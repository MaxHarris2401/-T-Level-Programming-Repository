import datetime
import os
import time
def main():
    while True:
        os.system('cls')
        print(datetime.datetime.today().strftime("%A:%d:%B.%Y"))
        print(datetime.datetime.today().strftime("%H:%M:%S"))
        time.sleep(0.85)
main()