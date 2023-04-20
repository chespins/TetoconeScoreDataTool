# coding:utf-8
import sys
import os
from common_def import readFileStr

sys.path.append(os.path.join(os.path.dirname(__file__), '..\\..\\..\\src\\'))
from model import getloginpage


def test_getDegreesData_none(mocker):
    param_data = readFileStr("degrees_none.json")
    sleep_mock = mocker.patch("model.getloginpage.sleep")
    degrees_mock = mocker.patch("model.mypagedata.getDegreesData", side_effect=param_data["getDegreesData"])
    db_degrees_mock = mocker.patch("model.datainserts.insertDegrees")
    param_session = param_data["sesson"]

    getloginpage.getDegreesData(param_session)

    assert sleep_mock.call_count == 6
    sleep_mock.assert_has_calls([
            mocker.call(1),
            mocker.call(1),
            mocker.call(1),
            mocker.call(1),
            mocker.call(1),
            mocker.call(1),
        ])
    assert degrees_mock.call_count == 6
    degrees_mock.assert_has_calls([
            mocker.call(param_session, "Stage"),
            mocker.call(param_session, "Partner"),
            mocker.call(param_session, "Accessory"),
            mocker.call(param_session, "System"),
            mocker.call(param_session, "MultiMode"),
            mocker.call(param_session, "Event"),
        ])
    db_degrees_mock.assert_called_once()
    db_degrees_mock.assert_called_with(param_data["db_degrees_param"])


def test_getDegreesData(mocker):
    param_data = readFileStr("degrees_success.json")
    sleep_mock = mocker.patch("model.getloginpage.sleep")
    degrees_mock = mocker.patch("model.mypagedata.getDegreesData", side_effect=param_data["getDegreesData"])
    db_degrees_mock = mocker.patch("model.datainserts.insertDegrees")
    param_session = param_data["sesson"]

    getloginpage.getDegreesData(param_session)

    assert sleep_mock.call_count == 6
    sleep_mock.assert_has_calls([
            mocker.call(1),
            mocker.call(1),
            mocker.call(1),
            mocker.call(1),
            mocker.call(1),
            mocker.call(1),
        ])
    assert degrees_mock.call_count == 6
    degrees_mock.assert_has_calls([
            mocker.call(param_session, "Stage"),
            mocker.call(param_session, "Partner"),
            mocker.call(param_session, "Accessory"),
            mocker.call(param_session, "System"),
            mocker.call(param_session, "MultiMode"),
            mocker.call(param_session, "Event"),
        ])
    db_degrees_mock.assert_called_once()
    db_degrees_mock.assert_called_with(param_data["db_degrees_param"])
