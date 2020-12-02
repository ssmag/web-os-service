#!/usr/bin/env python3

import sys
import time
from pywebostv.discovery import *
from pywebostv.connection import *
from pywebostv.controls import *

store = {}
client = WebOSClient("10.0.0.117")
client.connect()
print("Connecting to client..")
for status in client.register(store):
    if status == WebOSClient.PROMPTED:
        print("Please accept connection on the TV")
    elif status == WebOSClient.REGISTERED:
        print("Registration successful!")

system = SystemControl(client)
system.notify("HAI PEPONI")

app = ApplicationControl(client)
apps = app.list_apps()
x =
print(vars(x))
