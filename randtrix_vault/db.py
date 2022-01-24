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

from .orm import Model, Database
from .config import *
from typing import *
import os

class RandtrixModel(Model): pass


class RandtrixDB(RandtrixModel):
    _tb_name = TABLE_NAME

    profile_id = str
    profile_pass = str
    tags = str
    verify_hash = str

    def __init__(self, kwargs: Any = None) -> None:
        if kwargs is None:
            kwargs = {}
        self.profile_id = kwargs.get('profile_id')
        self.profile_pass = kwargs.get('profile_pass')
        self.tags = kwargs.get('tags')
        self.verify_hash = kwargs.get('verify_hash')


class RandtrixDBManager:

    @staticmethod
    def initialize_db() -> Any:
        return Database(DB_FILE)

    @staticmethod
    def create(kwargs: Any = None) -> Any:
        if kwargs is None:
            kwargs = {}
        RandtrixDB.db = RandtrixDBManager.initialize_db()
        trix = RandtrixDB(kwargs).save()
        trix.db.commit()
        return trix.id

    @staticmethod
    def get_by_profile_id(kwargs: Any = None) -> List:
        if kwargs is None:
            kwargs = {}
        RandtrixDB.db = RandtrixDBManager.initialize_db()
        x = RandtrixDB.db.execute(
            'SELECT * FROM {table_name} WHERE profile_id LIKE "{pro_id}" limit 1'.format(pro_id=kwargs.get('profile_id'), table_name=TABLE_NAME))
        return [dict(row) for row in x.fetchall()]

    @staticmethod
    def get_by_verify_hash(kwargs: Any = None) -> List:
        if kwargs is None:
            kwargs = {}
        RandtrixDB.db = RandtrixDBManager.initialize_db()
        x = RandtrixDB.db.execute(
            'SELECT verify_hash FROM {table_name} WHERE id = "{pro_id}"'.format(pro_id=kwargs.get('id'), table_name=TABLE_NAME))
        return [dict(row) for row in x.fetchall()]

    @staticmethod
    def get_all_profile_ids(kwargs: Any = None) -> List:
        if kwargs is None:
            kwargs = {}
        RandtrixDB.db = RandtrixDBManager.initialize_db()
        profile_id_query = 'SELECT profile_id FROM {table_name}'.format(table_name=TABLE_NAME)
        if kwargs.get('tags'):
            profile_id_query += ' WHERE tags LIKE "{tags}"'.format(tags=kwargs.get('tags'))
        profile_id_query += ' ORDER BY ID ASC'
        x = RandtrixDB.db.execute(profile_id_query)
        return [dict(row) for row in x.fetchall()]

    @staticmethod
    def generate_database_file():
        if not os.path.exists(DB_FILE):
            db = RandtrixDBManager.initialize_db()
            RandtrixDB.manager(db, RandtrixDB)
            db.connection.commit()
            db.close()
        return True
