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

from .db import RandtrixDBManager
from .mechanic import *
from .tools import *
from .exceptions import *
from typing import *


class RandtrixAssembler:

    @staticmethod
    def create_new_profile_entry(kwargs: Any = None) -> int | str:
        if kwargs is None:
            kwargs = {}
        seed_value = 0
        data = RandtrixDBManager.get_by_profile_id(kwargs)
        if data:
            return DB_MSG.get('aex')
        MechanicObj = RandtrixPasswordMechanic(seed_value=kwargs.get('six_d_seed'),
                                               frst_pass=kwargs.get('first_secret'),
                                               sec_pass=kwargs.get('second_secret'),
                                               thd_pass=kwargs.get('third_secret'))
        encrypted_msg = MechanicObj.encrypt_pass(password=kwargs.get('profile_pass'))
        try:
            seed_value = sum([int(x) for x in kwargs.get('six_d_seed')])
        except Exception as e:
            raise RandtrixException("Please Enter the 6 - digit integer seed value")
        verify_hash_data = kwargs.get('first_secret') + kwargs.get('second_secret') + kwargs.get('third_secret') + str(
            seed_value)
        sha256_verify_hash = RandtrixTools.generate_verify_hash(verify_hash_data)
        entry_id = RandtrixDBManager.create({'profile_id': kwargs.get('profile_id'),
                                             'profile_pass': encrypted_msg,
                                             'verify_hash': sha256_verify_hash,
                                             'tags': kwargs.get('tags') or 'null'})
        return entry_id

    @staticmethod
    def get_profile_pass(kwargs: Any = None) -> str | None:
        seed_value = 0
        if kwargs is None:
            kwargs = {}
        data = RandtrixDBManager.get_by_profile_id(kwargs)
        if not data:
            return ""
        MechanicObj = RandtrixPasswordMechanic(seed_value=kwargs.get('six_d_seed'),
                                               frst_pass=kwargs.get('first_secret'),
                                               sec_pass=kwargs.get('second_secret'),
                                               thd_pass=kwargs.get('third_secret'))
        try:
            seed_value = sum([int(x) for x in kwargs.get('six_d_seed')])
        except Exception as e:
            raise RandtrixException("Please Enter the 6 - digit integer seed value")
        verify_hash_data = kwargs.get('first_secret') + kwargs.get('second_secret') + kwargs.get('third_secret') + str(
            seed_value)
        sha256_verify_hash = RandtrixTools.generate_verify_hash(verify_hash_data)
        if sha256_verify_hash == data[0].get('verify_hash'):
            return MechanicObj.decrypt_pass(data[0].get('profile_pass'))
        else:
            return "null"
