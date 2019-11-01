# StardewScripts

Scripts to assist seed planning for Stardew Valley speedruns

- **CSRandom.py** is a direct recreate of the default C# random number generator implemented in python, allowing us to match exactly the game's RNG. Since the game reseeds constantly, most applications can use CSRandomLite, which takes advantage of constant reseeding to be able to directly calculate RNG values from the equation of a line instead of needing to properly seed an array and manipulate forward.
- **Utility.py** contains dumb codes to just convert raw days to Year/Season/Day format
- **ObjectInfo.py** contains a dict of item codes for all item objects (does not include tools/weapons)

Stardew Valley uses the time of game launch/"exit to title" as a seed for a large number of random events in-game. It computes this via (C#)
```
gameID = (ulong)(DateTime.UtcNow - new DateTime(2012, 6, 22)).TotalSeconds;
```

This means you can seed your game by changing the clock time and exiting to title from a current game in order to lock in a particular seed.

### Ancient Seed (new 10/31/19):
The seed maker selects a seed to return based on the hidden game seed, the tile the seed maker is on, the day, and the time of day when a crop is put in it. Using that, you can manipulate an ancient seed spawn coming from the seed maker by puting it on a specific tile/operating with it at specific times. This notebook allows you to walk through both an individual hour or a series of hour-by-hour snapshots of the seed maker layout.

### Mushroom Floor:
Each day the mushroom floor will spawn on a floor between 80-120. The floor it spawns on is entirely based on the initial seed and the current day number, so we can easily track when and where the floor will spawn. Note there are many days where the mushroom floor will not exist, either due to being spawned on a floor number that's divisible by 5 (80, 85, etc.) or other random catches.

### Trash Cans:
There are 7 trash cans scattered throughout Pelican Town, and their items are predetermined each day based again on that initial seed value. This code tracks the items that will spawn in each trashcan (indicated by the person's home) on a given day.

### Traveling Cart:
The traveling cart is one of the biggest RNG factors in the speedrun currently, as there are several items (Truffle, Rabbit's Foot, etc) that are extremely costly to gather in-game regularly and have relatively low odds (<2%) of being sold at the cart. Again the cart items and costs are predetermined by the game seed, allowing us to project the items that will be sold in future months or to search for the first instance of a particular item being sold at the cart.

