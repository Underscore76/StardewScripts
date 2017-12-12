from CSRandom import CSRandom

def harvest_quality(gameID, dayNumber, fLevel, xTile, yTile, fertilizer=None):
	number = 1
	quality = 0
	num3 = 0
	if fertilizer != None:
		if fertilizer == 'Basic':
			num3 = 1
		elif fertilizer == 'Quality':
			num3 = 2

	rand = CSRandom(xTile*7 + yTile*11 + gameID + dayNumber)
	num4 = 0.2 * (fLevel/10.0) + 0.2 * num3 * (fLevel+2.0)/12.0 + 0.01
	num5 = min(0.75, num4*2.0)
	if rand.Sample() < num4:
		quality = 2
	elif rand.Sample() < num5:
		quality = 1
	
	return quality

if __name__ == '__main__':
	import sys
	def printArr(arr):
		print('\n'.join(' '.join('%2d'%cell for cell in row) for row in arr))
	def printHouse():
		print('__ __ __ __ __ __ __ __ Gr Ho Ho Ho Ho St St St Ho Ho Ma Gr Gr __ Pa Gr Gr Gr')
		print('__ __ __ __ __ __ __ __ Gr Gr Gr Gr Gr Gr Gr Gr Gr Gr Gr Gr __ __ Pa Pa Pa Pa')
	if len(sys.argv) >= 2:
		gameID = int(sys.argv[1])
	else: 
		gameID = 143594438
	# Location in front of house	
	yStart=18
	yEnd=27
	xStart=50
	xEnd=75
	
	dayStart= 5
	dayEnd = 28
	fLevel = 0

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
		
	days[quality != 2] = 0
	print('Day:')
	printHouse()
	printArr(days)
