# -*- coding: utf-8 -*-
from kivy.uix.screenmanager import Screen
from kivy.properties import StringProperty
from kivy.properties import ObjectProperty
from kivy.properties import BooleanProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder

from model.abuchement import abuchmentModel
from variable.setappdata import AppCommonData
from view.baseScoreListScreen import BaseScoreListScreen
from util import util
from constant.systemconstant import ABUCHMENT_LIST
from constant.systemconstant import KIVY_CURRENT_DIR

Builder.load_file(util.findDataFile(KIVY_CURRENT_DIR + 'abuchement.kv'))


class AbuchmentScreen(BaseScoreListScreen):
    abuchmentRv = ObjectProperty()
    ungetFlg = BooleanProperty(False)
    abu = abuchmentModel()

    def __init__(self, comonData: AppCommonData, **kwargs):
        super(AbuchmentScreen, self).__init__(commonData=comonData, **kwargs)
        self.ids.LevelSpinnerId.values = self.abu.makeLavalNamePulldown()
        self.ids.LevelSpinnerId.text = ""
        self.ids.abuchmentSpinner.values = ABUCHMENT_LIST
        self.ids.abuchmentSpinner.text = ABUCHMENT_LIST[0]

    def serchMusic(self):
        serchLavelName = self.ids.LevelSpinnerId.text
        abuchment = self.ids.abuchmentSpinner.text
        self.abuchmentRv.data = self.abu.searchMusic(abuchment, serchLavelName, self.ungetFlg)

    def checkboxCheck(self, checkbox):
        self.ungetFlg = checkbox.active


class AbuchmentData(BoxLayout):
    musicName = StringProperty()
    levelName = StringProperty()
    playCount = StringProperty()
    perfectCount = StringProperty()
    fullComboCount = StringProperty()
    chartId = StringProperty()
    detailsFlg = BooleanProperty(False)

    def showHighScore(self, chartId):
        self.parent.parent.parent.parent.parent.parent.parent.switchingHighScoreDetails(chartId, "abuchment")


if __name__ == '__main__':
    pass
