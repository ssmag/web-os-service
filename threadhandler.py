import threading
import time

class ThreadHandler(object):
    def __init__(self, interval=1):
        self.interval = interval
        self.thread = threading.Thread(target=self.run, args=())

    def set_function(self, function):
        self.thread.target = function
        self.function = function
    
    def get_function(self):
        return self.function

    def run(self):
        while True:
            self.function()
            time.sleep(self.interval)

    def start(self):
        self.thread.start()


