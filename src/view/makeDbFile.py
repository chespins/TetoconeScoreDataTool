# -*- coding: utf-8 -*-
from kivy.uix.screenmanager import Screen
from kivy.properties import BooleanProperty
from kivy.lang import Builder

from util import util
from model import createDataFile as crd
from variable.setappdata import AppCommonData
from constant import systemconstant as cons
from constant import messeges as msg
from view import menu as mu


Builder.load_file(util.findDataFile(cons.KIVY_CURRENT_DIR + 'makeDbFile.kv'))


class makeDbFileScreen(Screen):
    def __init__(self, comonData: AppCommonData, **kwargs):
        super(makeDbFileScreen, self).__init__(**kwargs)
        self.commonData = comonData
        self.ids.fileName.text = cons.TETOCONE_DB_NAME
        if self.commonData.checkDbresult == cons.DB_ERROR_FILE_BREAK:
            self.ids.message.text = msg.DATA_FILE_ERROR
            self.ids.readOnlyBtn.disabled = True
        elif self.commonData.checkDbresult == cons.DB_UPDATE:
            self.ids.message.text = msg.DATA_FILE_UPDATE
        elif self.commonData.checkDbresult == cons.DB_ERROR_UNKNOWN_FILE:
            self.ids.message.text = msg.DATA_FILE_VERSION_ERROR
            self.ids.yesBtn.disabled = True

    def reCreateDbFile(self):
        if self.commonData.checkDbresult == cons.DB_ERROR_FILE_BREAK:
            crd.reMakeDataFile()
            self.switchingMenu()
        elif self.commonData.checkDbresult == cons.DB_UPDATE:
            self.commonData.dbFileVersion = crd.updateDbFile(self.commonData.dbFileVersion)
            self.switchingMenu()

    def readOnlyOpen(self):
        self.commonData.readOnlyFlg = True
        self.switchingMenu()

    def switchingMenu(self):
        screenName = 'menu'
        self.manager.add_widget(mu.MenuScreen(name=screenName, comonData=self.commonData))
        self.manager.current = screenName
    
    def on_leave(self, *args):
        self.manager.remove_widget(self)
        super().on_leave(*args)    


if __name__ == '__main__':
    pass
