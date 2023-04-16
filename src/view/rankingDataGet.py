# -*- coding: utf-8 -*-
import threading

from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from kivy.clock import Clock

from model import rankingDataGet as ins
from variable.setappdata import AppCommonData
from constant import messeges
from util import util
from constant.systemconstant import KIVY_CURRENT_DIR

Builder.load_file(util.findDataFile(KIVY_CURRENT_DIR + 'rankingDataGet.kv'))


class RankingDataGetScreen(Screen):

    def __init__(self,  comonData: AppCommonData, **kwargs):
        super(RankingDataGetScreen, self).__init__(**kwargs)
        self.commonData = comonData

    def on_pre_enter(self, **kwargs):
        self.ids.loginStatusMessage.text = messeges.DATA_INPORT_RANKING_START
        self.ids.loginStatusMessage.color = [0, 1, 0, 1]
        self.ids.serialNo.text = ''
        self.ids.password.text = ''
        self.ids.serialNo.disabled = False
        self.ids.password.disabled = False
        self.ids.buttonLogin.disabled = False

    def on_leave(self, **kwargs):
        self.manager.remove_widget(self)
        return super().on_leave(*kwargs)

    def bottonLoginMyPage(self):
        self.ids.loginStatusMessage.text = messeges.DATA_INPORT_PROCESS
        self.ids.loginStatusMessage.color = [0, 1, 0, 1]
        self.ids.serialNo.disabled = True
        self.ids.password.disabled = True
        self.ids.buttonLogin.disabled = True
        self.ids.buttonBack.disabled = True

        thread = threading.Thread(target=self.loginMyPage)
        thread.start()

    def loginMyPage(self):
        serialNo = self.ids.serialNo.text
        password = self.ids.password.text
        self.message = ins.getLoginRankingData(serialNo, password, self.commonData.displayChartId)
        Clock.schedule_once(self.endLoginMyPage)

    def endLoginMyPage(self, dt):
        self.ids.loginStatusMessage.text = self.message
        self.ids.buttonBack.disabled = False

        if not self.message == messeges.DATA_INPORT_SUCCESS:
            self.ids.loginStatusMessage.color = [1, 0, 0, 1]
            if not self.message == messeges.DATA_IMPORT_DATA_UNMATCH:
                self.ids.serialNo.disabled = False
                self.ids.password.disabled = False
                self.ids.buttonLogin.disabled = False


if __name__ == '__main__':
    pass
