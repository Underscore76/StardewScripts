from CSRandom import CSRandomLite
import numpy as np

# experience is NOT based on quality
# quality is just money equivalent
def harvest_quality(gameID, dayNumber, fLevel, xTile, yTile, fertilizer=None):
	number = 1
	quality = 0
	num3 = 0
	if fertilizer != None:
		if fertilizer == 'Basic':
			num3 = 1
		elif fertilizer == 'Quality':
			num3 = 2

	rand = CSRandomLite(xTile*7 + yTile*11 + gameID + dayNumber)
	num4 = 0.2 * (fLevel/10.0) + 0.2 * num3 * (fLevel+2.0)/12.0 + 0.01
	num5 = min(0.75, num4*2.0)
	if rand.Sample() < num4:
		quality = 2
	elif rand.Sample() < num5:
		quality = 1
	
	return quality

def find_best_days(seed, season, fLevel, xTile, yTile, fertilizer=None):
    max_quality = -1
    days = []
    for dayInMonth in range(1, 28 + 1):
        day = (season-1)*28 + dayInMonth
        if (season % 4) == 0:
            continue
        if (season % 4) == 1:
            if dayInMonth < 5:
                continue
        if (season % 4) == 2:
            if dayInMonth < 13:
                continue
        if (season % 4) == 3:
            if dayInMonth < 15:
                continue
        quality = harvest_quality(seed, day, fLevel, xTile, yTile, fertilizer)
        if quality > max_quality:
            days = [day]
            max_quality = quality
        elif quality == max_quality:
            days.append(dayInMonth)
    return max_quality, days
	
if __name__ == '__main__':
	def printArr(arr):
		print('\n'.join(' '.join('%2d'%cell for cell in row) for row in arr))
	yStart=18
	yEnd=27
	xStart=50
	xEnd=75
	
	dayStart= 43
	dayEnd = 43
	gameID = 143594438
	fLevel = 2

	import numpy as np

	quality = np.zeros((yEnd-yStart+1,xEnd-xStart+1),dtype=np.int)
	days = np.zeros((yEnd-yStart+1,xEnd-xStart+1),dtype=np.int)
	
	for x in range(xStart,xEnd+1):
		for y in range(yStart,yEnd+1):
			for d in range(dayStart,dayEnd+1):
				q = harvest_quality(gameID,d,fLevel,x,y)
				if q > quality[y-yStart,x-xStart]:
					quality[y-yStart,x-xStart] = q
					days[y-yStart,x-xStart] = d
		
	
	print('Quality:')
	printArr(quality)
	print('Day:')
	printArr(days)
