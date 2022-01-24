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

## DO NOT CHANGE THIS CONFIGURATION
ENCODE_RANGE = 16
KEY_SIZE = 32

## MECHANIC ASSIST PARAMS
VERIFY_HASH = "5da1cd00651"

## DB CONFIG
DB_NAME = 'randtrix_db'
DB_FILE = DB_NAME + '.' + 'sqlite'
TABLE_NAME = 'randtrix_profile_manage'

# MISC CONFIG
SEPARATOR_KEY = '_rand_encode_sep_'
SAFE_IMPUTER_CHR = '.'
BINARY_RANDOM_SEED = '100000'

# DB ALERT MSG
DB_MSG = {
    'aex': 'profile_id: {profile_id} - Already exists'
}