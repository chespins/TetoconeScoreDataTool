# -*- coding: utf-8 -*-
from db import character as cha
from db import highscorehistory as hsh
from db import datainserts as dbin
from db import degrees as deg
from constant import distConstant as lvNa


def InsertMusic(stages):
    musicDist = {}
    chartDist = {}
    highScoreList = []
    highScoreHistoryInportList = []
    rankHistoryList = []

    # 取得したデータを整形し格納
    for stageData in stages:
        # 楽曲情報格納
        music = stageData["stage"]
        if not music["id"] in musicDist.keys():
            music["name"] = music["label"]
            musicDist[music["id"]] = music

            # 難易度情報取得
            for chartIdKey in lvNa.LEVEL_NAME_DIST.values():
                if music[chartIdKey.keyName] is None:
                    continue

                chart = {
                        "chartId": music[chartIdKey.keyName],
                        "musicId": music["id"],
                        "levelId": chartIdKey.id
                    }
                chartDist[chart["chartId"]] = chart

        # 未プレイ楽曲は以後の手順はスキップ
        if stageData["playCount"] == 0:
            continue

        # ハイスコア登録
        highScore = {
                "chartId": stageData["chartId"],
                "mode": stageData["mode"],
                "musicId": stageData["stageId"],
                "highScore": stageData["highScore"],
                "maxCombo": stageData["maxCombo"],
                "playCount": stageData["playCount"],
                "clearedCount": stageData["clearedCount"],
                "fullComboCount": stageData["fullComboCount"],
                "perfectCount": stageData["perfectCount"],
                "updateTime": stageData["updatedAt"]
            }

        highScoreList.append(highScore)
        # 履歴登録
        highScoreHistoryList = hsh.selectHighScoreHistoryByMode(
                highScore["chartId"],
                highScore["mode"]
            )
        historyInsertFlg = True

        # 同一の履歴が登録済なら追加しない
        for highScoreHistory in highScoreHistoryList:
            if (highScoreHistory["highScore"] == highScore["highScore"]
                    and highScoreHistory["maxCombo"] == highScore["maxCombo"]):

                historyInsertFlg = False
                break

        if historyInsertFlg:
            highScoreHistoryInportList.append(highScore)

        # ランク回数登録
        for rankCount in stageData["rankCounts"]:
            rankHistory = {
                "chartId": stageData["chartId"],
                "mode": stageData["mode"],
                "rank": rankCount["rank"],
                "count": rankCount["count"]
                }
            rankHistoryList.append(rankHistory)

    dbin.dbinserts(
            musicDist,
            chartDist,
            highScoreList,
            highScoreHistoryInportList,
            rankHistoryList
        )
    return
    

def insertDegrees(degreesDist):
    degreesList = []
    for category in degreesDist.keys():
        for degrees in degreesDist[category]:
            degreesList.append({
                "degreesId": degrees["playerDegree"]["degreeId"],
                "degreesName": degrees["degreeInfo"]["label"],
                "category": category,
                "missionLabel": degrees["missionLabel"],
                "createdAt": degrees["playerDegree"]["createdAt"],
                "updatedAt": degrees["playerDegree"]["updatedAt"],
            })
    
    deg.insertDegrees(degreesList)
    return


def insertCharacter(characterList):
    dbCharacterList = []
    for characterInfo in characterList:
        character = characterInfo["character"]
        introduction = characterInfo["introduction"]
        dbCharacter = {
            "characterId": character["characterId"],
            "characterName": introduction["label"],
            "introduction": introduction["introduction"],
            "dearnessRank": character["dearnessRank"],
            "dearnessPoint": character["dearness"],
            "isUsed": character["isUsed"],
            "sortIndex": character["character"]["sortIndex"],
            "costumeId": character["costumeId"],
            "updatedAt": character["updatedAt"],
        }
        dbCharacterList.append(dbCharacter)
    
    cha.insertCharacter(dbCharacterList)
    return


if __name__ == '__main__':
    pass
