# coding:utf-8
import sys
import os
import json


sys.path.append(os.path.join(os.path.dirname(__file__), '..\\..\\..\\src\\'))
from model.outputCsvModel import OutputCsvModel

def readFileStr(filename):
    f = open(os.path.join("test", "model", "outputCsvModel", "data", filename), 'r', encoding='UTF-8')
    data = f.read()
    f.close()
    return json.loads(data)


common_json = readFileStr("common_testdata.json")
highScore_return = common_json["highScore_return"]
highScore_success = common_json["highScore_success"]
rank_db_return = common_json["rank_db_return"]
rank_dict_return = common_json["rank_dict_return"]
testObj = OutputCsvModel()


def test_success_false(mocker):
    csv_return = "結果文字列1"
    file_name = "fileName1"
    dbhs_mock = mocker.patch("db.highscore.selectHighScore", return_value=highScore_return)
    rnhs_mock = mocker.patch("db.rankhistory.selectAllRankData", return_value=rank_db_return)
    turh_mock = mocker.patch("util.tetocone_util.makeRankDict", return_value=rank_dict_return)
    csv_mock = mocker.patch("model.makeCsvFile.makeScoreCsvFile", return_value=csv_return)
    result = testObj.outputCsvFile(file_name, False, True)
    assert result == csv_return
    dbhs_mock.assert_called_once()
    dbhs_mock.assert_called_with("")
    rnhs_mock.assert_not_called()
    turh_mock.assert_not_called()
    csv_mock.assert_called_once()
    csv_mock.assert_called_with(highScore_success, file_name, False, {}, True)


def test_success_true(mocker):
    csv_return = "結果文字列2"
    file_name = "fileName2"
    dbhs_mock = mocker.patch("db.highscore.selectHighScore", return_value=highScore_return)
    rnhs_mock = mocker.patch("db.rankhistory.selectAllRankData", return_value=rank_db_return)
    turh_mock = mocker.patch("util.tetocone_util.makeRankDict", return_value=rank_dict_return)
    csv_mock = mocker.patch("model.makeCsvFile.makeScoreCsvFile", return_value=csv_return)
    result = testObj.outputCsvFile(file_name, True, False)
    assert result == csv_return
    dbhs_mock.assert_called_once()
    dbhs_mock.assert_called_with("")
    rnhs_mock.assert_called_once()
    rnhs_mock.assert_called_with()
    turh_mock.assert_called_once()
    turh_mock.assert_called_with(rank_db_return, False)
    csv_mock.assert_called_once()
    csv_mock.assert_called_with(highScore_success, file_name, True, rank_dict_return, False)


def test_marge_diff1(mocker):
    testData = readFileStr("marge_diff1.json")
    highScore_return_diff = testData["highScore_return"]
    highScore_success_diff = testData["highScore_success"]
    csv_return = "結果文字列"
    file_name = "fileName"
    dbhs_mock = mocker.patch("db.highscore.selectHighScore", return_value=highScore_return_diff)
    rnhs_mock = mocker.patch("db.rankhistory.selectAllRankData", return_value=rank_db_return)
    turh_mock = mocker.patch("util.tetocone_util.makeRankDict", return_value=rank_dict_return)
    csv_mock = mocker.patch("model.makeCsvFile.makeScoreCsvFile", return_value=csv_return)
    result = testObj.outputCsvFile(file_name, True, True)
    assert result == csv_return
    dbhs_mock.assert_called_once()
    dbhs_mock.assert_called_with("")
    rnhs_mock.assert_called_once()
    rnhs_mock.assert_called_with()
    turh_mock.assert_called_once()
    turh_mock.assert_called_with(rank_db_return, True)
    csv_mock.assert_called_once()
    csv_mock.assert_called_with(highScore_success_diff, file_name, True, rank_dict_return, True)


def test_marge_diff2(mocker):
    testData = readFileStr("marge_diff2.json")
    highScore_return_diff = testData["highScore_return"]
    highScore_success_diff = testData["highScore_success"]
    csv_return = "結果文字列"
    file_name = "fileName"
    dbhs_mock = mocker.patch("db.highscore.selectHighScore", return_value=highScore_return_diff)
    rnhs_mock = mocker.patch("db.rankhistory.selectAllRankData", return_value=rank_db_return)
    turh_mock = mocker.patch("util.tetocone_util.makeRankDict", return_value=rank_dict_return)
    csv_mock = mocker.patch("model.makeCsvFile.makeScoreCsvFile", return_value=csv_return)
    result = testObj.outputCsvFile(file_name, True, True)
    assert result == csv_return
    dbhs_mock.assert_called_once()
    dbhs_mock.assert_called_with("")
    rnhs_mock.assert_called_once()
    rnhs_mock.assert_called_with()
    turh_mock.assert_called_once()
    turh_mock.assert_called_with(rank_db_return, True)
    csv_mock.assert_called_once()
    csv_mock.assert_called_with(highScore_success_diff, file_name, True, rank_dict_return, True)


def test_highScore_empty(mocker):
    csv_return = "結果文字列3"
    file_name = "fileName2"
    dbhs_mock = mocker.patch("db.highscore.selectHighScore", return_value=[])
    rnhs_mock = mocker.patch("db.rankhistory.selectAllRankData", return_value=rank_db_return)
    turh_mock = mocker.patch("util.tetocone_util.makeRankDict", return_value=rank_dict_return)
    csv_mock = mocker.patch("model.makeCsvFile.makeScoreCsvFile", return_value=csv_return)
    result = testObj.outputCsvFile(file_name, True, False)
    assert result == "ハイスコアデータが存在しません。マイページ取得からハイスコアデータを取得してからもう一度お試しください。"
    dbhs_mock.assert_called_once()
    dbhs_mock.assert_called_with("")
    rnhs_mock.assert_not_called()
    turh_mock.assert_not_called()
    csv_mock.assert_not_called()


def test_highScore_Allempty(mocker):
    csv_return = "結果文字列3"
    file_name = "fileName2"
    highScore_return_empty = readFileStr("highScore_empty.json")
    dbhs_mock = mocker.patch("db.highscore.selectHighScore", return_value=highScore_return_empty)
    rnhs_mock = mocker.patch("db.rankhistory.selectAllRankData", return_value=rank_db_return)
    turh_mock = mocker.patch("util.tetocone_util.makeRankDict", return_value=rank_dict_return)
    csv_mock = mocker.patch("model.makeCsvFile.makeScoreCsvFile", return_value=csv_return)
    result = testObj.outputCsvFile(file_name, True, False)
    assert result == "ハイスコアデータが存在しません。マイページ取得からハイスコアデータを取得してからもう一度お試しください。"
    dbhs_mock.assert_called_once()
    dbhs_mock.assert_called_with("")
    rnhs_mock.assert_not_called()
    turh_mock.assert_not_called()
    csv_mock.assert_not_called()



