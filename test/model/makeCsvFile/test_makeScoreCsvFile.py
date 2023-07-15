# coding:utf-8
import sys
import os
import filecmp

from common_def_csv import readFileStr
sys.path.append(os.path.join(os.path.dirname(__file__), '..\\..\\..\\src\\'))
from model import makeCsvFile


def test_empty():
    highScoreList = []
    test_file_name = os.path.join(os.getcwd(), "scoreData_Test.csv")
    message = makeCsvFile.makeScoreCsvFile(highScoreList, test_file_name, False)
    assert message == "ハイスコアデータの作成に成功しました。"
    assert filecmp.cmp(test_file_name, "test/model/makeCsvFile/result/makeScoreCsvFile_empty.csv")


def test_empty_false():
    highScoreList = []
    test_file_name = os.path.join(os.getcwd(), "scoreData_Test.csv")
    message = makeCsvFile.makeScoreCsvFile(highScoreList, test_file_name, False)
    assert message == "ハイスコアデータの作成に成功しました。"
    assert filecmp.cmp(test_file_name, "test/model/makeCsvFile/result/makeScoreCsvFile_empty.csv")


def test_one_data_false():
    input_params = readFileStr("makeScoreCsvFile_one.json")
    test_file_name = os.path.join(os.getcwd(), "scoreData_Test.csv")
    message = makeCsvFile.makeScoreCsvFile(input_params["highScoreList"], test_file_name, False)
    assert message == "ハイスコアデータの作成に成功しました。"
    assert filecmp.cmp(test_file_name, "test/model/makeCsvFile/result/makeScoreCsvFile_one.csv")


def test_three_data_false():
    input_params = readFileStr("makeScoreCsvFile_three.json")
    test_file_name = os.path.join(os.getcwd(), "scoreData_Test.csv")
    message = makeCsvFile.makeScoreCsvFile(input_params["highScoreList"], test_file_name, False)
    assert message == "ハイスコアデータの作成に成功しました。"
    assert filecmp.cmp(test_file_name, "test/model/makeCsvFile/result/makeScoreCsvFile_three.csv")


def test_empty_true():
    highScoreList = []
    test_file_name = os.path.join(os.getcwd(), "scoreData_Test.csv")
    message = makeCsvFile.makeScoreCsvFile(highScoreList, test_file_name, True)
    assert message == "ハイスコアデータの作成に成功しました。"
    assert filecmp.cmp(test_file_name, "test/model/makeCsvFile/result/makeScoreCsvFile_empty_rank.csv")


def test_one_data_rank():
    input_params = readFileStr("makeScoreCsvFile_one_rank.json")
    test_file_name = os.path.join(os.getcwd(), "scoreData_Test.csv")
    message = makeCsvFile.makeScoreCsvFile(input_params["highScoreList"], test_file_name, True, input_params["rank"], False)
    assert message == "ハイスコアデータの作成に成功しました。"
    assert filecmp.cmp(test_file_name, "test/model/makeCsvFile/result/makeScoreCsvFile_one_rank.csv")


def test_three_data_rank():
    input_params = readFileStr("makeScoreCsvFile_three_rank.json")
    test_file_name = os.path.join(os.getcwd(), "scoreData_Test.csv")
    message = makeCsvFile.makeScoreCsvFile(input_params["highScoreList"], test_file_name, True, input_params["rank"], False)
    assert message == "ハイスコアデータの作成に成功しました。"
    assert filecmp.cmp(test_file_name, "test/model/makeCsvFile/result/makeScoreCsvFile_three_rank.csv")


def test_one_data_marge():
    input_params = readFileStr("makeScoreCsvFile_one_rank.json")
    test_file_name = os.path.join(os.getcwd(), "scoreData_Test.csv")
    message = makeCsvFile.makeScoreCsvFile(input_params["highScoreList"], test_file_name, False, {}, True)
    assert message == "ハイスコアデータの作成に成功しました。"
    assert filecmp.cmp(test_file_name, "test/model/makeCsvFile/result/makeScoreCsvFile_one_marge.csv")


def test_three_data_marge():
    input_params = readFileStr("makeScoreCsvFile_three_rank_marge.json")
    test_file_name = os.path.join(os.getcwd(), "scoreData_Test.csv")
    message = makeCsvFile.makeScoreCsvFile(input_params["highScoreList"], test_file_name, True, input_params["rank"], True)
    assert message == "ハイスコアデータの作成に成功しました。"
    assert filecmp.cmp(test_file_name, "test/model/makeCsvFile/result/makeScoreCsvFile_three_marge.csv")


def test_fileOutput_failed(mocker):
    mocker.patch("csv.writer", side_effect=PermissionError())
    highScoreList = []
    test_file_name = os.path.join(os.getcwd(), "scoreData_Test.csv")
    message = makeCsvFile.makeScoreCsvFile(highScoreList, test_file_name, True)
    assert message == "指定したファイル名でCSVファイルの出力に失敗しました。"
