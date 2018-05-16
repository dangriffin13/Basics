
import datetime


def return_now():
    return datetime.datetime.now()

def time_since_millenium(time_object):
    delta = time_object - datetime.datetime(2000, 1, 1)
    return delta

def one_day_ago(time_object):
    return time_object - datetime.timedelta(1)


if __name__ == "__main__":
    print("Date formatting methods are available")