TOKEN = 'Enter your token here'

from bot import commands as cmd
from bot import tic_tac_toe as tictac

cmdinputs=['!hello',
           '!help',
           '!tic_tac_toe']

cmdactions=[cmd.hello_cmd,
            cmd.help_cmd,
            tictac.tic_tac_toe_game]
