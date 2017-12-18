import time as t

class stopwatch():

    def __init__(self, ar="seco minute hour", s=1):
        self.s=s*100
        self.show="stopwatch.disp("
        for i in ar.split():
            if i not in ["time","hundseco","seco","minute","hour"]:
                return "What the hell is %s?" % i
            self.show+="self."+str(i)+","
        self.show = self.show[:-1]
        self.show+=")"

    def refresh(self):
        self.time = (t.time()-self.time_0)*self.s
        self.hundseco=self.pre(1,100)
        self.seco=self.pre(100,60)
        self.minute=self.pre(6000,60)
        self.hour=self.pre(360000,24)

    def disp(*args):
        x=""
        for i in reversed(args):
            x+=str(i)+":"
        return "%s"%x[:-1]

    def pre(self,a,b):
        x = int((self.time/a)%b)
        if x < 10:
            return "0%s"%x
        return x

    def start(self):
        self.time_0 = t.time()

    def get_time(self, raw=0):
        try:
            self.refresh()
            if raw:
                return self.time/100
            return eval(self.show)
        except AttributeError:
            print("You have to start the timer")

    def loop(self):
        #self.start()
        while 1:
            print("\r"+self.get_time(),end="")

def clock(utc=0):
    t = timer()
    while 1:
        t.time_0=0
        print("\r"+str(t.get_time()))

'''import tim
t = tim.stopwatch("seco minute")
t.start()
t.timer()'''