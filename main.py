#!/usr/bin/env python3

import time
from clienthelper import ClientHelper
from threadhandler import ThreadHandler


def main():
    cHelper = ClientHelper()
    tHandler = ThreadHandler()
    tHandler.set_function(cHelper.start_connection)
    tHandler.start()
    tHandler2 = ThreadHandler()
    tHandler2.set_function(check_registration)
    tHandler2.start()

def check_registration(cHelper):
    while (True):
        if (cHelper.registered):
            print("registered")
            time.sleep(1)


if __name__ == "__main__":
    main()
