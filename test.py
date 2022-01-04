# from randtrix_mechanic import *
# from randtrix_db import *

# hash_l = RandtrixPasswordMechanic(456790,"test123","test234","test567").pass_2_hash()
# hash_l = RandtrixPasswordMechanic(456790,"test123","test234","test567").randomize()
# hash_l = RandtrixPasswordMechanic(456790,"test123","test234","test567").hash_2_salt()
# hash_l_k = RandtrixPasswordMechanic(456709, "test123", "test234", "test567").encrypt_pass("Hello World")
# print(hash_l_k)
#
# hash_l = RandtrixPasswordMechanic(638590, "test123", "test234", "test567").decrypt_pass(hash_l_k)
# print(hash_l)
#
# hash_l = RandtrixPasswordMechanic(189463, "test123", "test234", "test567").decrypt_pass(hash_l_k)
# print(hash_l)


# s = RandrixDBManager.create_rtrix("bala", "123", "test")
# print(s)

from randtrix_vault.cryptix import *

s = AES16256Codec('mercidus?wqertyum', 'bbdefa2950f49882f295b1285d4fa9dec45fc4144bfb07ee6acc68762d12c2e3').encrypt()
print(s)
# print(''.join([chr(i) for i in s]))