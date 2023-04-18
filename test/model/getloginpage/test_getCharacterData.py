# coding:utf-8
import pytest
import sys
import os
import datetime
from common_def import readFileStr

sys.path.append(os.path.join(os.path.dirname(__file__), '..\\..\\..\\src\\'))
from model import getloginpage


@pytest.mark.freeze_time(datetime.datetime(2022, 11, 21, 10, 10, 10, tzinfo=datetime.timezone.utc))
def test_character_none(mocker):
    param_data = readFileStr("character_none.json")
    mock_return = param_data["mock_return"]
    character_mock = mocker.patch("model.mypagedata.getCharacterData", return_value=mock_return["getCharacterData"])
    character_ranking_mock = mocker.patch("model.mypagedata.getCharacterRanking", return_value=mock_return["getCharacterRanking"])
    db_character_mock = mocker.patch("model.datainserts.insertCharacter")
    db_introduction_mock = mocker.patch("db.character.selectCharacter", return_value=mock_return["selectCharacter"])
    sleep_mock = mocker.patch("model.getloginpage.sleep")
    input_session = param_data["input"]["sesson"]
    input_characters = param_data["input"]["characters"]

    getloginpage.getCharacterData(input_session, input_characters)

    db_introduction_mock.assert_not_called()
    character_mock.assert_not_called()
    character_ranking_mock.assert_not_called()
    db_character_mock.assert_called_once()
    db_character_mock.assert_called_with(param_data["mock_params"]["insertCharacter"])
    sleep_mock.assert_not_called()


@pytest.mark.freeze_time(datetime.datetime(2022, 11, 21, 10, 10, 10, tzinfo=datetime.timezone.utc))
def test_character_one(mocker):
    param_data = readFileStr("character_one.json")
    mock_return = param_data["mock_return"]
    character_mock = mocker.patch("model.mypagedata.getCharacterData", return_value=mock_return["getCharacterData"])
    character_ranking_mock = mocker.patch("model.mypagedata.getCharacterRanking", return_value=mock_return["getCharacterRanking"])
    db_character_mock = mocker.patch("model.datainserts.insertCharacter")
    db_introduction_mock = mocker.patch("db.character.selectCharacter", return_value=mock_return["selectCharacter"])
    sleep_mock = mocker.patch("model.getloginpage.sleep")
    input_session = param_data["input"]["sesson"]
    input_characters = param_data["input"]["characters"]

    getloginpage.getCharacterData(input_session, input_characters)

    db_introduction_mock.assert_called_once()
    db_introduction_mock.assert_called_with(characterId="CHR_T_01")
    character_mock.assert_called_once()
    character_mock.assert_called_with(input_session, "CHR_T_01")
    character_ranking_mock.assert_called_once()
    character_ranking_mock.assert_called_with(input_session, "CHR_T_01")
    db_character_mock.assert_called_once()
    db_character_mock.assert_called_with(param_data["mock_params"]["insertCharacter"])
    assert sleep_mock.call_count == 2
    sleep_mock.assert_has_calls([
            mocker.call(1),
            mocker.call(1),
    ])

@pytest.mark.freeze_time(datetime.datetime(2022, 11, 21, 10, 10, 10, tzinfo=datetime.timezone.utc))
def test_character_three(mocker):
    param_data = readFileStr("character_three.json")
    mock_return = param_data["mock_return"]
    character_mock = mocker.patch("model.mypagedata.getCharacterData", side_effect=mock_return["getCharacterData"])
    character_ranking_mock = mocker.patch("model.mypagedata.getCharacterRanking", side_effect=mock_return["getCharacterRanking"])
    db_character_mock = mocker.patch("model.datainserts.insertCharacter")
    db_introduction_mock = mocker.patch("db.character.selectCharacter", side_effect=mock_return["selectCharacter"])
    sleep_mock = mocker.patch("model.getloginpage.sleep")
    input_session = param_data["input"]["sesson"]
    input_characters = param_data["input"]["characters"]

    getloginpage.getCharacterData(input_session, input_characters)

    assert db_introduction_mock.call_count == 3
    db_introduction_mock.assert_has_calls([
            mocker.call(characterId="CHR_T_01"),
            mocker.call(characterId="CHR_T_02"),
            mocker.call(characterId="CHR_T_03"),
    ])
    assert character_mock.call_count == 2
    character_mock.assert_has_calls([
            mocker.call(input_session, "CHR_T_01"),
            mocker.call(input_session, "CHR_T_03"),
    ])
    assert character_ranking_mock.call_count == 2
    character_ranking_mock.assert_has_calls([
            mocker.call(input_session, "CHR_T_01"),
            mocker.call(input_session, "CHR_T_02"),
    ])
    db_character_mock.assert_called_once()
    db_character_mock.assert_called_with(param_data["mock_params"]["insertCharacter"])
    assert sleep_mock.call_count == 4
    sleep_mock.assert_has_calls([
            mocker.call(1),
            mocker.call(1),
            mocker.call(1),
            mocker.call(1),
    ])
