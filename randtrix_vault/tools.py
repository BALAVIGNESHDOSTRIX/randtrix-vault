"""
################################################################
#                     THE RANDTRIX VAULT                        #
# RANDOM MECHANISM WITH AES-256 ENCRYPTION FOR PASSWORD PROTECT #
#                                                               #
# DEVELOPER NAME: BALAVIGNESH M                                 #
# LICENSE: MIT                                                  #
# VERSION: 0.1.0                                                #
#################################################################
"""

from typing import *
from colorama import init, Fore, Back, Style

class RandtrixTools:
    """ Randtrix Tools """
    @staticmethod
    def index_manipulate(index:int=0) -> Dict:
        return {0: [index, index+1], 1: [index+1, index+2], 2: [index+2, index+3]}.get(index)

    @staticmethod
    def parse_string(profile_id: str="",data: str="", t: str='create'):
        if t == 'create':
            try:
                data = int(data)
            except:
                print("Profile not saved correctly")
            if isinstance(data, int):
                print("Profile Successfully saved.")
            else:
                print("Profile not saved correctly")

        if t == 'get':
            if isinstance(data, list):
                print("Profile ID:",  Style.BRIGHT + Fore.CYAN + profile_id + '\x00')
                print("Profile pass:", Style.BRIGHT + Fore.YELLOW + data[0] + '\x00')

