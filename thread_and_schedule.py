import time
import threading


def ten_second_breaks(n):
    if n > 12:
        print("That's going to take a while")
    else:
        print("Initiating run")
        for _ in range(n):
            for _ in range(10): #one second loops allow for keyboard interrupts
                time.sleep(1)
            print('It\'s been ten seconds')
        print("Run complete")

def takeNap():
    print("Start of second thread")
    time.sleep(5)
    print("End of second thread")

def basic_thread():
    print("Start of first thread")
    threadObj = threading.Thread(target=takeNap)
    threadObj.start()
    print("End of first thread")

#pass args to thread
def delayed_sum(*args):
    total = sum([arg for arg in args])
    print("Total has been summed")
    time.sleep(5)
    print('Sum: ', total)


def initiate_sum(*args):
    print("Initiating")
    #Do not pass args directly to function.  This returns the function immediately
    threadObj = threading.Thread(target=delayed_sum, args=args)  
    threadObj.start()
    print("End of initiation")


if __name__ == "__main__":
    print("Play with the timing of functions")