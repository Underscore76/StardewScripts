import numpy as np
from CSRandom import CSRandomLite
from ObjectInfo import ObjectInfo
import pickle


def getTreasureFromGeode(uniqueIDForThisGame, geode_number, geode_type):
	random = CSRandomLite(geode_number + (uniqueIDForThisGame // 2))
	num = None
	sheet_index = {0:535, 1:536, 2:537, 3: 749}[geode_type]
	if random.Sample() < 0.5:
		num = int(random.Next(3)) * 2 + 1
		if random.Sample() < 0.1:
			num = 10
		if random.Sample() < 0.01:
			num = 20
		if random.Sample() < 0.5:
			r = random.Next(4)
			if r == 0 or r == 1:
				return ObjectInfo[390] # stone
			if r == 2:
				return ObjectInfo[330] # clay
			if r == 3:
				if sheet_index == 535:
					return ObjectInfo[86] # earth crystal
				elif sheet_index == 536:
					return ObjectInfo[84] # frozen tear
				elif sheet_index ==537:
					return ObjectInfo[82] # fire quartz
				return ObjectInfo[82+ random.Next(3)*2]
		elif sheet_index == 535:
			num2 = random.Next(3)
			if num2 == 0:
				return ObjectInfo[378] # copper ore
			if num2 == 1: # assumes that the person is beyond floor 25 in the mines
				return ObjectInfo[380] # iron ore
			if num2 == 2:
				return ObjectInfo[382] # coal
		elif sheet_index == 536:
			r = random.Next(4)
			if r == 0:
				return ObjectInfo[378] # copper ore
			elif r == 1:
				return ObjectInfo[380] # iron ore
			elif r == 2:
				return ObjectInfo[382] # coal
			else:
				return ObjectInfo[384] # gold ore
		else:
			r = random.Next(5)
			if r == 0:
				return ObjectInfo[378] # copper ore
			elif r == 1:
				return ObjectInfo[380] # iron ore
			elif r == 2:
				return ObjectInfo[382] # coal
			elif r == 3:
				return ObjectInfo[384] # gold ore
			else:
				return ObjectInfo[386] # iridium ore
	else:
		geode_items = [538,542,548,549,552,555,556,557,558,566,568,569,571,574,576,121]
		frozen_items = [541,544,545,546,550,551,559,560,561,564,567,572,573,577,123]
		magma_items = [539,540,543,547,553,554,562,563,565,570,575,578,122]
		omni_items = [538,542,548,549,552,555,556,557,558,566,568,569,571,574,576,541,544,545,546,550,551,559,560,561,564,567,572,573,577,539,540,543,547,553,554,562,563,565,570,575,578,121,122,123]
		if sheet_index == 535:
			return ObjectInfo[geode_items[random.Next(len(geode_items))]]
		if sheet_index == 536:
			return ObjectInfo[frozen_items[random.Next(len(frozen_items))]]
		if sheet_index == 537:
			return ObjectInfo[magma_items[random.Next(len(magma_items))]]
		if sheet_index == 749:
			r = random.Next(len(omni_items))
			if random.Sample() < 0.008 and geode_number > 15:
				return ObjectInfo[74]
			try:
				return ObjectInfo[omni_items[r]]
			except IndexError:
				print(r, len(omni_items))
				return ObjectInfo[74]
	return ObjectInfo[390]

def getNumTreasureFromGeode(uniqueIDForThisGame, geode_number, geode_type):
    random = CSRandomLite(geode_number + (uniqueIDForThisGame // 2))
    num = None
    sheet_index = {0:535, 1:536, 2:537, 3: 749}[geode_type]
    if random.Sample() < 0.5:
        num = int(random.Next(3)) * 2 + 1
        if random.Sample() < 0.1:
            num = 10
        if random.Sample() < 0.01:
            num = 20
        if random.Sample() < 0.5:
            r = random.Next(4)
            if r == 0 or r == 1:
                return ObjectInfo[390], num # stone
            if r == 2:
                return ObjectInfo[330], 1 # clay
            if r == 3:
                if sheet_index == 535:
                    return ObjectInfo[86], 1 # earth crystal
                elif sheet_index == 536:
                    return ObjectInfo[84], 1 # frozen tear
                elif sheet_index ==537:
                    return ObjectInfo[82], 1 # fire quartz
                return ObjectInfo[82+ random.Next(3)*2], 1
        elif sheet_index == 535:
            num2 = random.Next(3)
            if num2 == 0:
                return ObjectInfo[378], num # copper ore
            if num2 == 1: # assumes that the person is beyond floor 25 in the mines
                return ObjectInfo[380], num # iron ore
            if num2 == 2:
                return ObjectInfo[382], num # coal
        elif sheet_index == 536:
            r = random.Next(4)
            if r == 0:
                return ObjectInfo[378], num # copper ore
            elif r == 1:
                return ObjectInfo[380], num # iron ore
            elif r == 2:
                return ObjectInfo[382], num # coal
            else:
                return ObjectInfo[384], num # gold ore
        else:
            r = random.Next(5)
            if r == 0:
                return ObjectInfo[378], num # copper ore
            elif r == 1:
                return ObjectInfo[380], num # iron ore
            elif r == 2:
                return ObjectInfo[382], num # coal
            elif r == 3:
                return ObjectInfo[384], num # gold ore
            else:
                return ObjectInfo[386], int(num/2) + 1# iridium ore
    else:
        geode_items = [538,542,548,549,552,555,556,557,558,566,568,569,571,574,576,121]
        frozen_items = [541,544,545,546,550,551,559,560,561,564,567,572,573,577,123]
        magma_items = [539,540,543,547,553,554,562,563,565,570,575,578,122]
        omni_items = [538,542,548,549,552,555,556,557,558,566,568,569,571,574,576,541,544,545,546,550,551,559,560,561,564,567,572,573,577,539,540,543,547,553,554,562,563,565,570,575,578,121,122,123]
        if sheet_index == 535:
            return ObjectInfo[geode_items[random.Next(len(geode_items))]], 1
        if sheet_index == 536:
            return ObjectInfo[frozen_items[random.Next(len(frozen_items))]], 1
        if sheet_index == 537:
            return ObjectInfo[magma_items[random.Next(len(magma_items))]], 1
        if sheet_index == 749:
            r = random.Next(len(omni_items))
            if random.Sample() < 0.008 and geode_number > 15:
                return ObjectInfo[74], 1
            try:
                return ObjectInfo[omni_items[r]], 1
            except IndexError:
                print(r, len(omni_items))
                return ObjectInfo[74], 1
    return ObjectInfo[390], 1

def count_unique_museum(item_set):
	return sum([1 for x in item_set if 'Arch' in x or 'Minerals -' in x]) 

# need a bunch of policy to decide on how to break items
# Scenario: 20x geode, 20x frozen geode, 20x magma geode, 60x omni geode
# Options:
#		1) Sequential order G->F->M->O
#		2) Alternate G->F->M->O each time, last block are all omni
#		3) Alternate G->O->G->O ... F->O->F->O ...
#		4-28) Permutations on (1)
def policy_seq_gfmo(uniqueIDForThisGame, geode_list):
	geode_counter = 0
	results = set()
	for geode_type, geode_count in enumerate(geode_list):
		for i in range(geode_count):
			geode_counter += 1
			results.add(getTreasureFromGeode(uniqueIDForThisGame, geode_counter, geode_type))
	return count_unique_museum(results)

def policy_alt_gfmo(uniqueIDForThisGame, geode_list):
	geode_counter = 0
	current_geodes = geode_list.copy()
	results = set()
	index = 0
	while any(current_geodes):
		if current_geodes[index] > 0:
			geode_counter += 1
			current_geodes[index] -= 1
			results.add(getTreasureFromGeode(uniqueIDForThisGame, geode_counter, index))
		index = (index + 1) % 4
	return count_unique_museum(results)

def policy_alt_gofomo(uniqueIDForThisGame, geode_list):
	geode_counter = 0
	current_geodes = geode_list.copy()
	results = set()
	index = 0
	omni_index = 3
	while any(current_geodes):
		# do the current type
		if current_geodes[index] > 0:
			geode_counter += 1
			current_geodes[index] -= 1
			results.add(getTreasureFromGeode(uniqueIDForThisGame, geode_counter, index))
		# filter in the final result
		if current_geodes[omni_index] > 0:
			geode_counter += 1
			current_geodes[omni_index] -= 1
			results.add(getTreasureFromGeode(uniqueIDForThisGame, geode_counter, omni_index))
		index = (index + 1) % 3
	return count_unique_museum(results)

def determine_break_policy():
	geode_list = [20,20,20,60]
	num_trials = 100000
	policies = [policy_seq_gfmo, policy_alt_gfmo, policy_alt_gofomo]
	results = np.zeros((len(policies), num_trials))
	
	for i in range(num_trials):
		seed = np.random.randint(np.iinfo(np.int32).max)
		for j, policy in enumerate(policies):
			results[j,i] = policy(seed, geode_list)

	save_dict = {
		'raw': results,
		'mean': np.mean(results, axis=1),
		'var': np.var(results, axis=1)
	}
	return save_dict


def single_omni_trial(max_break):
	items = set()
	results = np.zeros(max_break)
	seed = np.random.randint(np.iinfo(np.int32).max)
	for geode_count in range(max_break):
		items.add(getTreasureFromGeode(seed, geode_count+1, 3))
		results[geode_count] = count_unique_museum(items)
	return results


def build_omni_curve(num_trials=10, max_break=10):
	results = np.zeros((num_trials, max_break))

	for index in range(num_trials):
		results[index, :] = single_omni_trial(max_break)
		print(index, results[index, 199])
	return results

if __name__ == '__main__':
	if False:
		save_dict = determine_break_policy()
		print(save_dict)
		with open('geode_data.pkl','wb') as f:
			pickle.dump(save_dict, f)
	else:
		res = build_omni_curve(num_trials=10000,max_break=500)

		print(np.mean(res, axis=0))
		print(np.var(res, axis=0))
		with open('omni_count.pkl', 'wb') as f:
			pickle.dump(res, f)
