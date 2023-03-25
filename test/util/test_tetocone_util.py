# coding:utf-8
import pytest
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..\\..\\src\\'))
from util import tetocone_util


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
