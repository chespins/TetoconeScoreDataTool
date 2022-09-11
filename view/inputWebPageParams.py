# -*- coding: utf-8 -*-
import threading

from kivy.uix.screenmanager import Screen
from kivy.properties import StringProperty
from kivy.lang import Builder
from kivy.clock import Clock

from model import getloginpage as ins
from constant import messeges
from util import util

Builder.load_file(util.find_data_file('.\\kvfile\\inputWebPageParams.kv'))


class InputWebPageParamsScreen(Screen):
    text = StringProperty()

    def __init__(self, **kwargs):
        super(InputWebPageParamsScreen, self).__init__(**kwargs)
        self.ids.loginStatusMessage.text = messeges.DATA_INPORT_START
        self.ids.loginStatusMessage.color = [0, 1, 0, 1]
        self.ids.serialNo.text = ''
        self.ids.password.text = ''
        self.ids.serialNo.disabled = False
        self.ids.password.disabled = False
        self.ids.buttonLogin.disabled = False

    def on_leave(self, **kwargs):
        self.ids.loginStatusMessage.text = ''
        self.ids.serialNo.text = ''
        self.ids.password.text = ''
        self.ids.serialNo.disabled = False
        self.ids.password.disabled = False
        self.ids.buttonLogin.disabled = False

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
        self.message = ins.getLoginPageData(serialNo, password)
        Clock.schedule_once(self.endLoginMyPage)

    def endLoginMyPage(self, dt):
        self.ids.loginStatusMessage.text = self.message
        self.ids.buttonBack.disabled = False

        if not self.message == messeges.DATA_INPORT_SUCCESS:
            self.ids.loginStatusMessage.color = [1, 0, 0, 1]
            self.ids.serialNo.disabled = False
            self.ids.password.disabled = False
            self.ids.buttonLogin.disabled = False


if __name__ == '__main__':
    pass
