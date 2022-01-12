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
from hashlib import sha256
from .config import *

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
            if data and isinstance(data, str):
                if data != "null":
                    print("Profile ID:",  Style.BRIGHT + Fore.CYAN + profile_id + '\x00')
                    print("Profile pass:", Style.BRIGHT + Fore.YELLOW + data + '\x00')
                else:
                    print(Style.BRIGHT + Fore.RED + "Incorrect Password Combination entered...." + '\x00')
            elif not data:
                print("Profile ID:",  Style.BRIGHT + Fore.CYAN + profile_id + " not found" + '\x00')



    @staticmethod
    def generate_verify_hash(data):
        data = VERIFY_HASH + data
        return sha256(data.encode('utf-8')).hexdigest()