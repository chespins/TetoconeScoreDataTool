# -*- coding: utf-8 -*-
from kivy.uix.screenmanager import Screen
from kivy.properties import BooleanProperty
from kivy.lang import Builder

from util import util
from model import createDataFile as crd
from variable.setappdata import AppCommonData
from constant.systemconstant import TETOCONE_DB_NAME
from constant.systemconstant import DB_ERROR_FILE_BREAK
from constant.systemconstant import DB_ERROR_UNKNOWN_FILE
from constant.messeges import DATA_FILE_ERROR
from constant.messeges import DATA_FILE_VERSION_ERROR

Builder.load_file(util.find_data_file('./kvfile/makeDbFile.kv'))


class makeDbFileScreen(Screen):
    def __init__(self, comonData: AppCommonData, **kwargs):
        super(makeDbFileScreen, self).__init__(**kwargs)
        self.commonData = comonData
        self.ids.fileName.text = TETOCONE_DB_NAME
        if self.commonData.checkDbresult == DB_ERROR_FILE_BREAK:
            self.ids.message.text = DATA_FILE_ERROR
        elif self.commonData.checkDbresult == DB_ERROR_UNKNOWN_FILE:
            self.ids.message.text = DATA_FILE_VERSION_ERROR
            self.ids.yesBtn.disabled = True

    def reCreateDbFile(self):
        if self.commonData.checkDbresult == DB_ERROR_FILE_BREAK:
            crd.makeDataFile()

    def readOnlyOpen(self):
        self.commonData.readOnlyFlg = True


if __name__ == '__main__':
    pass
