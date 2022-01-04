import base64, pyaes
from typing import *

class AES16256Codec:
    def __init__(self, data:str, key:str) -> None:
        self.data = []
        self.key = key[:32]
        self.fernet = pyaes.AES(self.key.encode('utf-8'))
        temp_data = [ord(c) for c in data]

        if len(temp_data) < 16:
            self.data.append(AES16256Codec.safe_imputer(temp_data))
        else:
            initial_size = 16
            final_size = len(temp_data)
            k = []
            self.data.append(temp_data[:16])
            i = 1
            while i < 17 and initial_size <= final_size:
                k.append(temp_data[initial_size: initial_size + 1][0])
                initial_size += 1
                i += 1
                if i == 16 and len(k) == 16:
                    self.data.append(k)
                    k = []
                    i = 1
                else:
                    self.data.append(AES16256Codec.safe_imputer(k))
                    break

    @staticmethod
    def safe_imputer(list_d:List=[]) -> List:
        initial_size = len(list_d)
        while initial_size < 16:
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
                encrypted_string += '_encode_sep_'
        return encrypted_string

    def decrypt(self) -> str:
        return self.fernet.decrypt(self.data)