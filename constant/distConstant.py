# -*- coding: utf-8 -*-

class LevelName():
    def __init__(self, id, name, keyName):
        self.id = id
        self.name = name
        self.keyName = keyName

LEVEL_NAME_DIST = {
    "1": LevelName(1, "STANDARD", "chartIdEasy"),
    "2": LevelName(2, "EXPERT", "chartIdNormal"),
    "3": LevelName(3, "ULTIMATE", "chartIdHard"),
    "4": LevelName(4, "MANIAC", "chartIdManiac"),
    "5": LevelName(5, "CONNECT", "chartIdConnect"),
}

GANRU_NAME_DIST = {
    "G000": "アニメ・ポップス",
    "G001": "バーチャル",
    "G002": "東方アレンジ",
    "G003": "ゲーム",
    "G004": "オリジナル",
    "G005": "バラエティー",
}

MODE_NAME_DIST = {
    "1": "シングルプレイ",
    "2": "協力プレイ(2人)",
    "3": "協力プレイ(3人)",
    "4": "協力プレイ(4人)",
    "5": "対戦プレイ(2人)",
    "6": "対戦プレイ(4人)",
}

RANK_DIST = {
        "SSS": "SS+",
        "SS": "SS",
        "S": "S",
        "AAA": "AA+",
        "AA": "AA",
        "A": "A",
        "BBB": "BB+",
        "BB": "BB",
        "B": "B",
        "C": "C",
        "D": "D",
        "E": "E"
}
