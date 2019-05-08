from CSRandom import CSRandomLite
from ObjectInfo import ObjectInfo
from Utility import dayToYSD

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

def findMonsterFloors(gameID, day):
	monster_floors = []
	for level in range(1,120):
		floor = checkMonsterFloor(gameID, day, level)
		if floor != '':
			monster_floors.append((level, floor))
	return monster_floors if monster_floors else []

if __name__ == '__main__':
	idMax = 50000
	days_to_run = [5]

	min_list = [
	(5,1,""),(5,2,""),(5,3,""),(6,4,""),(6,5,""),(6,6,""),(5,1,""),(5,2,""),(5,3,""),(6,4,""),(6,5,""),(6,6,""),(5,1,""),(5,2,""),(5,3,""),(6,4,""),(6,5,""),(6,6,""),
	(5,1,""),(5,2,""),(5,3,""),(6,4,""),(6,5,""),(6,6,""),(5,1,""),(5,2,""),(5,3,""),(6,4,""),(6,5,""),(6,6,""),(5,1,""),(5,2,""),(5,3,""),(6,4,""),(6,5,""),(6,6,"")]
	minID = -1
	for gameID in range(idMax):
		floor_list = []
		for day in days_to_run:
			for level in range(1,121):
				status = checkMonsterFloor(gameID, day, level)
				if status != "":
					floor_list.append((day,level, status))
		if len(floor_list) <= 3:
			print(gameID, floor_list)
		if len(floor_list) < len(min_list):
			minID = gameID
			min_list = floor_list
		elif len(floor_list) == len(min_list):
			if floor_list[0][0] > min_list[0][0]:
				minID = gameID
				min_list = floor_list			
	print(minID, min_list)
	min_list = []
