from colorclass import Color
from colorclass import disable_all_colors, enable_all_colors, is_enabled
from time import localtime, strftime
from enum import IntEnum
from dnsvalidator.lib.core.__version__ import __version__


class OutputHelper(object):
    def __init__(self, arguments):
        if arguments.nocolor:
            disable_all_colors()

        self.verbose = arguments.verbose
        self.silent = arguments.silent
        self.seperator = "=============================================="

    def print_banner(self):
        if self.silent:
            return

        print(self.seperator)
        print("dnsvalidator v%s\tby James McLean (@vortexau) & Michael Skelton (@codingo_)" % __version__)
        print(self.seperator)

    def terminal(self, level, target, message=""):
        if level == 0 and not self.verbose:
            return

        formatting = {
            0: Color('{autoblue}[VERBOSE]{/autoblue}'),
            1: Color('{autoyellow}[INFO]{/autoyellow}'),
            2: Color('{autogreen}[ACCEPTED]{/autogreen}'),
            3: Color('{autored}[REJECTED]{/autored}'),
            4: Color('{autobgyellow}{autored}[ERROR]{/autored}{/autobgyellow}')
        }

        leader = formatting.get(level, '[#]')

        format_args = {
           'time': strftime("%H:%M:%S", localtime()),
           'target': target,
           'message': message,
            'leader':leader
        }

        if target == 0:
            template = '[{time}] {leader} {message}'
        else:
            template = '[{time}] {leader} [{target}] {message}'
            
        print(template.format(**format_args))


class Level(IntEnum):
    VERBOSE = 0
    INFO = 1
    ACCEPTED = 2
    REJECTED = 3
    ERROR = 4