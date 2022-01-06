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

class RandtrixAssembler:

    @staticmethod
    def create_new_profile_entry(kwargs={}):
        MechanicObj = RandtrixPasswordMechanic(seed_value=kwargs.get('seed'),
                                            frst_pass=kwargs.get('first_pass'),
                                            sec_pass=kwargs.get('second_pass'),
                                            thd_pass=kwargs.get('third_pass'))
        encrypted_msg = MechanicObj.encrypt_pass(password=kwargs.get('profile_pass'))
        entry_id = RandtrixDBManager.create({'profile_id': kwargs.get('profile_id'),
                                             'profile_pass': encrypted_msg,
                                             'tags': kwargs.get('tags')})
        return entry_id

    @staticmethod
    def get_profile_pass(kwargs={}):
        data = RandtrixDBManager.get_by_profile_id(kwargs)
        decrypted_l = []
        if data:
            for entry in data:
                MechanicObj = RandtrixPasswordMechanic(seed_value=kwargs.get('six_d_seed'),
                                                       frst_pass=kwargs.get('first_secret'),
                                                       sec_pass=kwargs.get('second_secret'),
                                                       thd_pass=kwargs.get('third_secret'))
                decrypt_pass = MechanicObj.decrypt_pass(entry.get('profile_pass'))
                decrypted_l.append(decrypt_pass)
        return decrypted_l