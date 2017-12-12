from CSRandom import CSRandom
from ObjectInfo import ObjectInfo
from Utility import dayToYSD

def findMushroomFloor(gameID,day):
	mush_floor = None
	for level in range(80,121):
		rand = CSRandom(day + level + (gameID//2))
		
		# checks darkness
		if rand.Sample() < 0.3:
			rand.Sample() 
		# checks color lighting for style
		rand.Sample()
		if rand.Sample() < 0.035 and level % 5 != 0:
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
		level = findMushroomFloor(gameID,day)
		if level is None:
			print(dayToYSD(day),'\tNo Mushroom Floor')
		else:
			print(dayToYSD(day),'\tMushroom Floor: ',level)

