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

class RandtrixTools:
    """ Randtrix Tools """
    @staticmethod
    def index_manipulate(index:int=0) -> Dict:
        return {0: [index, index+1], 1: [index+1, index+2], 2: [index+2, index+3]}.get(index)