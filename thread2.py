import threading
class evenThread(threading.Thread):
    def run(self):
        for num in range(1,21):
            if num%2==0:
                print(f'{num} is even')

class oddThread(threading.Thread):
    def run(self):
        for num in range(1,21):
            if num%2!=0:
                print(f'{num} is odd')

t1=evenThread()
t2=oddThread()
t1.start()
t2.start()
