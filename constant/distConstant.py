# -*- coding: utf-8 -*-

class LevelName():
    def __init__(self, id, name, keyName, colorCode):
        self.id = id
        self.name = name
        self.keyName = keyName
        self.colorCode = colorCode

LEVEL_NAME_DIST = {
    "1": LevelName(1, "STANDARD", "chartIdEasy", [0.212, 0.51, 0.894, 1]),
    "2": LevelName(2, "EXPERT", "chartIdNormal", [0.925, 0.271, 0.271, 1]),
    "3": LevelName(3, "ULTIMATE", "chartIdHard", [0.627, 0.204, 0.997, 1]),
    "4": LevelName(4, "MANIAC", "chartIdManiac", [0.29, 0.804, 0.627, 1]),
    "5": LevelName(5, "CONNECT", "chartIdConnect", [1, 0.706, 0.859, 1]),
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

class displayedMode():
    def __init__(self, name, searchedMode):
        self.name = name
        self.searchedMode = searchedMode


DISPLAYED_MODE_DIST = {
    "全て": displayedMode("全て", {1, 2, 3, 4, 5, 6}),
    "シングルプレイ": displayedMode("シングルプレイ", {1}),
    "協力プレイ(全て)": displayedMode("協力プレイ(全て)", {2, 3, 4}),
    "協力プレイ(2人)": displayedMode("協力プレイ(2人)", {2}),
    "協力プレイ(3人)": displayedMode("協力プレイ(3人)", {3}),
    "協力プレイ(4人)": displayedMode("協力プレイ(4人)", {4}),
    "対戦プレイ(全て)": displayedMode("対戦プレイ(全て)", {5, 6}),
    "対戦プレイ(2人)": displayedMode("対戦プレイ(2人)", {5}),
    "対戦プレイ(4人)": displayedMode("対戦プレイ(4人)", {6}),
}


class apiLankName:
    def __init__(self, apiLank, gameLank, colorCode):
        self.id = id
        self.apiLank = apiLank
        self.gameLank = gameLank
        self.colorCode = colorCode


RANK_DIST = {
        "SSS": apiLankName("SSS", "SS+", [1, 0, 1, 0.5]),
        "SS": apiLankName("SS", "SS", [1, 0, 1, 0.5]),
        "S": apiLankName("S", "S", [1, 0, 1, 0.5]),
        "AAA": apiLankName("AAA", "AA+", [1, 0, 1, 0.5]),
        "AA": apiLankName("AA", "AA", [1, 0, 1, 0.5]),
        "A": apiLankName("A", "A", [1, 0, 1, 0.5]),
        "BBB": apiLankName("BBB", "BB+", [1, 0, 1, 0.5]),
        "BB": apiLankName("BB", "BB", [1, 0, 1, 0.5]),
        "B": apiLankName("B", "B", [1, 0, 1, 0.5]),
        "C": apiLankName("C", "C", [1, 0, 1, 0.5]),
        "D": apiLankName("D", "D", [1, 0, 1, 0.5]),
        "E": apiLankName("E", "E", [1, 0, 1, 0.5]),
}
