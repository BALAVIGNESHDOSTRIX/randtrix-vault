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

from .orm import Manager, Model, Database

class RandtrixManager(Manager):

    def get_by_profile_id(self, profile_id=''):
        sql = 'SELECT * FROM {tb} WHERE profile_id LIKE %{pro_id}% = ?'.format(tb=self.table_name, pro_id=profile_id)
        result = self.db.execute(sql)
        row = result.fetchone()
        if not row:
            msg = 'Object%s with id does not exist: %s' % (self.model, id)
            raise ValueError(msg)
        return self.create(**row)

class RandtrixModel(Model): pass

class RandtrixDB(RandtrixModel):
    # __name__ = 'randtrix_table'

    profile_id = str
    profile_pass = str
    tags = str

    def __init__(self, kwargs={}):
        self.profile_id = kwargs.get('profile_id')
        self.profile_pass = kwargs.get('profile_pass')
        self.tags = kwargs.get('tags')


class RandtrixDBManager:

    @staticmethod
    def initialize_db():
        return Database('randtrix_db.sqlite')

    @staticmethod
    def create(kwargs={}):
        RandtrixDB.db = RandtrixDBManager.initialize_db()
        trix = RandtrixDB(kwargs).save()
        trix.db.commit()
        return trix.id

    @staticmethod
    def get_by_profile_id(kwargs):
        RandtrixDB.db = RandtrixDBManager.initialize_db()
        x = RandtrixDB.db.execute('SELECT * FROM RandtrixDB WHERE profile_id LIKE "{pro_id}"'.format(pro_id=kwargs.get('profile_id')))
        rows = []
        for row in x.fetchall():
            rows.append(dict(row))
        return rows
