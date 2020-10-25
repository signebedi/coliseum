"""player.py: primary source file for coliseum, a simple, turn-based command line game in python"""

import time, colorama, os, random, pickle, sys
from colorama import Fore, Back, Style 

class Player:
    def __init__(self):
        
        colorama.init(autoreset=True)
        
        header = [  '   _____ ____  _      _____  _____ ______ _    _ __  __ ',
                    '  / ____/ __ \| |    |_   _|/ ____|  ____| |  | |  \/  |',
                    ' | |   | |  | | |      | | | (___ | |__  | |  | | \  / |',
                    ' | |   | |  | | |      | |  \___ \|  __| | |  | | |\/| |',
                    ' | |___| |__| | |____ _| |_ ____) | |____| |__| | |  | |',
                    '  \_____\____/|______|_____|_____/|______|\____/|_|  |_|',
                ]
        
        for item in header: print(item)
    
        print('\nWelcome to the Coliseum. Earn ducats in the Work Room, buy equipment in the Shop, and battle for glory in the Arena!')

        self.lvl = 1
        self.xp = 0
        self.str = 1
        self.spd = 1
        self.con = 1
        self.weapon = 1
        self.armor = 1
        self.shield = 1
        self.potions = 0
        self.is_alive = True
        self.hp = 10*(self.lvl+self.con)
        self.gold = 5
        self.kills = 0
        self.victories = []
        
        if os.path.exists("save.pickle"):
            load_game = input('\nDo you want to load a save file? (yes, no; defaults to no)\n')
            if load_game == 'yes': self.load()
            else: self.name = input('\nWhat is your character\'s name?\n> ')
        else: self.name = input('\nWhat is your character\'s name?\n> ')
        
    def input(self):
        i = input('\nWhat would you like to do next? (type "help" for options)\n> ')

        if i == 'help': print('\nOPTIONS:\nwork\nstats\nstore\nbattle\ntournament\nsave\nload\n')
        elif i == 'work': self.work()
        elif i == 'stats': self.stats()
        elif i == 'store': self.store()
        elif i == 'save': self.save()
        elif i == 'load': self.load()
        elif i == 'dev-load-tournament': self.dev_load_tournament()
        elif i == 'battle': self.battle(enemy = self.enemy_generator())
        elif i == 'die': self.dead() # this is a debug command to test that the Player.dead() function works
        elif i == 'hurt': 
            self.hp -= 3
            print('\noh no, you hurt yourself!\n')
            if self.hp <= 0: self.dead() 
        elif i == 'tournament' : self.tournament()
        else: print('\nInvalid Command\n')

    def store(self):
        print('\nYou walk into the coliseum armory to prepare for battle\n')
        while True:
            i = input('What would you like to buy? (type "help" for options)\n> ')
            if i == "help": print(f'\nOPTIONS:\nstr - cost: {self.str}\ncon - cost: {self.con}\nspd - cost: {self.spd}\nweapon - cost: {self.weapon}\nshield - cost: {self.shield}\narmor - cost: {self.armor}\npotion - cost: 10\nstats\nleave\n')
            elif i == "str": self.str = self.increase_stat('str')
            elif i == "con": self.con = self.increase_stat('con'); self.hp = 10*(self.lvl+self.con)
            elif i == "spd": self.spd = self.increase_stat('spd')
            elif i == "weapon": self.weapon = self.increase_stat('weapon')
            elif i == "shield": self.shield = self.increase_stat('shield')
            elif i == "armor": self.armor = self.increase_stat('armor')
            elif i == "potion": 
                if self.gold >= 10: 
                    self.potions += 1
                    self.gold -= 10
                    print('\nYou purchased a potion\n')
                else: print('\nInsufficient gold -- you need 10 gold to purchase a potion\n')
            elif i == "stats": self.stats()
            elif i == "leave": print('\nyou left the armory\n'); break
            else: print('\nUnknown command! Please try again\n')


    def tournament(self, tournaments=None):
        if not tournaments:
            from coliseum.tournaments import tournaments
        cmd = input(f'\nWhich tournament do you want to fight in? (options: {", ".join([t["name"] for t in tournaments])}) \n> ')
        
        for t in tournaments:
            if cmd in t["name"]:
                print(f'\nYou have opted to fight in the {cmd} and your enemies are {", ".join([e["name"] for e in t["enemies"]])}\n')

                player_lost_tournament = False
                
                for enemy in t["enemies"]:
                    if self.battle(enemy, battle_type='tournament'): # assess the truth value of each battle and...
                        player_lost_tournament = True # if returns true, break this loop and set player_lost_tournament to True
                        break

                if player_lost_tournament: # only give the reward if the player actually wins the tournament
                    print(f'\nYou lost the {cmd}\n')
                else:    
                    self.gold += t["gold"]
                    t["won"] = True
                    self.victories.append(t['name'])
                    print(f'\nYou won the {t["name"]} and earned {t["gold"]} ducats!\n')
            # else: print('\nInvalid tournament\n')

    def enemy_generator(self):

        # here we import the list of enemies from enemies.py and we
        # develop a random enemy for a given battle

        from coliseum.enemies import enemy_list
        
        enemy_selector = random.choice(enemy_list)

        enemy = {}

        enemy['name'] = enemy_selector['name']
        enemy['difficulty'] = enemy_selector['difficulty']
        
        enemy['hp'] = (self.lvl + enemy['difficulty']) * 10
        #enemy['hp'] = self.lvl*random.randint(1, (self.lvl*enemy['difficulty'])) + 10
        enemy['atk'] = random.randint(1, (self.lvl*enemy['difficulty'])) + 2
        enemy['def'] = random.randint(1, (self.lvl*enemy['difficulty']))
        enemy['spd'] = random.randint(1, (self.spd*enemy['difficulty']))
        enemy['gold'] = random.randint(1, (self.lvl*enemy['difficulty'])) + 10


        return enemy        

    def battle(self, enemy, battle_type=None):
        
        if battle_type == 'tournament':
            enemy['mode'] = 'spar'
            print(f'\nYou entered the arena for a tournament battle with {enemy["name"]}\n')

        else:
            cmd = input('\nDo you want to wager on a friendly spar, or a battle to the death? (options: spar, death; defaults to spar)\n> ')
        
            if cmd == 'death': enemy['mode'] = 'death'; enemy['gold'] += enemy['gold']
            else: enemy['mode'] = 'spar'
        
            print(f'\nYou entered the arena for a one-on-one battle with a(n) {enemy["name"]}, with a wager of {enemy["gold"]} ducats\n')
        
        while True:
            
            cmd = input(f'\nYour hp is {self.hp}. The {enemy["name"]}\'s health is {enemy["hp"]} in a {enemy["mode"]} match. what would you like to do? (type "help" for options)\n> ')
            
            if cmd == 'atk' or cmd == 'a': 
                player_dmg = self.lvl*random.randint(1, (self.str+self.weapon)) - enemy['def']
                
                try: assert player_dmg > 0
                except: player_dmg = 0

                enemy['hp'] -= player_dmg
                print(f'\nyou attacked the {enemy["name"]} and dealt {player_dmg} damage.\n')
            
                if enemy["hp"] <= 0: 
                    print(f'\nYou defeated the {enemy["name"]} and gained an experience point and {enemy["gold"]} ducats!\n')
                    self.xp += 1
                    self.gold+=enemy['gold']
                    self.kills+=1
    
                    if self.xp == self.lvl: self.level_up()
                    
                    break
            
                if self.dodge_check(enemy['spd']) > 50: 
                    print(f'\nYour speed allowed you to dodge the {enemy["name"]}\'s attack\n')
                    
                else:
                
                    enemy_dmg = self.lvl*random.randint(1, enemy['atk']) - (self.armor+self.shield) + 2
                    
                    # don't let enemy cause negative damage
                    try: assert enemy_dmg > 0
                    except: enemy_dmg = 0
                    
                    self.hp -= enemy_dmg
                    
                    print(f'\nThe {enemy["name"]} attacked you and dealt {enemy_dmg} damage.\n')
                
                # if this is a spar
                if self.hp <= 0: 
                    if battle_type == 'tournament':
                        self.hp = 1
                        print(f'\nThe {enemy["name"]} defeated you\n')
                        return True # if this returns true, then break the underlying loop in tournament mode to prevent payoff

                    if enemy['mode'] == 'spar':
                        self.hp = 1
                        self.gold -= enemy['gold']
                        print(f'\nThe {enemy["name"]} defeated you, and you lost {enemy["gold"]} ducats\n')
                        break
                    else:
                        self.dead()
                        break
    
            elif cmd == 'stats': self.stats()
            
            elif cmd == 'help': print('\nOPTIONS:\natk\nstats\nrun\n')
            
            elif cmd == 'potion': 
                if self.potions > 0:
                    self.potions -= 1
                    self.hp = 10*(self.lvl+self.con)
                    print('\nYou used a potion and regained full health\n')
                else: print ('\nInsufficient potions\n')
    
            elif cmd == 'run':
              
                if battle_type == 'tournament':  
                    print ('\nsorry, but you can\'t run away from a tournament!\n')
                    
                else:
                    print(f'\nYou ran away from the {enemy["name"]} and lost {enemy["gold"]} ducats\n')
                    self.gold -= enemy["gold"]
                    break

    def dodge_check(self, enemy_spd):
        # do a speed check to see if you dodge an enemy attack
        check = (self.spd - enemy_spd + random.randint(-5,5)) * 100
        return check

    def level_up(self):
        self.lvl += 1
        self.hp = 10*(self.lvl+self.con)
        self.xp = 0
        
        print(f'\nCongrats! You made it to level {self.lvl}!\n')
        self.stats()
        
    def work(self):
        while(True):
            worktime = round(time.time())+5
            num = round(time.time())
            while(round(time.time()) <= worktime):
                if round(time.time()) == num: pass
                else: print(round(worktime) - round(time.time())); time.sleep(1)
            self.gold += 5
            i = input('\nYou worked for five seconds and earned 5 ducats. Do you want to continue? y/n\n> ')
            if i == 'y':pass
            else: break
    def stats(self):
        if self.hp <= .25*(10*(self.lvl+self.con)): hp_color =  Fore.RED
        elif self.hp >= .75*(10*(self.lvl+self.con)): hp_color = Fore.GREEN 
        else: hp_color = Fore.YELLOW
        print('\u2500'*80)
        print(f'name: ' + Fore.CYAN + Style.BRIGHT + f'{self.name}' + Style.RESET_ALL + f'\n\nhp: '+ hp_color + Style.BRIGHT + f'{self.hp}' + Style.RESET_ALL + f' \nxp: {self.xp}\nlvl: {self.lvl}\n\nstr: {self.str}\nspd: {self.spd}\ncon: {self.con}\ngold: {self.gold}\nkills: {self.kills}\nTrophies: {self.victories} \n\nweapon: {self.weapon}\nshield: {self.shield}\narmor: {self.armor}\npotions: {self.potions}')
        print('\u2500'*80)
        
    def increase_stat(self, cmd):
        
        if cmd == 'str': stat = self.str
        elif cmd == 'spd': stat = self.spd
        elif cmd == 'con': stat = self.con
        elif cmd == 'weapon': stat = self.weapon
        elif cmd == 'armor': stat = self.armor
        elif cmd == 'shield': stat = self.shield
        
        if self.gold >= stat:
            self.gold -= stat
            stat += 1
            print(f'\nYou leveled up your {cmd} to {stat}\n')
            return stat
            
        else:
            print(f'\nInsufficient gold -- you need {stat} gold to level your {cmd} skill up\n')
            return stat

    def save(self):
        with open('save.pickle', 'wb') as f:
            pickle.dump(vars(self), f)

        print('\nSave successful!\n')


    def dead(self):
        print(f'\nOh dear, {self.name}... it looks like you have been defeated, consigned to the mists of history. Better luck next time.\n')
        self.end_text = [
            ' ________         ____        __  __',
            '/_  __/ /  ___   / __/__  ___/ / / /',
            ' / / / _ \/ -_) / _// _ \/ _  / /_/ ',
            '/_/ /_//_/\__/ /___/_//_/\_,_/ (_)  \n\n',
        ]
        for item in self.end_text: print(item)
        self.is_alive = False

    def load(self):
        try: 
            loaded_file = pickle.load(open("save.pickle", "rb"))
            
            self.lvl = loaded_file['lvl']
            self.xp = loaded_file['xp']
            self.str = loaded_file['str']
            self.spd = loaded_file['spd']
            self.con = loaded_file['con']
            self.weapon = loaded_file['weapon']
            self.armor = loaded_file['armor']
            self.shield = loaded_file['shield']
            self.potions = loaded_file['potions']
            self.is_alive = loaded_file['is_alive']
            self.hp = loaded_file['hp']
            self.gold = loaded_file['gold']
            self.kills = loaded_file['kills']
            self.victories = loaded_file['victories']
            self.name = loaded_file['name']
            
            print(f'\nSuccessfully loaded your last save file! {loaded_file}\n')
        except: print('\nNo save file found...\n')

    def dev_load_tournament(self):
        try: 
            filepath = os.path.join(os.getcwd(), 'tournament.py')
            sys.path.insert(0, filepath)
            from tournaments import tournaments
            for tournament in tournaments:
                assert isinstance(tournament['name'], str)
                assert isinstance(tournament['type'], str)
                assert tournament['type'] in ['beginner','intermediate','advanced']
                assert isinstance(tournament['enemies'], list)
                assert isinstance(tournament['gold'], int)
                assert tournament['won'] == False
                for enemy in tournament['enemies']:
                    assert isinstance(enemy['name'], str)
                    assert isinstance(enemy['hp'], int)
                    assert isinstance(enemy['atk'], int)
                    assert isinstance(enemy['def'], int)
                    assert isinstance(enemy['spd'], int)
                    assert isinstance(enemy['gold'], int)

            self.tournament(tournaments)

        except Exception as e:
            print(f'\nsorry, could not find a file named tournament.py in the current working directory. See our docs for instructions on adding your own tournaments. {e}\n')