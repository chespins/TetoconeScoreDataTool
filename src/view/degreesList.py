# -*- coding: utf-8 -*-

from kivy.uix.screenmanager import Screen
from kivy.properties import StringProperty
from kivy.properties import ObjectProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.lang import Builder

from model.degreesSearch import DegreesSearch
from util import util
from constant.systemconstant import KIVY_CURRENT_DIR
from variable.setappdata import AppCommonData

Builder.load_file(util.findDataFile(KIVY_CURRENT_DIR + 'degreesList.kv'))


class DegreesList(Screen):
    degreesRv = ObjectProperty()
    model = DegreesSearch()

    def __init__(self, **kwargs):
        super(DegreesList, self).__init__(**kwargs)
        self.ids.categorySpinnerId.values = self.model.makeCategoryPullDown()
        self.ids.categorySpinnerId.text = ""

    def resetData(self):
        self.degreesRv.data = []
        self.ids.categorySpinnerId.text = ""
        self.ids.searchMissionLabel.text = ""

    def searchDegrees(self):
        categoryName = self.ids.categorySpinnerId.text
        searchMissionLabel = self.ids.searchMissionLabel.text
        self.degreesRv.data = self.model.getdegreesList(categoryName, searchMissionLabel)

    def allDegrees(self):
        self.resetData()
        self.degreesRv.data = self.model.getdegreesList("", "")

    def on_leave(self, *args):
        self.manager.remove_widget(self)
        super().on_leave(*args)


class Degrees(BoxLayout):
    degreesId = StringProperty()
    degreesName = StringProperty()
    categoryName = StringProperty()
    missionLabel = StringProperty()
    getDate = StringProperty()


if __name__ == '__main__':
    pass
