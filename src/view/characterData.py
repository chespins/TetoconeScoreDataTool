# -*- coding: utf-8 -*-

from kivy.uix.screenmanager import Screen
from kivy.properties import StringProperty
from kivy.properties import ObjectProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.lang import Builder

from model.characterInfo import CharacterInfoModel
from util import util
from constant.systemconstant import KIVY_CURRENT_DIR
from variable.setappdata import AppCommonData

Builder.load_file(util.findDataFile(KIVY_CURRENT_DIR + 'characterData.kv'))


class characterDataScreen(Screen):
    characterNameListRv = ObjectProperty()
    dataSet = CharacterInfoModel()

    def __init__(self, **kwargs):
        super(characterDataScreen, self).__init__(**kwargs)

    def on_pre_enter(self, **kwargs):
        self.dataSet.refreshCharacterData()
        characterList = self.dataSet.getCharacterNameList()
        self.characterNameListRv.data = characterList
        character = self.dataSet.preDisplayedCharacterInfo()
        self.showCharacterInfo(character)

    def setCharacterInfo(self, characterId):
        character = self.dataSet.getCharacterInfo(characterId)
        self.showCharacterInfo(character)

    def showCharacterInfo(self, character):
        self.ids.characterName.text = character["characterName"]
        self.ids.dearnessRank.text = character["dearnessRank"]
        self.ids.dearnessPoint.text = character["dearnessPoint"]
        self.ids.introduction.text = character["introduction"]
        self.ids.rankingData.text = character["dearnessRanking"]
        self.ids.rankingGetDate.text = character["dearnessRankingDate"]
        self.ids.lastPlayDate.text = character["lastPlayDate"]

    def on_leave(self, *args):
        self.manager.remove_widget(self)
        super().on_leave(*args)


class CharacterName(BoxLayout):
    characterId = StringProperty()
    characterName = StringProperty()

    def setCharacterInfo(self, characterId):
        self.parent.parent.parent.parent.parent.parent.parent.setCharacterInfo(characterId)


if __name__ == '__main__':
    pass
