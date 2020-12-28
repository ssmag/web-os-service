#!/usr/bin/env python3

from pywebostv.connection import WebOSClient as TVClient
import threading as Thread


class ClientHelper:

    def __init__(self):
        self.ip = "10.0.0.117"
        self.store = {}
        self.registered = False
        self.client = TVClient(self.ip)

    def start_connection(self):
        if self.registered:
            return
        print("Connecting to client...")
        self.client.connect()
        self.register_tv()

    def register_tv(self):
        if self.registered:
            return
        for status in self.client.register(self.store):
                if status == TVClient.PROMPTED:
                    print("Please accept the connection on the TV")
                elif status == TVClient.REGISTERED:
                    self.registered = True
                    print("Registration successful")
