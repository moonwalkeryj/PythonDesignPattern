__author__ = 'Saturn'
import threading
import time

class Subject:

    def __init__(self):
        self.observers = []
        self.status = "default status"

    def attach(self, observer):
        self.observers.append(observer)

    def detach(self, observer):
        self.observers.remove(observer)

    def notify(self):
        for index in range(len(self.observers)):
            self.observers[index].update()

    def setStatus(self, s):
        self.status = s
        self.notify()

    def getStatus(self):
        return self.status


class Observer:

    GlobalID = 0

    def __init__(self, subject):
        subject.attach(self)
        self.s = subject
        self.id = Observer.GlobalID
        Observer.GlobalID += 1

    def update(self):
        print "observer ", self.id, " updated; Subject status: ", self.s.getStatus()

def runSubjectChange(subject):
    for i in range(10):
        subject.setStatus("status changed: " + str(i))
        time.sleep(2)

def runSubjectChangeLong(subject):
    for i in range(10):
        subject.setStatus("status changed: " + str(i+20))
        time.sleep(3)

if  __name__ == "__main__":
    subject = Subject()
    a = Observer(subject)
    b = Observer(subject)
    c = Observer(subject)

    thread1 = threading.Thread(target=runSubjectChange, args=(subject,))
    thread2 = threading.Thread(target=runSubjectChange, args=(subject,))
    thread3 = threading.Thread(target=runSubjectChange, args=(subject,))
    thread4 = threading.Thread(target=runSubjectChangeLong, args=(subject,))

    thread1.start()
    thread2.start()
    thread3.start()
    thread4.start()

    thread1.join()
    thread2.join()
    thread3.join()
    thread4.join()