# coding:utf-8
import pytest
import sys
import os
import datetime
import json

sys.path.append(os.path.join(os.path.dirname(__file__), '..\\..\\src\\'))
from util import util

def readFileStr(filename):
    f = open(os.path.join("test", "util", "data", filename), 'r', encoding='UTF-8')
    data = f.read()
    f.close()
    return json.loads(data)


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


@pytest.mark.freeze_time(datetime.datetime(2022, 11, 21, 10, 10, 10, tzinfo=datetime.timezone.utc))
def test_getDateTimeNow():
    output = util.getDateTimeNow()
    assert "2022-11-21T10:10:10+00:00" == output


@pytest.mark.freeze_time(datetime.datetime(2022, 11, 21, 10, 10, 10, tzinfo=datetime.timezone.utc))
def test_getDateTimeNowFileName():
    output = util.getDateTimeNowFileName()
    assert "20221121-101010" == output


if __name__ == "__main__":
    pass
