from CSRandom import CSRandom
from ObjectInfo import ObjectInfo
import Utility

def checkRainIn2Days(gameID,day,steps):
	rand = CSRandomLite(gameID//100 + day*10 + 1 + steps)
	for i in range(day):
		rand.Next()

	dishOfTheDay = rand.Next(194,240)
	num = rand.Next(1,4 + (0 if rand.Sample() > 0.08 else 10))
	if dishOfTheDay == 217:
		dishOfTheDay = 216
		num = rand.Next(1,4 + (0 if rand.Sample() > 0.08 else 10))

	if rand.Sample() >= 0.8:
		dailyLuck = rand.Next(-100,101)/1000.0
	else:
		dailyLuck = 0.1

	chanceToRain = 0.183

	if rand.Sample() < chanceToRain:
		return True
	else:
		return False

if __name__ == '__main__':
	gameID = 143594438
	day = 5
	count = 0
	for steps in range(30,300):
		if checkRainIn2Days(gameID,day-2,steps):
			print('Will rain on ',Utility.dayToYSD(day), 'with steps:',steps)
			count+=1
			if count > 3:
				break

	
