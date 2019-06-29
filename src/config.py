TOKEN = 'Entrer your token here'

GITHUB_LINK='https://github.com/Tetrastorm/Sakura.py'

cmdinputs=['!hello',
           '!help',
           '!tic_tac_toe',
           '!github']

from bot import commands as cmd
from bot import tic_tac_toe as tictac

cmdactions=[cmd.hello_cmd,
            cmd.help_cmd,
            tictac.tic_tac_toe_game,
            cmd.github_cmd]
