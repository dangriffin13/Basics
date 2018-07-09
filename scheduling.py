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





if __name__ == "__main__":
    print("Play with the timing of functions")