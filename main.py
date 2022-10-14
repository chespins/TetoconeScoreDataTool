# -*- coding: utf-8 -*-
from kivy.app import App
from kivy.core.text import LabelBase, DEFAULT_FONT
from kivy.resources import resource_add_path
from kivy.uix.screenmanager import ScreenManager
from kivy.config import Config

from view import highScoreSelected as hss
from view import inputWebPageParams as web
from view import highScoreDetails as det
from view import highScoreHistoryDetails as his
from view import abuchement as abu
from view import license
from view import menu as mu
from view import makeDbFile as mkd
from variable.setappdata import AppCommonData
from util import util

Config.set('graphics', 'width', '640')
Config.set('graphics', 'height', '480')

resource_add_path(util.find_data_file('./fonts'))
LabelBase.register(DEFAULT_FONT, 'Corporate-Mincho-ver2.otf')


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
        self.sm.add_widget(
                mu.MenuScreen(
                        comonData=self.appCommonData,
                        name='menu'
                    )
            )
        self.sm.add_widget(
                hss.HighScoreSelectScreen(
                        comonData=self.appCommonData,
                        name='highScoreSelect'
                    )
            )
        self.sm.add_widget(
                web.InputWebPageParamsScreen(name='webData')
            )
        self.sm.add_widget(
                det.HighScoreDetailsScreen(
                        comonData=self.appCommonData,
                        name='details'
                    )
            )
        self.sm.add_widget(
                his.HighScoreHistoryDetailsScreen(
                        comonData=self.appCommonData,
                        name='history'
                    )
            )
        self.sm.add_widget(
                license.LicenseScreen(
                        name='license'
                    )
            )
        self.sm.add_widget(
                abu.AbuchmentScreen(
                        comonData=self.appCommonData,
                        name='abuchment'
                    )
            )
        return self.sm

    def showHighScore(self, chartId):
        self.appCommonData.setDisplayChartId(chartId)
        self.sm.current = "details"


if __name__ == '__main__':
    TetoconeScoreApp().run()
