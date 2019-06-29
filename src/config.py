TOKEN = 'NTkzNzcwMTE2MTY0ODc4MzQ0.XRTqgw.h_MnKTO2YMBvFyp4t6E3KFn-uhc'

from bot import commands as cmd
from bot import tic_tac_toe as tictac

cmdinputs=['!hello',
           '!help',
           '!tic_tac_toe']

cmdactions=[cmd.hello_cmd,
            cmd.help_cmd,
            tictac.tic_tac_toe_game]
