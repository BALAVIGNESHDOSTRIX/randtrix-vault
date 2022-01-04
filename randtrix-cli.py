import argparse, cmd2
from colorama import init, Fore, Back, Style
from randtrix_vault.assembler import *


init(autoreset=True)

banner = """
################################################################
#                     THE RANDTRIX VAULT                        #
# RANDOM MECHANISM WITH AES-256 ENCRYPTION FOR PASSWORD PROTECT #
#                                                               #
# DEVELOPER NAME: BALAVIGNESH M                                 #
# LICENSE: MIT                                                  #
# VERSION: 0.1.0                                                #
#################################################################
"""

class RandtrixCLI(cmd2.Cmd):
    def __init__(self):
        super().__init__(multiline_commands=['orate'])
        self.hidden_commands += [
            'alias', 'edit', 'history', 'macro', 'py', 'run_pyscript', 'run_script', 'set', 'shell', 'shortcuts'
        ]
        self.intro = Style.BRIGHT + Fore.GREEN + banner + '\x00'
        self.prompt = 'randtrix-cli>'

    def randtrix(self, args):
        if args.command == 'create_rtrix':
            vals = {
                'seed': args.six_d_seed,
                'first_pass': args.first_secret,
                'second_pass': args.second_secret,
                'third_pass': args.third_secret,
                'profile_pass': args.profile_pass,
                'profile_id': args.profile_id,
                'tags': args.tags
            }
            record_id = RandtrixAssembler.create_new_profile_entry(vals)
            print(record_id)
        if args.command == 'get_rtrix':
            vals = {
                'profile_id': args.profile_id,
                'six_d_seed': args.six_d_seed,
                'first_secret': args.first_secret,
                'second_secret': args.second_secret,
                'third_secret': args.third_secret,
            }
            data = RandtrixAssembler.get_profile_pass(vals)
            print(data)

    randtrix_parser = argparse.ArgumentParser(prog="randtrix",
                                              description="",
                                              conflict_handler='resolve',
                                              formatter_class=argparse.RawTextHelpFormatter,
                                              usage="randtrix [-h]"
                                              )

    subparsers = randtrix_parser.add_subparsers(dest='command', title="Options")
    subparser = subparsers.add_parser('create_rtrix', help='Create Password Entry')
    subparser.add_argument('profile_id', help='Profile ID', default=None)
    subparser.add_argument('profile_pass', help='Profile Password', default=None)
    subparser.add_argument('six_d_seed', help='6 Digit Integer Seed Value', default=None)
    subparser.add_argument('first_secret', help='First Secret', default=None)
    subparser.add_argument('second_secret', help='Second Secret', default=None)
    subparser.add_argument('third_secret', help='Third Secret', default=None)
    subparser.add_argument('tags', help='Tags', default=None)

    subparser = subparsers.add_parser('get_rtrix', help='Get Password Entry')
    subparser.add_argument('profile_id', help='Profile ID', default=None)
    subparser.add_argument('six_d_seed', help='6 Digit Integer Seed Value', default=None)
    subparser.add_argument('first_secret', help='First Secret', default=None)
    subparser.add_argument('second_secret', help='Second Secret', default=None)
    subparser.add_argument('third_secret', help='Third Secret', default=None)

    randtrix_parser.set_defaults(func=randtrix)

    @cmd2.with_argparser(randtrix_parser)
    def do_randtrix(self, args):
        func = getattr(args, "func", None)
        if func is not None:
            func(self, args)

cli = RandtrixCLI()
cli.debug = True
cli.cmdloop()