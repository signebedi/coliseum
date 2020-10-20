"""tournaments.py: a set of tournaments the player can fight in coliseum, a simple, turn-based command line game in python"""

tournaments = [
    {
        'name': 'Tutorial Cup',
        'type': 'beginner',
        'enemies': [
            {'name':'Glardon the Greek', 'hp': 1, 'atk': 1, 'def': 1, 'spd': 1, 'gold': 0},
            {'name':'Filibert the Frank', 'hp': 17, 'atk': 3, 'def': 3, 'spd': 5, 'gold': 0},
            {'name':'Estek the Mamluk', 'hp': 28, 'atk': 5, 'def': 5, 'spd': 2, 'gold': 0},
        ],
        'gold': 10,
        'won': False,
    },
    {
        'name': 'Historical Cup',
        'type': 'beginner',
        'enemies': [
            {'name':'Titus Livius', 'hp': 25, 'atk': 3, 'def': 3, 'spd': 3, 'gold': 0},
            {'name':'Thucydides', 'hp': 35, 'atk': 4, 'def': 4, 'spd': 5, 'gold': 0},
            {'name':'Plutarch', 'hp': 40, 'atk': 5, 'def': 5, 'spd': 4, 'gold': 0},
            {'name':'Aulus Hirtius', 'hp': 55, 'atk': 7, 'def': 6, 'spd': 6, 'gold': 0},
        ],
        'gold': 50,
        'won': False,
     },
    
    {
        'name': 'Mathematical Cup',
        'type': 'beginner',
        'enemies': [
            {'name':'Thales', 'hp': 28, 'atk': 3, 'def': 4, 'spd': 4, 'gold': 0},
            {'name':'Pythagoras', 'hp': 36, 'atk': 3, 'def': 5, 'spd': 5, 'gold': 0},
            {'name':'Euclid', 'hp': 42, 'atk': 4, 'def': 6, 'spd': 5, 'gold': 0},
            {'name':'Archimedes of Syracuse', 'hp': 58, 'atk': 7, 'def': 7, 'spd': 7, 'gold': 0},
        ],
        'gold': 50,
        'won': False,
     },
    
    {
         'name': 'Dramatist Cup',
         'type': 'beginner',
         'enemies': [
             {'name':'Aeschylus', 'hp': 23, 'atk': 4, 'def': 3, 'spd': 4, 'gold': 0},
             {'name':'Euripides', 'hp': 33, 'atk': 5, 'def': 4, 'spd': 5, 'gold': 0},
             {'name':'Aristophanes', 'hp': 38, 'atk': 5, 'def': 5, 'spd': 4, 'gold': 0},
             {'name':'Sophocles', 'hp': 55, 'atk': 8, 'def': 5, 'spd': 7, 'gold': 0},
         ],
         'gold': 50,
         'won': False,
     },
    
    {
         'name': 'Hellenic Cup',
         'type': 'intermediate',
         'enemies': [
             {'name':'Pyrrhus of Epirus', 'hp': 65, 'atk': 7, 'def': 8, 'spd': 8, 'gold': 0},
             {'name':'Cleopatra', 'hp': 80, 'atk': 8, 'def': 8, 'spd': 8, 'gold': 0},
             {'name':'Hannibal Barca', 'hp': 100, 'atk': 12, 'def': 12, 'spd': 14, 'gold': 0},
             {'name':'Mithridates VI of Pontus', 'hp': 150, 'atk': 15, 'def': 15, 'spd': 15, 'gold': 0},        
         ],
         'gold': 75,
         'won': False,
     }, 

    {'name': 'Barbarian Cup',
         'type': 'intermediate',
         'enemies': [
             {'name':'Jugurtha', 'hp': 85, 'atk': 8, 'def': 6, 'spd': 8, 'gold': 0},
             {'name':'Cassivellaunus', 'hp': 100, 'atk': 9, 'def': 7, 'spd': 8, 'gold': 0},
             {'name':'Vercingetorix', 'hp': 140, 'atk': 11, 'def': 8, 'spd': 12, 'gold': 0},
             {'name':'Arminius', 'hp': 175, 'atk': 17, 'def': 14, 'spd': 16, 'gold': 0},        
         ],
         'gold': 75,
         'won': False,
    },

    {'name': 'Hero Cup',
         'type': 'advanced',
         'enemies': [
             {'name':'Publius Decius Mus', 'hp': 200, 'atk': 20, 'def': 14, 'spd': 17, 'gold': 0},
             {'name':'Quintus Fabius Maximus', 'hp': 300, 'atk': 18, 'def': 25, 'spd': 20, 'gold': 0},
             {'name':'Publius Cornelius Scipio', 'hp': 250, 'atk': 25, 'def': 20, 'spd': 20, 'gold': 0},
             {'name':'Gnaeus Pompey Magnus', 'hp': 500, 'atk': 30, 'def': 30, 'spd': 30, 'gold': 0},        
             {'name':'Gaius Julius Caesar', 'hp': 1000, 'atk': 35, 'def': 25, 'spd': 100, 'gold': 0},        
         ],
         'gold': 100,     
         'won': False,
    },
]