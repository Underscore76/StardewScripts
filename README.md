# StardewScripts

Scripts to assist seed planning for Stardew Valley speedruns

- **CSRandom.py** is a direct recreate of the default C# random number generator implemented in python, allowing us to match exactly the game's RNG.
- **Utility.py** contains dumb codes to just convert raw days to Year/Season/Day format
- **ObjectInfo.py** contains a dict of item codes for all item objects (does not include tools/weapons)

Stardew Valley uses the time of file creation as a seed for a large number of random events in-game. By setting your computer's clock to a time and tracking it closely, you could attempt to select a specific seed at startup.

### Mushroom Floor:
Each day the mushroom floor will spawn on a floor between 80-120. The floor it spawns on is entirely based on the initial seed and the current day number, so we can easily track when and where the floor will spawn. Note there are many days where the mushroom floor will not exist, either due to being spawned on a floor number that's divisible by 5 (80, 85, etc.) or other random catches.

### Trash Cans:
There are 7 trash cans scattered throughout Pelican Town, and their items are predetermined each day based again on that initial seed value. This code tracks the items that will spawn in each trashcan (indicated by the person's home) on a given day.

### Traveling Cart:
The traveling cart is one of the biggest RNG factors in the speedrun currently, as there are several items (Truffle, Rabbit's Foot, etc) that are extremely costly to gather in-game regularly and have relatively low odds (<2%) of being sold at the cart. Again the cart items and costs are predetermined by the game seed, allowing us to project the items that will be sold in future months or to search for the first instance of a particular item being sold at the cart.

