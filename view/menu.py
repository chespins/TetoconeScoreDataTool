# -*- coding: utf-8 -*-

from kivy.uix.screenmanager import Screen
from kivy.lang import Builder

from util import util
from variable.setappdata import AppCommonData

Builder.load_file(util.find_data_file('./kvfile/menu.kv'))


class MenuScreen(Screen):
    def __init__(self, comonData: AppCommonData, **kwargs):
        super(MenuScreen, self).__init__(**kwargs)
        self.commonData = comonData

    def on_pre_enter(self, **kwargs):
        self.ids.webData.disabled = self.commonData.readOnlyFlg


if __name__ == '__main__':
    pass
