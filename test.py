# from mechanic import *
# from db import *

# hash_l = AES16256Codec(456790,"test123","test234","test567").pass_2_hash()
# hash_l = AES16256Codec(456790,"test123","test234","test567").randomize()
# hash_l = AES16256Codec(456790,"test123","test234","test567").hash_2_salt()
# hash_l_k = AES16256Codec(456709, "test123", "test234", "test567").encrypt_pass("Hello World")
# print(hash_l_k)
#
# hash_l = AES16256Codec(638590, "test123", "test234", "test567").decrypt_pass(hash_l_k)
# print(hash_l)
#
# hash_l = AES16256Codec(189463, "test123", "test234", "test567").decrypt_pass(hash_l_k)
# print(hash_l)


# s = RandrixDBManager.create_rtrix("bala", "123", "test")
# print(s)

from randtrix_vault.cryptix import *
message = 'mercidus?wqertkumddddddddddddddddddddddd'
key = 'bbdefa2950f49882f295b1285d4fa9dec45fc4144bfb07ee6acc68762d12c2e'
s = AES16256Codec(message, key).encrypt()
decryped_message = AES16256Codec(s, key , encode=False).decrypt()
assert message == decryped_message