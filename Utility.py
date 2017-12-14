seasonDict = {0: 'Spring', 1: 'Summer', 2: 'Fall', 3: 'Winter'}


def _dayToYear(day):
    return (day-1) // 112


def _dayToSeason(day):
    season = (day-1) // 28 % 4
    season = season if season in seasonDict.keys() else 0
    return seasonDict[season]


def dayToYSD(day):
    year = _dayToYear(day)
    season = _dayToSeason(day)
    day = 28 if day % 28 == 0 else day % 28
    YSD = 'Year: %1d Season: %s Day: %2d' % (year+1, season, day)
    return YSD
