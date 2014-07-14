__author__ = 'Saturn'
import threading
import time

class AbstractSubject:
    def __init__(self, name):
        self.name = name
        self.observers = []
        self.status = "default status"

    def attach(self):
        pass
    def detach(self):
        pass
    def notify(self):
        pass


class Subject(AbstractSubject):

    def __init__(self, name):
        AbstractSubject.__init__(self,name)
        # lock to prevent thread access of observers
        self.lock = threading.Lock()

    def attach(self, observer):
        self.lock.acquire()
        self.observers.append(observer)
        self.lock.release()

    def detach(self, observer):
        self.lock.acquire()
        self.observers.remove(observer)
        self.lock.release()

    def notify(self):
        self.lock.acquire()
        for observer in self.observers:
            observer.update()
        self.lock.release()

    def setStatus(self, s):
        self.status = s
        self.notify()

    def getStatus(self):
        return self.status

class ObserverBase:
    GlobalID = 0

    def __init__(self, subject):
        print "observer base constructor"
        subject.attach(self)
        self.s = subject
        self.id = Observer.GlobalID
        Observer.GlobalID += 1

    def update(self):
        pass

class Observer(ObserverBase):
    def __init__(self, subject):
        ObserverBase.__init__(self, subject)
        print "observer inherent constructor"

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

def deleteObserver(subject, observer, seconds = 4):
    time.sleep(seconds)
    subject.detach(observer)
    print "observer deleted"

if  __name__ == "__main__":
    subject = Subject("FirstSubject")
    a = Observer(subject)
    b = Observer(subject)
    c = Observer(subject)

    thread1 = threading.Thread(target=runSubjectChange, args=(subject,))
    thread2 = threading.Thread(target=runSubjectChangeLong, args=(subject,))
    thread3 = threading.Thread(target=deleteObserver, args=(subject, a, 4))
    thread4 = threading.Thread(target=deleteObserver, args=(subject, b, 5))
    #
    thread1.start()
    thread2.start()
    thread3.start()
    thread4.start()

    # thread1.join()
    # thread2.join()
    # thread3.join()
    # thread4.join()