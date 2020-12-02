#!/usr/bin/env python3

import time
from clienthelper import ClientHelper
from threadhandler import ThreadHandler


def main():
    cHelper = ClientHelper()
    tHandler = ThreadHandler()
    tHandler.set_function(cHelper.start_connection)
    tHandler.start()
    tHandler.set_function(check_registration, cHelper)
    tHandler.start()
    tHandler.set_function(list_threads, tHandler)
    tHandler.start()

def list_threads(tHandler):
    while (True):
        print(tHandler.get_thread_list())
        time.sleep(5)
        
def check_registration(cHelper):
    while (True):
        if (cHelper.registered):
            print("registered")
            time.sleep(1)


if __name__ == "__main__":
    main()
