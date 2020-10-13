import time, colorama, os, random
from colorama import Fore, Back, Style 
from player import Player

def main():

    player = Player()

    while player.is_alive == True:
        player.input()
        
if __name__ == "__main__":
    main()