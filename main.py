#!/usr/bin/env python3

import time
from pywebostv.discovery import *
from pywebostv.connection import *
from pywebostv.controls import *
from flask import Flask, request
from string import Template

app = Flask(__name__)

def main():
    store = {}
    client = WebOSClient("10.0.0.117")
    client.connect()
    print("Connecting to client..")
    try:
        for status in client.register(store):
            if status == WebOSClient.PROMPTED:
                print("Please accept connection on the TV")
            elif status == WebOSClient.REGISTERED:
                print("Registration successful!")
                system = SystemControl(client)
                system.notify("HAI PEPONI")

                #TODO: Move inp and client into class 
                inp = InputControl(client)
                print(inp)
                print("input controller started")
                app.run(debug=True)
    except Exception:
        print("TIMEOUT SYSTEM")

app.route('/')
def index():
    return 'index'

@app.route("/webos", methods=['POST'])
def keystroke():
    data = request.form
    print(data)
    uinput = data["uinput"]
    print(uinput)
    t = Template('{ "uinput" : "${keystroke}" }').substitute(keystroke=uinput)
    inp.type(uinput)
    inp.enter()
    print(str(t))
    return str(t)

if __name__ == '__main__':
    main()
