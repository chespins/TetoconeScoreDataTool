# coding:utf-8
import json
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..\\..\\src\\'))
from util import tetocone_util


def readFileStr(filename):
    f = open(os.path.join("test", "util", "data", filename), 'r', encoding='UTF-8')
    data = f.read()
    f.close()
    return json.loads(data)


def test_getLevelIdByName_0():
    assert tetocone_util.getLevelIdByName("") == 0


def test_getLevelIdByName_1():
    assert tetocone_util.getLevelIdByName("STANDARD") == 1


def test_getLevelIdByName_2():
    assert tetocone_util.getLevelIdByName("EXPERT") == 2


def test_getLevelIdByName_3():
    assert tetocone_util.getLevelIdByName("ULTIMATE") == 3


def test_getLevelIdByName_4():
    assert tetocone_util.getLevelIdByName("MANIAC") == 4


def test_getLevelIdByName_5():
    assert tetocone_util.getLevelIdByName("CONNECT") == 5


def test_getGenreIdByName_0():
    assert tetocone_util.getGenreIdByName("アニメ・ポップス") == "G000"


def test_getGenreIdByName_1():
    assert tetocone_util.getGenreIdByName("バーチャル") == "G001"


def test_getGenreIdByName_2():
    assert tetocone_util.getGenreIdByName("東方アレンジ") == "G002"


def test_getGenreIdByName_3():
    assert tetocone_util.getGenreIdByName("ゲーム") == "G003"


def test_getGenreIdByName_4():
    assert tetocone_util.getGenreIdByName("オリジナル") == "G004"


def test_getGenreIdByName_5():
    assert tetocone_util.getGenreIdByName("バラエティー") == "G005"


def test_getGenreIdByName_Empty():
    assert tetocone_util.getGenreIdByName("") == ""


def test_makeRankDict_empty():
    assert tetocone_util.makeRankDict([]) == {}


def test_makeRankDict_one():
    params = readFileStr("makeRankDict_one.json")
    assert tetocone_util.makeRankDict(params["input"]) == params["output"]


def test_makeRankDict_three():
    params = readFileStr("makeRankDict_three.json")
    assert tetocone_util.makeRankDict(params["input"]) == params["output"]


def test_makeRankDict_three_false():
    params = readFileStr("makeRankDict_three.json")
    assert tetocone_util.makeRankDict(params["input"], False) == params["output"]


def test_makeRankDict_three_true():
    params = readFileStr("makeRankDict_three.json")
    assert tetocone_util.makeRankDict(params["input"], True) == params["output_true"]
