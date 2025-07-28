import threading

def even():
    for n in range(1,21):
        if n%2==0:
            print(f'{n} is Even')

def odd():
    for n in range(1,21):
        if n%2!=0:
            print(f'{n} is odd')
even_thrad=threading.Thread(target=even)
odd_thrad=threading.Thread(target=odd)
even_thrad.start()
odd_thrad.start()
