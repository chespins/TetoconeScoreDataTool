# -*- coding: utf-8 -*-

from kivy.uix.screenmanager import Screen
from kivy.lang import Builder

from util import util
from variable.setappdata import AppCommonData
from constant.systemconstant import KIVY_CURRENT_DIR

Builder.load_file(util.findDataFile(KIVY_CURRENT_DIR + 'menu.kv'))


class MenuScreen(Screen):
    def __init__(self, comonData: AppCommonData, **kwargs):
        super(MenuScreen, self).__init__(**kwargs)
        self.commonData = comonData

    def on_pre_enter(self, **kwargs):
        self.ids.webData.disabled = self.commonData.readOnlyFlg
        self.ids.rankingCheck.disabled = not self.commonData.checkRankingData()
        degreesDis = not self.commonData.checkDegreesData()
        self.ids.characterData.disabled = degreesDis
        self.ids.degreesList.disabled =  degreesDis


if __name__ == '__main__':
    pass
