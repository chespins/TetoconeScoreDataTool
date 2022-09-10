# -*- coding: utf-8 -*-
import os
import sys
import datetime
import re

timezoneReg = re.compile(r'((\+|\-)\d{2}):(\d{2})')


def find_data_file(filename):
    if hasattr(sys, "_MEIPASS"):
        return os.path.join(sys._MEIPASS, filename)
    return os.path.join(filename)


def readFileStr(filename):
    f = open(find_data_file(filename), 'r', encoding='UTF-8')
    data = f.read()
    f.close()
    return data


def changeTimeZone(strTime):
    dt = datetime.datetime.fromisoformat(strTime)
    dt_jst = dt.astimezone(datetime.timezone(datetime.timedelta(hours=+9)))
    JstTime = datetime.datetime.strftime(dt_jst, '%Y{0}%m{1}%d{2} %H:%M:%S')

    return JstTime.format("年", "月", "日", )


if __name__ == '__main__':
    pass
