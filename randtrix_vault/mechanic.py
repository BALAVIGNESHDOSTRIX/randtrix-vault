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
from hashlib import sha256
import random
from .cryptix import AES16256Codec
from .exceptions import *
from .tools import *


class RandtrixPasswordMechanic:
    """ Randtrix Password Mechanic """
    def __init__(self, seed_value: int = 0, frst_pass: str = "", sec_pass: str = "", thd_pass: str = "") -> None:
        self.seed_value = str(seed_value)
        self.passwrd_lst = [frst_pass, sec_pass, thd_pass]

        if not len(self.seed_value) == 6:
            raise RandtrixException("Please Enter 6 digit Integer seed value")

    def pass_2_hash(self) -> List:
        return [sha256(x.encode('utf8')).hexdigest() for x in self.passwrd_lst]

    def randomize(self) -> List[int]:
        rand_int_l = []
        for index, pas in enumerate(self.passwrd_lst):
            inx_combinator = RandtrixTools.index_manipulate(index)
            random.seed(int(self.seed_value[inx_combinator[0]]) + int(self.seed_value[inx_combinator[1]]))
            rand_int_l.append(random.randint(index, int('100000', 2)))
        return rand_int_l

    def hash_2_salt(self) -> Any:
        pass_hash = ""
        rand_int_l = self.randomize()
        for index, hash in enumerate(self.pass_2_hash()):
            pass_hash += hash[index:rand_int_l[index]]
        return sha256(pass_hash.encode('utf-8')).hexdigest()

    def encrypt_pass(self, password: str) -> str:
        return AES16256Codec(password, self.hash_2_salt()).encrypt()

    def decrypt_pass(self, data: str) -> str:
        return AES16256Codec(data, self.hash_2_salt()).decrypt()