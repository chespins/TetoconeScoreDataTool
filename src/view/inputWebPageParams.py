# -*- coding: utf-8 -*-
import threading

from kivy.uix.screenmanager import Screen
from kivy.properties import BooleanProperty
from kivy.lang import Builder
from kivy.clock import Clock

from model import getloginpage as ins
from constant import messeges
from util import util
from constant.systemconstant import KIVY_CURRENT_DIR

Builder.load_file(util.findDataFile(KIVY_CURRENT_DIR + 'inputWebPageParams.kv'))


class InputWebPageParamsScreen(Screen):
    scoreGetFlg = BooleanProperty(True)
    degreesGetFlg = BooleanProperty(True)
    characterGetFlg = BooleanProperty(True)
    rankingGetFlg = BooleanProperty(True)
    standardGetFlg = BooleanProperty(True)
    expertGetFlg = BooleanProperty(True)
    ultimateGetFlg = BooleanProperty(True)
    maniacGetFlg = BooleanProperty(True)
    connectGetFlg = BooleanProperty(True)

    def __init__(self, **kwargs):
        super(InputWebPageParamsScreen, self).__init__(**kwargs)
        self.ids.loginStatusMessage.text = messeges.DATA_INPORT_START
        self.ids.loginStatusMessage.color = [0, 1, 0, 1]
        self.ids.serialNo.text = ''
        self.ids.password.text = ''
        self.ids.serialNo.disabled = False
        self.ids.password.disabled = False
        self.ids.buttonLogin.disabled = False
        self.setRankingLevel()

    def on_leave(self, **kwargs):
        self.manager.remove_widget(self)
        super().on_leave(*kwargs) 

    def bottonLoginMyPage(self):
        self.ids.loginStatusMessage.text = messeges.DATA_INPORT_PROCESS
        self.ids.loginStatusMessage.color = [0, 1, 0, 1]
        self.ids.serialNo.disabled = True
        self.ids.password.disabled = True
        self.ids.buttonLogin.disabled = True
        self.ids.buttonBack.disabled = True
        self.ids.checkBoxScore.disabled = True
        self.ids.checkBoxDegrees.disabled = True
        self.ids.checkBoxCharacter.disabled = True
        self.ids.checkBoxranking.disabled = True
        self.ids.checkBoxStandard.disabled = True
        self.ids.checkBoxExpert.disabled = True
        self.ids.checkBoxUltimate.disabled = True
        self.ids.checkBoxManiac.disabled = True
        self.ids.checkBoxConnect.disabled = True

        thread = threading.Thread(target=self.loginMyPage)
        thread.start()

    def loginMyPage(self):
        serialNo = self.ids.serialNo.text
        password = self.ids.password.text
        self.message = ins.getLoginPageData(serialNo, password, self.scoreGetFlg, self.rankingGetFlg,
                self.standardGetFlg, self.expertGetFlg, self.ultimateGetFlg, 
                self.maniacGetFlg, self.connectGetFlg, self.degreesGetFlg, self.characterGetFlg
            )
        Clock.schedule_once(self.endLoginMyPage)

    def endLoginMyPage(self, dt):
        self.ids.loginStatusMessage.text = self.message
        self.ids.buttonBack.disabled = False

        if not self.message == messeges.DATA_INPORT_SUCCESS:
            self.ids.loginStatusMessage.color = [1, 0, 0, 1]
            self.ids.serialNo.disabled = False
            self.ids.password.disabled = False
            self.ids.buttonLogin.disabled = False
            self.setRankingLevel()

    def scoreGetFlgCheck(self, checkbox):
        self.scoreGetFlg = checkbox.active

    def degreesGetFlgCheck(self, checkbox):
        self.degreesGetFlg = checkbox.active

    def characterGetFlgCheck(self, checkbox):
        self.characterGetFlg = checkbox.active

    def rankingGetFlgCheck(self, checkbox):
        self.rankingGetFlg = checkbox.active
        self.setRankingLevel()

    def standardGetFlgCheck(self, checkbox):
        self.standardGetFlg = checkbox.active

    def expertGetFlgCheck(self, checkbox):
        self.expertGetFlg = checkbox.active

    def ultimateGetFlgCheck(self, checkbox):
        self.ultimateGetFlg = checkbox.active

    def maniacGetFlgCheck(self, checkbox):
        self.maniacGetFlg = checkbox.active

    def connectGetFlgCheck(self, checkbox):
        self.connectGetFlg = checkbox.active
    
    def setRankingLevel(self):
        self.ids.checkBoxScore.disabled = False
        self.ids.checkBoxDegrees.disabled = False
        self.ids.checkBoxCharacter.disabled = False
        self.ids.checkBoxranking.disabled = False
        self.ids.checkBoxStandard.disabled = not self.rankingGetFlg
        self.ids.checkBoxExpert.disabled = not self.rankingGetFlg
        self.ids.checkBoxUltimate.disabled = not self.rankingGetFlg
        self.ids.checkBoxManiac.disabled = not self.rankingGetFlg
        self.ids.checkBoxConnect.disabled = not self.rankingGetFlg


if __name__ == '__main__':
    pass
