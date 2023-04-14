# coding:utf-8
import pytest
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..\\..\\src\\'))
from util import util


def test_changeTimeZone1():
    input = "2023-01-07T08:12:27+00:00"
    success = "2023年1月7日 17:12:27"
    assert success == util.changeTimeZone(input)


def test_changeTimeZone2():
    input = "2023-01-07T21:09:01+00:00"
    success = "2023年1月8日 06:09:01"
    assert success == util.changeTimeZone(input)


def test_changeTimeZone3():
    input = "2023-01-0721:09:01+00:00"
    
    with pytest.raises(ValueError) as e:
        util.changeTimeZone(input)


def test_changeTimeZone4():
    input = "2023-02-07T08:12:27.000Z"
    success = "2023年2月7日 17:12:27"
    assert success == util.changeTimeZone(input)


def test_diffDate1():
    input1 = "2023-01-07T21:09:01+00:00"
    input2 = "2023-01-07T21:09:02+00:00"
    assert util.diffDate(input1, input2)


def test_diffDate2():
    input1 = "2023-01-09T21:09:00+00:00"
    input2 = "2023-01-09T21:09:00+00:00"
    assert util.diffDate(input1, input2)


def test_diffDate3():
    input1 = "2023-01-09T21:09:01+00:00"
    input2 = "2023-01-09T21:09:00+00:00"
    assert not util.diffDate(input1, input2)


def test_diffDate4():
    input1 = "2023-01-09T21:09:01+00:00"
    input2 = "2023-01-0921:09:00+00:00"

    with pytest.raises(ValueError) as e:
        util.diffDate(input1, input2)


if __name__ == "__main__":
    pass
