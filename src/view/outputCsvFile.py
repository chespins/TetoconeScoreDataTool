# -*- coding: utf-8 -*-
import os

from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from kivy.properties import BooleanProperty

from variable.setappdata import AppCommonData
from util import util
from constant.systemconstant import KIVY_CURRENT_DIR
from widget.fileChoosePopUp import FileChoosePopUp
from model.outputCsvModel import OutputCsvModel

Builder.load_file(util.findDataFile(KIVY_CURRENT_DIR + 'outputCsvFile.kv'))


class OutPutCsvFile(Screen):
    initialfileName =  "scoreData_" + util.getDateTimeNowFileName() + ".csv"
    selectDir = os.getcwd()
    model = OutputCsvModel()
    rankDisplayedFlg = BooleanProperty(False)
    playModeFlg = BooleanProperty(True)

    def __init__(self,  comonData: AppCommonData, **kwargs):
        super(OutPutCsvFile, self).__init__(**kwargs)
        self.commonData = comonData

    def on_pre_enter(self, **kwargs):
        self.selectDir = os.getcwd()
        self.ids.saveFolder.text = self.selectDir
        self.ids.fileName.text = self.initialfileName

    def on_leave(self, **kwargs):
        self.manager.remove_widget(self)
        return super().on_leave(*kwargs)

    def bottonCsvOutput(self, **kwargs):
        saveFilePath = os.path.join(self.selectDir, self.ids.fileName.text)
        rankFlg = self.rankDisplayedFlg
        margeFlg = not self.playModeFlg
        message = self.model.outputCsvFile(saveFilePath, rankFlg, margeFlg)
        self.ids.message.text = message

    def bottonSelectOutputFileName(self, **kwargs):
        popup = FileChoosePopUp(self.selectDir)                   
        popup.popupEvent.bind(on_popup_closed=self.closeFileChoosePopUp)
        popup.open()

    def closeFileChoosePopUp(self, instance, selectDir):
        if selectDir is not None:
            self.selectDir = selectDir
            self.ids.saveFolder.text = self.selectDir

    def rankDisplayedFlgCheck(self, checkbox):
        self.rankDisplayedFlg = checkbox.active

    def playModeFlgCheck(self, checkbox):
        self.playModeFlg = checkbox.active
