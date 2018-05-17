
import datetime as dt


def get_now():
    return dt.datetime.now()

def time_since_millenium(time_object):
    delta = time_object - dt.datetime(2000, 1, 1)
    return delta

def one_day_ago(time_object):
    return time_object - dt.timedelta(1)

def mdy_backslash(time_object):
    try:
        #check for time_object

    return time_object.strftime("%m/%d/%Y")

def dmy_backslash(time_object):
    try:
        #check for time_object
    return time_object.strftime("%d/%m/%Y")

def mdyhs_backslash(time_object):
    try:
        #check for time_object
    return time_object.strftime("%m/%d/%Y %H:%M")

def dmyhs_backslash(time_object):
    try:
        #check for time_object
    return time_object.strftime("%d/%m/%Y %H:%M")

def mdy_dash(time_object):
    try:
        #check for time_object
    return time_object.strftime("%m-%d-%Y")


def dmy_dash(time_object):
    try:
        #check for time_object

def date_from_mdy_backslash(string):


def date_from_dmy_backslash(string):


def date_from_mdyhs_backslash(string):




if __name__ == "__main__":
    print("Date formatting methods are available")