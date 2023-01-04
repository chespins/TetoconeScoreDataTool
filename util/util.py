# -*- coding: utf-8 -*-
import os
import sys
import datetime
import re

timezoneReg = re.compile(r'((\+|\-)\d{2}):(\d{2})')


def findDataFile(filename):
    if hasattr(sys, "_MEIPASS"):
        return os.path.join(sys._MEIPASS, filename)
    return os.path.join(filename)


def readFileStr(filename):
    f = open(findDataFile(filename), 'r', encoding='UTF-8')
    data = f.read()
    f.close()
    return data


def changeTimeZone(strTime):
    dt = datetime.datetime.fromisoformat(strTime)
    dtJst = dt.astimezone(datetime.timezone(datetime.timedelta(hours=+9)))
    JstDate = str(dtJst.year) + "年" + str(dtJst.month) + "月" + str(dtJst.day) + "日"
    
    JstTime = datetime.datetime.strftime(dtJst, '%H:%M:%S')
    return JstDate + " " + JstTime


def diffDate(strTime1, strTime2):
    datetime1 =  datetime.datetime.fromisoformat(strTime1)
    datetime2 =  datetime.datetime.fromisoformat(strTime2)
    return datetime1 <= datetime2


def getDateTimeNow():
    date = datetime.datetime.now()
    date_iso = date.astimezone(datetime.timezone(datetime.timedelta(hours=+0)))
    utcTime = datetime.datetime.strftime(date_iso, '%Y-%m-%d{0}%H:%M:%S+00:00')
    return utcTime.format("T",)

def minDateTime():
    return "2000-01-01T00:00:00+00:00"


if __name__ == '__main__':
    pass
