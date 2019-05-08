from itertools import chain
import sys

from ObjectInfo import ObjectInfo
from CSRandom import CSRandomLite as CSRandom
from Utility import dayToYSD
import pprint
import time
from joblib import Parallel, delayed
import json


def item_validity_check(item):
    if item['blacklisted']:
        return False
    elif item['name'] == "Weeds":
        return False
    elif not item['price'] > 0:
        return False
    elif any(category in item['category'] for category in ["Quest", "Minerals", "Arch"]):
        return False
    elif '-' not in item['category']:
        return False
    else:
        return True

def getTravelingMerchantStock(item_data, gameID, dayNumber):
    rand = CSRandom(gameID+dayNumber)
    stock = {}
    for i in range(10):
        index = rand.Next(2, 790)
        while True:
            index = (index+1) % 790
            item = item_data.get(str(index))
            if item is None or not item_validity_check(item):
                continue
            break
        stock[item['name']] = max(rand.Next(1,11)*100, item['price']*rand.Next(3,6))
        count = 1 if (rand.Sample() > 0.1) else 5
    return stock


def check_day(item_data, game_id, day, item_list):
    stock = getTravelingMerchantStock(item_data, game_id, day)
    day_items = {key: stock[key] for key in stock.keys() if key in item_list}
    return day_items

def scan_seed(item_data, seed, item_list, start_week=3, end_week=36):
    days = {}
    for week in range(start_week, end_week+1):
        day = week * 7 - 2  # Friday
        days[day] = check_day(item_data, seed, day, item_list)
        day = week * 7  # Sunday
        days[day] = check_day(item_data, seed, day, item_list)
    return days

def satisfy_bundle(day_dict, bundle_list, bundle_count=None):
    if bundle_count == None:
        bundle_count = len(bundle_list)
    bundle_dict = {item: False for item in bundle_list}
    for d in day_dict.keys():
        for b in bundle_list:
            if not bundle_dict[b]:
                if b in day_dict[d]:
                    bundle_dict[b] = True
        if sum(bundle_dict.values()) == bundle_count:
            return True
    return sum(bundle_dict.values()) == bundle_count

def satisfy_all_bundles(day_dict, bundles):
    for bundle in bundles:
        if not satisfy_bundle(day_dict, bundle[0], bundle[1]):
            return (False, bundle[0])
    return (True,)

def min_set_cover(universe, day_dict):
    days = list(day_dict.keys())
    covered = set()
    cover = []
    while covered != universe:
        day = max(days, key=lambda d: len(set(day_dict[d].keys()) - covered))
        cover.append(day)
        covered |= set(day_dict[day].keys())
    return cover

def purchase_plan(universe, day_dict, cover):
    plan = {day: [] for day in cover}
    for item in universe:
        days = [day for day in cover if item in day_dict[day]]
        min_day = min(days, key=lambda d: day_dict[d][item]/d)
        plan[min_day].append(item)
    return plan

def is_seed_valid(item_data, gid, item_list, bundles):
    day_dict = scan_seed(item_data, gid, item_list)
    bundle_check = satisfy_all_bundles(day_dict, bundles)
    if bundle_check[0]:
        # identify minimum set cover over days
        universe = set(chain(*[day_dict[d].keys() for d in day_dict.keys()]))
        cover = sorted(min_set_cover(universe, day_dict))
        plan = purchase_plan(universe, day_dict, cover)
        print('Seed {}: # of Items: {} # of Trips: {}'.format(gid, len(universe), len(plan)))
        return (True, gid, plan)
    else:
        return (False, gid, bundle_check[1])

if __name__ == '__main__':
    with open('data/items.json', 'r') as f:
        item_data = json.load(f)
    
    bundles = [
               [['L. Goat Milk', 'Large Milk', 'Large EggW', 'Large EggB', 'Duck Egg', 'Wool'], 5], # Animal
               [['Cloth', 'Goat Cheese', 'Cheese'], 2], # Artisan
               [['Fiddlehead Fern', 'Truffle', 'Maki Roll', 'Fried Egg'], None], # Chef
               [['Sea Urchin', 'Duck Feather'], None], # Dye
               [['Rabbit\'s Foot', 'Pomegranate'], None], # Enchanter
               [['Catfish', 'Shad', 'Tiger Trout'], None], # River
               [['Largemouth Bass', 'Carp', 'Bullhead', 'Sturgeon'], None], # Lake
               [['Sardine', 'Tuna', 'Red Snapper', 'Tilapia'], None], # Ocean
               [['Walleye', 'Bream', 'Eel'], None], # Night
               [['Lobster', 'Crayfish', 'Shrimp', 'Snail', 'Periwinkle'], 2], #Crab pot
               [['Pufferfish', 'Ghostfish', 'Sandfish', 'Woodskip'], None], # Special Fish
               [['Chub'], None] # Field Research
              ]

    item_list = list(chain(*[b[0] for b in bundles]))

    if False:
        block_size = 500
        for block in range(100, 10000):
            start_time = time.time()
            b_start = block_size*block
            b_end = block_size*(block+1)
        
            seed_list = Parallel(n_jobs=4)(delayed(is_seed_valid)(item_data, gid, item_list, bundles) for gid in range(b_start, b_end))
            pruned_seed_list = list(filter(lambda s: s[0], seed_list))
            if pruned_seed_list:
                print(pruned_seed_list)
            end_time = time.time()
            print('\t\tFinished Block {0} in {1:.3g} seconds'.format(block, end_time-start_time))
    else:
        start_time = time.time()
        for gid in range(1,500):
            seed_tuple = is_seed_valid(item_data, gid, item_list, bundles)
            if seed_tuple[0]:
                print('Seed {}: # of Trips: {}'.format(gid, len(seed_tuple[2])))
        end_time = time.time()
        print('Time: ',end_time-start_time)

