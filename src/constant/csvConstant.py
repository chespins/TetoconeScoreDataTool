# -*- coding: utf-8 -*-
from  variable import csvdata as da

# dataType
DATA_TYPE_OUTHER = da.CsvDataType(False, False, False, False, False, False)
DATA_TYPE_GENRU = da.CsvDataType(False, False, False, False, False, True)
DATA_TYPE_COUNT = da.CsvDataType(False, False, False, False, True, False)
DATA_TYPE_MODE = da.CsvDataType(False, False, False, True, False, False)
DATA_TYPE_LEVEL = da.CsvDataType(False, False, True, False, False, False)
DATA_TYPE_TIME = da.CsvDataType(False, True, False, False, False, False)
DATA_TYPE_RANK = da.CsvDataType(True, False, False, False, False, False)

# sourceDataName
SOURCE_CHART = "chart"
SOURCE_HIGH_SCORE = "highScore"
SOURCE_RANK_HISTORY = "rankHistory"

# csvHeader score
SCORE_HEADER_MUSIC_NAME = da.CsvDataHeader(SOURCE_HIGH_SCORE, "musicName", "楽曲名", DATA_TYPE_OUTHER)
SCORE_HEADER_LEVEL_NAME = da.CsvDataHeader(SOURCE_HIGH_SCORE, "levelId", "難易度", DATA_TYPE_LEVEL)
SCORE_HEADER_PLAY_MODE = da.CsvDataHeader(SOURCE_HIGH_SCORE, "mode", "プレイモード", DATA_TYPE_MODE)
SCORE_HEADER_GUNRU_NAME = da.CsvDataHeader(SOURCE_HIGH_SCORE, "genreId", "ジャンル", DATA_TYPE_GENRU)
SCORE_HEADER_HIGH_SCORE = da.CsvDataHeader(SOURCE_HIGH_SCORE, "highScore", "ハイスコア", DATA_TYPE_COUNT)
SCORE_HEADER_MAX_COMBO = da.CsvDataHeader(SOURCE_HIGH_SCORE, "maxCombo", "最高コンボ", DATA_TYPE_COUNT)
SCORE_HEADER_PLAY_COUNT = da.CsvDataHeader(SOURCE_HIGH_SCORE, "playCount", "プレイ回数", DATA_TYPE_COUNT)
SCORE_HEADER_CLEAR_COUNT = da.CsvDataHeader(SOURCE_HIGH_SCORE, "clearedCount", "クリア回数", DATA_TYPE_COUNT)
SCORE_HEADER_FULL_COMBO_COUNT = da.CsvDataHeader(SOURCE_HIGH_SCORE, "fullComboCount", "フルコンボ回数", DATA_TYPE_COUNT)
SCORE_HEADER_PERFECT_COUNT = da.CsvDataHeader(SOURCE_HIGH_SCORE, "perfectCount", "パーフェクト回数", DATA_TYPE_COUNT)
SCORE_HEADER_UPDATE_TIME = da.CsvDataHeader(SOURCE_HIGH_SCORE, "updateTime", "最終プレイ日時", DATA_TYPE_TIME)
SCORE_HEADER_RANK_SSS = da.CsvDataHeader(SOURCE_RANK_HISTORY, "SSS", "SS+達成回数", DATA_TYPE_RANK)
SCORE_HEADER_RANK_SS = da.CsvDataHeader(SOURCE_RANK_HISTORY, "SS", "SS達成回数", DATA_TYPE_RANK)
SCORE_HEADER_RANK_S = da.CsvDataHeader(SOURCE_RANK_HISTORY, "S", "S達成回数", DATA_TYPE_RANK)
SCORE_HEADER_RANK_AAA = da.CsvDataHeader(SOURCE_RANK_HISTORY, "AAA", "AA+達成回数", DATA_TYPE_RANK)
SCORE_HEADER_RANK_AA = da.CsvDataHeader(SOURCE_RANK_HISTORY, "AA", "AA達成回数", DATA_TYPE_RANK)
SCORE_HEADER_RANK_A = da.CsvDataHeader(SOURCE_RANK_HISTORY, "A", "A達成回数", DATA_TYPE_RANK)
SCORE_HEADER_RANK_BBB = da.CsvDataHeader(SOURCE_RANK_HISTORY, "BBB", "BB+達成回数", DATA_TYPE_RANK)
SCORE_HEADER_RANK_BB = da.CsvDataHeader(SOURCE_RANK_HISTORY, "BB", "BB達成回数", DATA_TYPE_RANK)
SCORE_HEADER_RANK_B = da.CsvDataHeader(SOURCE_RANK_HISTORY, "B", "B達成回数", DATA_TYPE_RANK)
SCORE_HEADER_RANK_C = da.CsvDataHeader(SOURCE_RANK_HISTORY, "C", "C達成回数", DATA_TYPE_RANK)
SCORE_HEADER_RANK_D = da.CsvDataHeader(SOURCE_RANK_HISTORY, "D", "D達成回数", DATA_TYPE_RANK)
SCORE_HEADER_RANK_E = da.CsvDataHeader(SOURCE_RANK_HISTORY, "E", "E達成回数", DATA_TYPE_RANK)


CSV_SCORE_INFO_HEADER = [
        SCORE_HEADER_MUSIC_NAME,
        SCORE_HEADER_LEVEL_NAME,
    ]


CSV_SCORE_SCORE_HEADER = [
        SCORE_HEADER_GUNRU_NAME,
        SCORE_HEADER_HIGH_SCORE,
        SCORE_HEADER_MAX_COMBO,
        SCORE_HEADER_PLAY_COUNT,
        SCORE_HEADER_CLEAR_COUNT,
        SCORE_HEADER_FULL_COMBO_COUNT,
        SCORE_HEADER_PERFECT_COUNT,
    ]


CSV_SCORE_RANK_HEADER = [
        SCORE_HEADER_RANK_SSS,
        SCORE_HEADER_RANK_SS,
        SCORE_HEADER_RANK_S,
        SCORE_HEADER_RANK_AAA,
        SCORE_HEADER_RANK_AA,
        SCORE_HEADER_RANK_A,
        SCORE_HEADER_RANK_BBB,
        SCORE_HEADER_RANK_BB,
        SCORE_HEADER_RANK_B,
        SCORE_HEADER_RANK_C,
        SCORE_HEADER_RANK_D,
        SCORE_HEADER_RANK_E,
    ]
