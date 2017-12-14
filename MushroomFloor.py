from CSRandom import CSRandom
from Utility import dayToYSD


def find_mushroom_floor(gameID, day):
    mush_floor = None
    for level in range(80, 121):
        rand = CSRandom(day + level + (gameID//2))

        # checks darkness
        if rand.sample() < 0.3:
            rand.sample()
        # checks color lighting for style
        rand.sample()
        if rand.sample() < 0.035 and level % 5 != 0:
            mush_floor = level
    return mush_floor

if __name__ == '__main__':
    import sys
    if len(sys.argv) >= 2:
        gameID = int(sys.argv[1])
    else:
        gameID = 143594438
    dayStart = 1
    dayEnd = 112
    for day in range(dayStart,dayEnd):
        level = find_mushroom_floor(gameID,day)
        if level is None:
            print(dayToYSD(day), '\tNo Mushroom Floor')
        else:
            print(dayToYSD(day), '\tMushroom Floor: ', level)
