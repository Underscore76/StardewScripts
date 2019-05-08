from CSRandom import CSRandomLite
from ObjectInfo import ObjectInfo
from Utility import dayToYSD
import sys

def findMushroomFloor(gameID,day):
	mush_floor = []
	for level in range(80,121):
		rand = CSRandomLite(day + level + (gameID//2))
		
		# checks darkness
		if rand.Sample() < 0.3:
			rand.Sample() 
		# checks color lighting for style
		rand.Sample()
		if rand.Sample() < 0.035 and level % 5 != 0:
			mush_floor.append(level)
	return mush_floor if mush_floor else list()

def checkMonsterFloor(gameID, day, level):
	if level % 40 % 20 != 0 or level % 40 == 0:
		if level % 10 != 0:
			num = level % 40
		else:
			num = 10
	else:
		num = 20
	if level == 120:
		num = 120
	rand = CSRandomLite(day + level +(gameID//2))
	if rand.Sample() < 0.05 and num % 5 != 0 and num % 40 > 5 and num % 40 < 30 and num % 40 != 19:
		if rand.Sample() < 0.5:
			return "Monster Area"
		else:
			return "Slime Area"
	return ""

if __name__ == '__main__':
	if len(sys.argv) >= 2:
		gameID = int(sys.argv[1])
	else:
		gameID = 143594438
	dayStart = 1
	dayEnd = 112
	for day in range(dayStart,dayEnd):
		level = findMushroomFloor(gameID,day)
		if level is None:
			print(dayToYSD(day),'\tNo Mushroom Floor')
		else:
			print(dayToYSD(day),'\tMushroom Floor: ',level)

	print("Day 5 Floor Status")
	for level in range(1,121):
		status = checkMonsterFloor(gameID, 5, level)
		if status != "":
			print(level, '\t', status)

