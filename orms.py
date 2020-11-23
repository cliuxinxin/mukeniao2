from orator import Model
from orator.orm import belongs_to_many

from config import db

Model.set_connection_resolver(db)

class Entry(Model):
    __fillable__ = ['location']

    @belongs_to_many
    def trans(self):
        return Tran

class Tran(Model):
    __fillable__ = ['name','type']

    @belongs_to_many
    def entries(self):
        return Entry
