# -*- coding: utf-8 -*-

from db import degrees as de
from model.basemodel import BaseModel
from util import util
from constant.distConstant import DEGREE_CATEGORY_DIST


class DegreesSearch(BaseModel):
    def getdegreesList(self, searchCategory, searchMissionLabel):
        category = ""
        degreesList = []

        for categoryKey in DEGREE_CATEGORY_DIST.keys():
            if searchCategory == DEGREE_CATEGORY_DIST[categoryKey]:
                category = categoryKey
                break

        dbDegreesList = de.selectDegrees(category=category, searchMissionLabel=searchMissionLabel)

        for dbDegrees in dbDegreesList:
            categoryName = dbDegrees["category"]
            if dbDegrees["category"] in DEGREE_CATEGORY_DIST.keys():
                categoryName = DEGREE_CATEGORY_DIST[dbDegrees["category"]]

            missionLabel = dbDegrees["missionLabel"]
            if missionLabel is None:
                missionLabel = ""

            degrees = {
                    "degreesId": dbDegrees["degreesId"],
                    "degreesName": dbDegrees["degreesName"],
                    "categoryName": categoryName,
                    "missionLabel": missionLabel,
                    "getDate": util.changeTimeZone(dbDegrees["createdAt"]),
                }
            
            degreesList.append(degrees)
            
        return degreesList
    
    def makeCategoryPullDown(self):
        pulldownList = [""]
        for categoryName in DEGREE_CATEGORY_DIST.values():
            pulldownList.append(categoryName)

        return pulldownList
