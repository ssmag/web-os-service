import threading
import time

class ThreadHandler(object):
    thread_list = []
    active_thread = None

    def add_thread_to_list(self, thread):
        if (thread not in self.thread_list):
            self.thread_list.append(thread)

    def __init__(self, interval=1, args=()):
        self.interval = interval
        self.args = args
        t = threading.Thread(target=self.run, args=self.args)
        self.active_thread = t

    def set_function(self, function, arg=None, args=()):
        self.function = function
        if arg:
            self.args = (arg,)
            return
        self.args = args
       
    
    def get_function(self):
        return self.function

    def set_args(self, args):
        self.args = args
    
    def get_args():
        return self.args

    def get_thread_list(self):
        return self.thread_list

    def get_active_thread():
        return self.active_thread

    def run(self, args=()):
        while True:
            if (args):
                self.function(args)
            else:
                self.function()
            time.sleep(self.interval)

    def start(self):
            t = threading.Thread(target=self.run, args=self.args)
            self.add_thread_to_list(t)
            self.active_thread = t
            self.active_thread.start()

