# -*- coding: utf-8 -*-
from constant import distConstant as dsc


def getLevelIdByName(searchedName) -> int:
    searchLevelId = 0
    for levelName in dsc.LEVEL_NAME_DIST.values():
            if levelName.name == searchedName:
                searchLevelId = levelName.id
                break
    
    return searchLevelId


def getGenreIdByName(searchGenreName) -> str:
    searchGenreId = ""
    for genreId in dsc.GANRU_NAME_DIST.keys():
        if dsc.GANRU_NAME_DIST[genreId] == searchGenreName:
            searchGenreId = genreId
            break
    
    return searchGenreId


if __name__ == '__main__':
    pass
