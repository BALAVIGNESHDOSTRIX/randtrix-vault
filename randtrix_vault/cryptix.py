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

import base64, pyaes
from typing import *
from .exceptions import *
from .config import *

class AES16256Codec:
    def __init__(self, data: str, key: str, encrypted_data: str=" ", encode: bool=True) -> None:
        if (str(data).endswith('.') and encode) or (str(data).startswith('.') and encode):
            raise AESEncryptionException("Please do not enter the '.' endswith or '.' startswith passwords")
        if '_rand_encode_sep_' in data and not encode:
            data = ''.join(str(data).split('_rand_encode_sep_'))
        self.data = []
        self.key = key[:KEY_SIZE]
        self.fernet = pyaes.AES(self.key.encode('utf-8'))
        self.encrypted_data = encrypted_data

        temp_data = [ord(c) for c in data]
        if not encode:
            self.data = [temp_data[i:i + ENCODE_RANGE] for i in range(0, len(temp_data), ENCODE_RANGE)]

        if encode:
            if len(temp_data) < ENCODE_RANGE:
                self.data.append(AES16256Codec.safe_imputer(temp_data))
            else:
                for k in [temp_data[i:i + ENCODE_RANGE] for i in range(0, len(temp_data), ENCODE_RANGE)]:
                    if len(k) == ENCODE_RANGE:
                        self.data.append(k)
                    else:
                        self.data.append(AES16256Codec.safe_imputer(k))

    @staticmethod
    def safe_imputer(list_d: List) -> List:
        initial_size = len(list_d)
        while initial_size < ENCODE_RANGE:
            list_d.append(ord('.'))
            initial_size += 1
        return list_d

    def encrypt(self) -> str:
        encrypted_string = ""
        enc_lst = [self.fernet.encrypt(data_seq) for data_seq in self.data]
        size_of_enc_string = len(enc_lst) - 1
        for index, enc_code_l in enumerate(enc_lst):
            for enc_code in enc_code_l:
                encrypted_string += chr(enc_code)
            if index != size_of_enc_string:
                encrypted_string += '_rand_encode_sep_'
        return encrypted_string

    def decrypt(self) -> str:
        decrypted_string = ""
        dec_lst = [self.fernet.decrypt(data_seq) for data_seq in self.data]
        for index, dec_code_l in enumerate(dec_lst):
            for a_index, dec_code in enumerate(dec_code_l):
                decrypted_string += chr(dec_code)
        decrypted_string = decrypted_string[::-1]
        while True:
            if decrypted_string.startswith('.'):
                decrypted_string = decrypted_string[1:]
            else:
                break
        return decrypted_string[::-1]