"""__main__.py: execution script for coliseum, a simple, turn-based command line game in python"""

import time, colorama, os, random, sys
from colorama import Fore, Back, Style 
from coliseum.player import Player
from coliseum._version import __version__
from coliseum._metadata import *

def main():

    player = Player()

    while player.is_alive == True:
        player.input()
        
if __name__ == "__main__":
    main()