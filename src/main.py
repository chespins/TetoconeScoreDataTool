# -*- coding: utf-8 -*-
import os

from kivy.app import App
from kivy.core.text import LabelBase
from kivy.core.text import DEFAULT_FONT
from kivy.resources import resource_add_path
from kivy.uix.screenmanager import ScreenManager
from kivy.config import Config

from view import menu as mu
from view import makeDbFile as mkd
from variable.setappdata import AppCommonData
from util import util
from constant.systemconstant import FONT_DIR
from constant.systemconstant import FONT_FILE_NAME

os.environ['KIVY_GL_BACKEND'] = 'sdl2'
os.environ['KIVY_NO_CONSOLELOG'] = '1'

Config.set('graphics', 'width', '640')
Config.set('graphics', 'height', '480')

resource_add_path(util.findDataFile(FONT_DIR))
LabelBase.register(DEFAULT_FONT, FONT_FILE_NAME)

class TetoconeScoreApp(App):
    def build(self):
        self.appCommonData = AppCommonData()
        self.sm = ScreenManager()
        if self.appCommonData.checkDbresult != 0:
                self.sm.add_widget(
                        mkd.makeDbFileScreen(
                                comonData=self.appCommonData,
                                name='dbFile'
                        )
                )
        else:
                self.sm.add_widget(
                        mu.MenuScreen(
                                comonData=self.appCommonData,
                                name='menu'
                        )
                )
        
        return self.sm

if __name__ == '__main__':
    TetoconeScoreApp().run()
