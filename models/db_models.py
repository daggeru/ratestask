from webapp.app import db

db.Model.metadata.reflect(db.engine)


class Ports(db.Model):
    __table__ = db.Model.metadata.tables['ports']


class Prices(db.Model):
    __table__ = db.Model.metadata.tables['prices']


class Regions(db.Model):
    __table__ = db.Model.metadata.tables['regions']
