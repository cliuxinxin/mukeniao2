from orator import Model
from orator.orm import belongs_to_many,has_many,belongs_to

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
    
    @belongs_to_many
    def trains(self):
        return Train


class Train(Model):
   __fillable__ = ['name']

   @belongs_to_many
   def trans(self):
       return Tran

   @has_many
   def results(self):
       return Result

class Result(Model):
    __fillable__ = ['key','value'] 

    @belongs_to
    def trains(self):
        return Train

