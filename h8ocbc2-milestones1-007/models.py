from config import db, ma
from marshmallow import fields

class Director(db.Model):
    __tablename__ = 'directors'
    name = db.Column(db.Text, nullable=False)
    id = db.Column(db.Integer, primary_key=True)
    gender = db.Column(db.Integer, nullable=False)
    uid = db.Column(db.Integer, nullable=False)
    department = db.Column(db.Text, nullable=False)
    movies = db.relationship(
        'Movie',
        backref='directors',
        cascade='all, delete, delete-orphan',
        single_parent=True,
        order_by='desc(Movie.release_date)'
    )

class Movie(db.Model):
    __tablename__ = 'movies'
    id = db.Column(db.Integer, primary_key=True)
    original_title = db.Column(db.Text, nullable=False)
    budget = db.Column(db.Integer, nullable=False)
    popularity = db.Column(db.Integer, nullable=False)
    release_date = db.Column(db.Text, nullable=False)
    revenue = db.Column(db.Integer, nullable=False)
    title = db.Column(db.Text, nullable=False)
    vote_average = db.Column(db.Float, nullable=False)
    vote_count = db.Column(db.Integer, nullable=False)
    overview = db.Column(db.Text, nullable=False)
    tagline = db.Column(db.Text, nullable=False)
    uid = db.Column(db.Integer, nullable=False)
    director_id = db.Column(db.Integer,db.ForeignKey('directors.id'))
    
class DirectorSchema(ma.SQLAlchemyAutoSchema):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    class Meta:
        model = Director
        sqla_session = db.session
        load_instance = True #from

    movies = fields.Nested('DirectorMovieSchema', default=[], many=True)

class DirectorMovieSchema(ma.SQLAlchemyAutoSchema):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    id = fields.Int()
    original_title = fields.Str()
    budget = fields.Int()
    popularity = fields.Int()
    release_date = fields.Str()
    revenue = fields.Int()
    title = fields.Str()
    vote_average = fields.Float()
    vote_count = fields.Int()
    overview = fields.Str()
    tagline = fields.Str()  
    uid = fields.Int()
    director_id = fields.Int()


class MovieSchema(ma.SQLAlchemyAutoSchema):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    class Meta:
        model = Movie
        sqla_session = db.session
        load_instance = True #from

    directors = fields.Nested("MovieDirectorSchema", default=None)


class MovieDirectorSchema(ma.SQLAlchemyAutoSchema):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    name = fields.Str()
    id = fields.Int()
    gender = fields.Int()
    uid = fields.Int()
    department = fields.Str()


class TopDirectorSchema(ma.SQLAlchemyAutoSchema):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    class Meta:
        model = Director
        sqla_session = db.session
        load_instance = True #from

    total_movies = fields.Int()
    