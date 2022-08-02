# Games calculators
## Description
These scripts can be used to make computations in certains games.

## Installing 
Run : 

`pip install -r requirements.txt`

## Summary
[Merge Dragons](#merge-dragons-md-id)

## Merge Dragons {#md-id}
The script for the game *Merge Dragons* only compute the required number of items of level `start_level` to merge in
order to have an item of level `target_level`.

There is two modes : 
* Optimized : Simulation with merges of 5 objects (bonus item taken into account)
* Unoptimized : Simulation with merges of 3 objects

### Run
**Complete command line :**

``python merge_dragons.py --start_level <start_level> --target_level <target_level> --unoptimized <bool value>``

- `start_level` (int): level of items used as base item for merges (default = 0)
- `target_level` (int): level of item wanted
- `unoptimized` (bool): optimized mode (default = False)

**Example :**

``python merge_dragons.py --target_level 4``