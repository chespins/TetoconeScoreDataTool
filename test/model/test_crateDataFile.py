# coding:utf-8
import pytest
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..\\..\\src\\'))
from model import createDataFile
from exception.dbversionError import DBVersionError


def test_checkDbVersion_no_file(mocker):
    isfile_mock = mocker.patch("os.path.isfile", return_value=False)
    make_mock = mocker.patch("model.createDataFile.makeDbFile")
    db_mock = mocker.patch("db.dbversion.getDbVersion", return_value="v0")
    assert createDataFile.checkDbVersion() == (0, "v0.8")
    isfile_mock.assert_called_once()
    isfile_mock.assert_called_with("tetocone.db")
    make_mock.assert_called_once()
    make_mock.assert_called_with()
    db_mock.assert_not_called()


def test_checkDbVersion_v08(mocker):
    isfile_mock = mocker.patch("os.path.isfile", return_value=True)
    make_mock = mocker.patch("model.createDataFile.makeDbFile")
    db_mock = mocker.patch("db.dbversion.getDbVersion", return_value="v0.8")
    assert createDataFile.checkDbVersion() == (0, "v0.8")
    isfile_mock.assert_called_once()
    isfile_mock.assert_called_with("tetocone.db")
    db_mock.assert_called_once()
    db_mock.assert_called_with()
    make_mock.assert_not_called()


def test_checkDbVersion_v05(mocker):
    isfile_mock = mocker.patch("os.path.isfile", return_value=True)
    make_mock = mocker.patch("model.createDataFile.makeDbFile")
    db_mock = mocker.patch("db.dbversion.getDbVersion", return_value="v0.5")
    assert createDataFile.checkDbVersion() == (1, "v0.5")
    isfile_mock.assert_called_once()
    isfile_mock.assert_called_with("tetocone.db")
    db_mock.assert_called_once()
    db_mock.assert_called_with()
    make_mock.assert_not_called()


def test_checkDbVersion_unknown(mocker):
    isfile_mock = mocker.patch("os.path.isfile", return_value=True)
    make_mock = mocker.patch("model.createDataFile.makeDbFile")
    db_mock = mocker.patch("db.dbversion.getDbVersion", return_value="v0.4")
    assert createDataFile.checkDbVersion() == (-2, "v0.4")
    isfile_mock.assert_called_once()
    isfile_mock.assert_called_with("tetocone.db")
    db_mock.assert_called_once()
    db_mock.assert_called_with()
    make_mock.assert_not_called()


def test_checkDbVersion_break(mocker):
    isfile_mock = mocker.patch("os.path.isfile", return_value=True)
    make_mock = mocker.patch("model.createDataFile.makeDbFile")
    db_mock = mocker.patch("db.dbversion.getDbVersion", side_effect=DBVersionError())
    assert createDataFile.checkDbVersion() == (-1, "")
    isfile_mock.assert_called_once()
    isfile_mock.assert_called_with("tetocone.db")
    db_mock.assert_called_once()
    db_mock.assert_called_with()
    make_mock.assert_not_called()


def test_reMakeDataFile(mocker):
    remove_mock = mocker.patch("os.remove")
    make_mock = mocker.patch("model.createDataFile.makeDbFile")
    assert createDataFile.reMakeDataFile()
    remove_mock.assert_called_once()
    remove_mock.assert_called_with("tetocone.db")
    make_mock.assert_called_once()
    make_mock.assert_called_with()


def test_makeDbFile(mocker):
    db_mock = mocker.patch("db.dbversion.ddlInsert")
    update_mock = mocker.patch("model.createDataFile.dbUpdateFrom05")
    assert createDataFile.makeDbFile()
    db_mock.assert_called_once()
    db_mock.assert_called_with()
    update_mock.assert_called_once()
    update_mock.assert_called_with()


def test_dbUpdateFrom05(mocker):
    db_mock = mocker.patch("db.dbversion.dbUpdateFrom05")
    assert createDataFile.dbUpdateFrom05()
    db_mock.assert_called_once()
    db_mock.assert_called_with()
