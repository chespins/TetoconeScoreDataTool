# coding:utf-8
import os
import json


def readFileStr(filename):
    f = open(os.path.join("test", "model", "makeCsvFile", "data", filename), 'r', encoding='UTF-8')
    data = f.read()
    f.close()
    return json.loads(data)