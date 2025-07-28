import threading
class Bus:
    def __init__(self):
        self.seats=50
        self.l=threading.Lock()
    def reserve(self,name,s):
        self.l.acquire()
        for i in range(s):
            self.seats=self.seats-1
        print(f'{name} seats are reserved')
        print(f'{self.seats} are available')
        self.release()
class ReserveThread(threading.Thread):
    def __init__(self,name,bus):
        super().__init__()
        self.__bus=bus
        self.__name=name
        self.__s=s
    def run(self):
        self.__bus.reserve(self.__name,self.__s)

bus1=Bus()
t1=ReserveThread("paras",10,bus1)
t2=ReserveThread("ashu",5,bus1)
t3=ReserveThread("adi",10,bus1)
t1.start()
t2.start()
t3.start()

