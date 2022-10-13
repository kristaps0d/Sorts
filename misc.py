import time

class Timer():

    def __init__(self):
        self.start = time.time()
        self.time = None

    def StartTimer(self):
        self.start = time.time()
        return self.start

    def StopTimer(self):
        self.time = time.time() - self.start
        return self.time

    def TimeFunction(self, func:any, args:tuple) -> float:
        self.StartTimer()
        func(args)
        return self.StopTimer()

def keyboardExceptionExitHandler(function:any, args:tuple) -> any:
    try:
        return function(args)
    except KeyboardInterrupt:
        return