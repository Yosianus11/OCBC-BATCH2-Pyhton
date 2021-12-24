from datetime import datetime
from config import db, ma

class Avocado(db.Model):
    __tablename__ = 'avocado'
    date = db.Column(db.Text)
    avgprice = db.Column(db.Float)
    totalvol = db.Column(db.Integer, primary_key=True)
    avo_a = db.Column(db.Integer)
    avo_b = db.Column(db.Float)
    avo_c = db.Column(db.Float)
    type = db.Column(db.Integer)
    regionid = db.Column(db.Integer)

class Avoregion(db.Model):
    __tablename__ = 'avoregion'
    regionid = db.Column(db.Integer, primary_key=True)
    region = db.Column(db.Text)
    
class Avotype(db.Model):
    __tablename__ = 'avotype'
    typeid = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.Text)

class AvocadoSchema(ma.SQLAlchemyAutoSchema):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
    class Meta:
        model = Avocado
        # sqla_session = db.session
        load_instance = True #from
        
class AvoregionSchema(ma.SQLAlchemyAutoSchema):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
    class Meta:
        model = Avoregion
        # sqla_session = db.session
        load_instance = True #from
        
class AvotypeSchema(ma.SQLAlchemyAutoSchema):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
    class Meta:
        model = Avotype
        # sqla_session = db.session
        load_instance = True #from
