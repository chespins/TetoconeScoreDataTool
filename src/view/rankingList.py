# -*- coding: utf-8 -*-
from kivy.uix.screenmanager import Screen
from kivy.properties import StringProperty
from kivy.properties import ObjectProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder

from model.rankingListGet import RankingListGet as rank
from variable.setappdata import AppCommonData
from view.baseScoreListScreen import BaseScoreListScreen
from util import util
from constant.systemconstant import KIVY_CURRENT_DIR


Builder.load_file(util.findDataFile(KIVY_CURRENT_DIR + 'rankingList.kv'))


class RankingListScreen(BaseScoreListScreen):
    rankingListRv = ObjectProperty()
    rankModel = rank()

    def __init__(self, comonData: AppCommonData, **kwargs):
        super(RankingListScreen, self).__init__(commonData=comonData, **kwargs)
        self.ids.LevelSpinnerId.values = self.rankModel.makeLavalNamePulldown()
        self.ids.LevelSpinnerId.text = ""
        self.ids.genreSpinnerId.values = self.rankModel.makeGenreNamePulldown()
        self.ids.genreSpinnerId.text = ""
        self.commonData = comonData

    def serchMusic(self):
        serchLavelName = self.ids.LevelSpinnerId.text
        serchGenreName = self.ids.genreSpinnerId.text
        self.rankingListRv.data = self.rankModel.searchMusic(serchLavelName, serchGenreName)


class rankingData(BoxLayout):
    musicName = StringProperty()
    levelName = StringProperty()
    highScore = StringProperty()
    maxRank = StringProperty()
    ranking = StringProperty()

    def showHighScore(self, chartId):
        self.parent.parent.parent.parent.parent.parent.parent.switchingHighScoreDetails(chartId, "rankingList")


if __name__ == '__main__':
    pass
