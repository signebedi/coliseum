# Gameplay
---

## Installation

To install this over Pip, run the following command:

```pip install coliseum```

To start the game, run the following command:

```python -m coliseum```


## Starting a New Game

You start the game at level 1, but will face a number of choices to increase your character's level at little cost. You can type the ```help``` command to see available commands. 

## Coliseum Battles and Tournaments

You can battle individual, randomized enemies in the arena by running the ```battle``` command. You can also choose to fight in a tournament by running the ```tournament``` command, which will allow you to select from pre-determined set of tournaments. You can also load your own tournaments into the game by running the command ```dev-load-tournament```, but note that this will search for a file named tournaments.py in your current working directory, the contents of which should follow the following structure:

```python
tournaments = [
    {
        'name': 'TOURNAMENT_NAME_HERE', # naming convention: capitalized, no special characters, eg. Tutorial Cup
        'type': 'beginner|intermediate|advanced', # simply for administrative purposes, record the difficulty level
        'enemies': [ # this element should store a list of enemy dictionaries
            {'name':'NAME', 'hp': INT, 'atk': INT, 'def': INT, 'spd': INT, 'gold': INT},
            {'name':'NAME', 'hp': INT, 'atk': INT, 'def': INT, 'spd': INT, 'gold': INT},
            {'name':'NAME', 'hp': INT, 'atk': INT, 'def': INT, 'spd': INT, 'gold': INT},
        ],
        'gold': INT,
        'won': False, # this determines at runtime whether a character has beaten this tournament before
    },
    ... ADDITIONAL TOURNAMENTS CAN BE ADDED HERE ...
}
```

## Saving and Loading Games

Coliseum will save to, and load from, a pickle file if you run the command ```save``` or ```load```. It will only search the current working directory for your save file--so make sure to run the game in the directory with your save file. It only supports a single save.pickle file, meaning that subsequent saves will overwrite past saves.

## Visiting the General Store

To level up your skills and equipment, visit the store by running the ```store``` command. Once you have entered the store, you can purchase upgrades. The cost of these upgrades is equal to the level of your skill and/or equipment. For example, if you have a level 7 constitution, then it will cost you 7 ducats to upgrade to level 8.

## Working to Earn Gold

You can work to earn additional ducats using the ```work``` command. You earn one ducat for each second you work. You can work for up to 5 seconds at a time until you need to renew your contract, which is intended to prevent exploits of this system.