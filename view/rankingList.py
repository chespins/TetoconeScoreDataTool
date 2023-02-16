# -*- coding: utf-8 -*-
from kivy.uix.screenmanager import Screen
from kivy.properties import StringProperty
from kivy.properties import ObjectProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder

from model.rankingListGet import RankingListGet as rank
from variable.setappdata import AppCommonData
from util import util
from constant.systemconstant import ABUCHMENT_LIST

Builder.load_file(util.findDataFile('./kvfile/rankingList.kv'))


class RankingListScreen(Screen):
    rankingListRv = ObjectProperty()

    def __init__(self, comonData: AppCommonData, **kwargs):
        super(RankingListScreen, self).__init__(**kwargs)
        self.ids.LevelSpinnerId.values = rank.makeLavalNamePulldown()
        self.ids.LevelSpinnerId.text = ""
        self.ids.genreSpinnerId.values = rank.makeGenreNamePulldown()
        self.ids.genreSpinnerId.text = ""
        self.commonData = comonData

    def resetData(self):
        self.rankingListRv.data = []

    def serchMusic(self):
        serchLavelName = self.ids.LevelSpinnerId.text
        serchGenreName = self.ids.genreSpinnerId.text
        self.rankingListRv.data = rank.searchMusic(serchLavelName, serchGenreName)


class rankingData(BoxLayout):
    musicName = StringProperty()
    levelName = StringProperty()
    highScore = StringProperty()
    maxRank = StringProperty()
    ranking = StringProperty()


if __name__ == '__main__':
    pass
