TOKEN = 'Put your token here'

GITHUB_LINK = 'https://github.com/Tetrastorm/Sakura.py'

BOT_LINK = 'https://discordapp.com/api/oauth2/authorize?client_id=593770116164878344&permissions=0&scope=bot'

GITHUB_MSG = 'To follow the project, report an issue or contributing => ' + GITHUB_LINK

LINK_MSG = 'To add Sakura.py on your discord server => ' + BOT_LINK

REALEASE_NOTE = ['```md\n',
               '# Release Note Sakura.py v.0.1.2 #\n\n',
               'Feature:\n',
               '- Add !release to display the last release note\n'
               '- Add !link to get the link for add the bot on another discord server\n',
               '\nBugs fix and improvements:\n',
               '- Improve help command\n',
               '- Update help command\n',
               '- Improve coordinate system in !tic_tac_toe\n',
               '- Add an indication of the action played by the bot in !tic_tac_toe\n',
               '\nUpdate from: 06/30/2019'
               '```']

HELP_MSG = ['```md\n',
              '# Commands:\n'
              '- !help\n',
              '- !hello\n',
              '\n# Game:\n',
              '- !tic_tac_toe\n',
              '\n# Other:\n',
              '- !release\n',
              '- !link\n',
              '- !github',
              '```']

CMD_INPUTS = ['!hello',
            '!help',
            '!tic_tac_toe',
            '!release',
            '!link',
            '!github'
            ]

from bot import commands as cmd
from bot import tic_tac_toe as tictac

CMD_ACTIONS = [cmd.hello_cmd,
            cmd.help_cmd,
            tictac.tic_tac_toe_game,
            cmd.release_cmd,
            cmd.link_cmd,
            cmd.github_cmd]
