# -*- coding: utf-8 -*-

from kivy.uix.screenmanager import Screen
from kivy.lang import Builder

from util import util
from variable.setappdata import AppCommonData
from constant.systemconstant import KIVY_CURRENT_DIR
from view import degreesList as deg
from view import characterData as cha
from view import license as lic
from view import inputWebPageParams as web
from view import highScoreSelected as hss
from view import abuchement as abu
from view import rankingList as rak


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

    def switchingDegreesList(self):
        screenName = 'degreesList'
        self.manager.add_widget(deg.DegreesList(name=screenName))
        self.manager.current = screenName

    def switchingCharacterData(self):
        screenName = 'characterData'
        self.manager.add_widget(cha.characterDataScreen(name=screenName))
        self.manager.current = screenName

    def switchingLicense(self):
        screenName = 'license'
        self.manager.add_widget(lic.LicenseScreen(name=screenName))
        self.manager.current = screenName

    def switchingWebData(self):
        screenName = 'webData'
        self.manager.add_widget(web.InputWebPageParamsScreen(name=screenName))
        self.manager.current = screenName

    def switchingHighScoreSelect(self):
        screenName = 'highScoreSelect'
        self.manager.add_widget(hss.HighScoreSelectScreen(name=screenName, comonData=self.commonData))
        self.manager.current = screenName

    def switchingRankingList(self):
        screenName = 'rankingList'
        self.manager.add_widget(rak.RankingListScreen(name=screenName, comonData=self.commonData))
        self.manager.current = screenName

    def switchingAbuchment(self):
        screenName = 'abuchment'
        self.manager.add_widget(abu.AbuchmentScreen(name=screenName, comonData=self.commonData))
        self.manager.current = screenName


if __name__ == '__main__':
    pass
