# -*- coding: utf-8 -*-
from kivy.uix.screenmanager import Screen
from kivy.properties import StringProperty
from kivy.properties import ObjectProperty
from kivy.properties import BooleanProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder

from model.abuchement import abuchmentModel
from variable.setappdata import AppCommonData
from util import util
from constant.systemconstant import ABUCHMENT_LIST

Builder.load_file(util.findDataFile('./kvfile/abuchement.kv'))


class AbuchmentScreen(Screen):
    abuchmentRv = ObjectProperty()
    ungetFlg = BooleanProperty(False)
    abu = abuchmentModel()

    def __init__(self, comonData: AppCommonData, **kwargs):
        super(AbuchmentScreen, self).__init__(**kwargs)
        self.ids.LevelSpinnerId.values = self.abu.makeLavalNamePulldown()
        self.ids.LevelSpinnerId.text = ""
        self.ids.abuchmentSpinner.values = ABUCHMENT_LIST
        self.ids.abuchmentSpinner.text = ABUCHMENT_LIST[0]
        self.commonData = comonData

    def resetData(self):
        self.abuchmentRv.data = []
        self.ungetFlg = False

    def serchMusic(self):
        serchLavelName = self.ids.LevelSpinnerId.text
        abuchment = self.ids.abuchmentSpinner.text
        self.abuchmentRv.data = self.abu.serchMusic(abuchment, serchLavelName, self.ungetFlg)

    def checkboxCheck(self, checkbox):
        self.ungetFlg = checkbox.active


class AbuchmentData(BoxLayout):
    musicName = StringProperty()
    levelName = StringProperty()
    playCount = StringProperty()
    perfectCount = StringProperty()
    fullComboCount = StringProperty()


if __name__ == '__main__':
    pass
