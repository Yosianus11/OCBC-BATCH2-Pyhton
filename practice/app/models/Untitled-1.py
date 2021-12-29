

# class Avoregion(db.Model):
#     __tablename__ = 'avoregion'
#     regionid = db.Column(db.Integer, primary_key=True)
#     region = db.Column(db.Text)
    
#     avocados = db.relationship(
#         'Avocado',
#         backref='avoregion',
#         cascade='all, delete, delete-orphan',
#         single_parent=True,
#         order_by='desc(Avocado.avgprice)'
#     )
    
#     def __repr__(self):
#         return '<avoregion {}>'.format(self.name)
    

        
# class Avotype(db.Model):
#     __tablename__ = 'avoregion'
#     typeid = db.Column(db.Integer, primary_key=True)
#     type = db.Column(db.Text)
    
#     avocados = db.relationship(
#         'Avocado',
#         backref='avoregion',
#         cascade='all, delete, delete-orphan',
#         single_parent=True,
#         order_by='desc(Avocado.avgprice)'
#     )


# class AvoregionSchema(ma.SQLAlchemyAutoSchema):
#     class Meta:
#         model = Avoregion
#         # sqla_session = db.session
#         load_instance = True #from
        
# class AvotypeSchema(ma.SQLAlchemyAutoSchema):
#     class Meta:
#         model = Avotype
#         # sqla_session = db.session
#         load_instance = True #from