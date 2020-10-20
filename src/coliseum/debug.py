# in addition to being able to run the game in debug mode, this script also provides
# a debug() decorator that can be used to audit the output of each function

import time, colorama, os, random, sys
from colorama import Fore, Back, Style 
from player import Player


# I created a wrapper function -- called a decorator -- to this script so 
# we can add it to various parts of player.py to debug portions
def debug(func):
    import functools
    
    # print the function signature and return value
    @functools.wraps(func)
    def wrapper_debug(*args, **kwargs):
        args_repr = [repr(a) for a in args]                      # 1
        kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]  # 2
        signature = ", ".join(args_repr + kwargs_repr)           # 3
        print(f"Calling {func.__name__}({signature})")
        value = func(*args, **kwargs)
        print(f"{func.__name__!r} returned {value!r}")           # 4
        return value
    return wrapper_debug

def main():

    player = Player()

    # overwrite the starting values with player inputs

    player.lvl = int(input('Input your desired level. \n>'))
    player.str = int(input('Input your desired strength. \n>'))
    player.con = int(input('Input your desired constitution. \n>'))
    player.spd = int(input('Input your desired speed. \n>'))
    player.weapon = int(input('Input your desired weapon value. \n>'))
    player.armor = int(input('Input your desired armor value. \n>'))
    player.shield = int(input('Input your desired shield level. \n>'))
    player.hp = 10*(player.lvl+player.con)
    
    while player.is_alive == True:
        player.input()
        
if __name__ == "__main__":
    main()