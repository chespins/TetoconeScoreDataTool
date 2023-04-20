# -*- coding: utf-8 -*-

from kivy.uix.screenmanager import Screen
from kivy.properties import StringProperty
from kivy.properties import ObjectProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder

from model.highscoredetails import HighScoreFormusic
from util import util
from constant.systemconstant import KIVY_CURRENT_DIR
from variable.setappdata import AppCommonData
from view import highScoreHistoryDetails as his
from view import rankingDataGet as rdg

Builder.load_file(util.findDataFile(KIVY_CURRENT_DIR + 'highScoreDetails.kv'))


class HighScoreDetailsScreen(Screen):
    chartId = StringProperty()
    rankHistoryRv = ObjectProperty()
    dataSet = HighScoreFormusic()
    leaveFlg = False

    def __init__(self, comonData: AppCommonData, **kwargs):
        super(HighScoreDetailsScreen, self).__init__(**kwargs)
        self.commonData = comonData

    def on_pre_enter(self, **kwargs):
        if self.chartId == "":
            self.chartId = self.commonData.displayChartId
            self.setMusicDate()
            modePulldownData = self.dataSet.makeModeNamePulldown(self.chartId)
            defaultMode = modePulldownData[0]
            if self.commonData.isWidgetRankingData():
                defaultMode = self.dataSet.getSinglePlayName()

            self.ids.modeSpinnerId.values = modePulldownData
            self.ids.modeSpinnerId.text = defaultMode
            self.ids.modeSpinnerId.disabled = len(modePulldownData) == 1
            self.setHighScoreData(defaultMode)
        else:
            self.updateRankingData(self.ids.modeSpinnerId.text)
    
    def resetScreen(self, **kwargs) :
        self.leaveFlg = True
        self.manager.current = self.commonData.clearSourceWidget()

    def switchinghistoryData(self):
        screenName = 'history'
        self.manager.add_widget(his.HighScoreHistoryDetailsScreen(name=screenName, comonData=self.commonData))
        self.manager.current = screenName
        
    def switchingRankingData(self):
        screenName = 'rankingGet'
        self.manager.add_widget(rdg.RankingDataGetScreen(name=screenName, comonData=self.commonData))
        self.manager.current = screenName
    
    def on_leave(self, *args):
        if self.leaveFlg:
            self.manager.remove_widget(self)

        return super().on_leave(*args)

    def setMusicDate(self):
        musicInfo = self.dataSet.getMusicName(self.chartId)
        self.ids.levelName.text = musicInfo["levelName"]
        self.ids.levelName.color = musicInfo["levelColor"]
        self.ids.musicName.text = musicInfo["musicName"]
        self.ids.genreName.text = musicInfo["genreName"]

    def setHighScoreData(self, displayedMode):
        highScoreData = self.dataSet.getHighScoreByMusic(self.chartId, displayedMode)
        self.ids.highScore.text = highScoreData["highScore"]
        self.ids.maxCombo.text = highScoreData["maxCombo"]
        self.ids.playCount.text = highScoreData["playCount"]
        self.ids.clearedCount.text = highScoreData["clearedCount"]
        self.ids.fullComboCount.text = highScoreData["fullComboCount"]
        self.ids.perfectCount.text = highScoreData["perfectCount"]
        self.ids.lastPlayDate.text = highScoreData["lastUpdateTime"]
        self.rankHistoryRv.data = self.dataSet.getRankHistoryDataForChartId(self.chartId, displayedMode)
        self.updateRankingData(displayedMode)

    def updateRankingData(self, displayedMode):
        singlePlayFlg = self.dataSet.isSinglePlay(displayedMode)
        rankingDataGetFlg = not self.commonData.readOnlyFlg
        if rankingDataGetFlg:
            self.ids.rankingGetButton.disabled = not singlePlayFlg
            if singlePlayFlg:
                ranking = self.dataSet.makeRankingData(self.chartId)
                if ranking["rankingDisPlayedFlg"]:
                    self.ids.rankingLabel.text = "ランキング"
                    self.ids.rankingData.text = ranking["ranking"]
                    self.ids.rankingGetDate.text = ranking["getDate"]
                    return 
        
        else:
            self.ids.rankingGetButton.disabled = True
            
        self.ids.rankingLabel.text = ""
        self.ids.rankingData.text = ""
        self.ids.rankingGetDate.text = ""


class rankHistory(BoxLayout):
    rank = StringProperty()
    count = StringProperty()


if __name__ == '__main__':
    pass
