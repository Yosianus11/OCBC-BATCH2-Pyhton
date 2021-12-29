"""
This is the people module and supports all the REST actions for the
director data
"""

from flask import make_response, abort
from config import db
from sqlalchemy.sql import func
from models import Director, DirectorSchema, Movie,TopDirectorSchema




def read_all(order_by, sort):
    """
    This function responds to a request for /api/director
    with one matching person from people

    :param order_by:   order by and sort
    :return:           all data of director
    """
    # Create the list of people from our data
    if sort[0] == "desc":
        director = Director.query.order_by(db.desc(order_by[0])).limit(10)
    else :
        director = Director.query.order_by(db.asc(order_by[0])).limit(10)

    # Serialize the data for the response
    director_schema = DirectorSchema(many=True)
    data = director_schema.dump(director)
    return data


def highest_dir():
    """
    This function responds to a request for /api/director

    :return:           get most productive director
    """
    director = db.session.query(Director.id,
                                Director.name,
                                Director.department,
                                Director.uid,
                                Director.gender,
                                func.count('*').label('total_movies')
                                ).join(Movie, 
                                       Director.id == Movie.director_id
                                ).group_by(Movie.director_id
                                ).order_by(db.desc(func.count(Movie.director_id))).limit(5)

    director_schema = TopDirectorSchema(many=True, )
    data = director_schema.dump(director)
    return data

def read_one(id):
    """
    This function responds to a request for /api/director/{id}
    with one matching  diector

    :param id:  id of director
    :return:    data of id director
    """
    # Build the initial query
    director = (
        Director.query.filter(Director.id == id)
        .outerjoin(Movie)
        .one_or_none()
    )

    # Did we find a person?
    if director is not None:

        # Serialize the data for the response
        director_schema = DirectorSchema()
        data = director_schema.dump(director)
        return data

    # Otherwise, nope, didn't find that person
    else:
        abort(404, f"Director not found for Id: {id}")


def read_byname(name):
    """ Search Director name acoording to name
    
    Keyword arguments:
    argument -- input param {name}
    Return: data of director with name inputed
    """
    
    # Build the initial query
    director = (
        Director.query.filter(Director.name == name)
        .outerjoin(Movie)
        .one_or_none()
    )

    # Did we find a director?
    if director is not None:

        # Serialize the data for the response
        director_schema = DirectorSchema()
        data = director_schema.dump(director)
        return data

    # Otherwise, nope, didn't find that director
    else:
        abort(404, f"Director not found for name: {name}")

def create(director):
    """
    This function responds to a request for /api/director/
    creating new director

    :return:    data of id director inputed
    """
    
    name = director.get("name")

    existing_director = (
        Director.query.filter(Director.name == name)
        .one_or_none()
    )

    # Can we insert this person?
    if existing_director is None:

        # Create a person instance using the schema and the passed in person
        schema = DirectorSchema(only=['id','name','department','uid','gender'])
        new_director = schema.load(director, session=db.session)

        # Add the person to the database
        db.session.add(new_director)
        db.session.commit()

        # Serialize and return the newly created person in the response
        data = schema.dump(new_director)

        return data, 201

    # Otherwise, nope, person exists already
    else:
        abort(409, f"Director {name} exists already")

def update(id, director):
    """
    This function responds to a request for /api/director/{id}
    update data director

    :param id:  id of director
    :return:    data of id director
    """
    # Get the person requested from the db into session
    update_director = Director.query.filter(
        Director.id == id
    ).one_or_none()

    # Did we find an existing person?
    if update_director is not None:

        # turn the passed in person into a db object
        schema = DirectorSchema(only=['id','name','department','uid','gender'])
        update = schema.load(director, session=db.session)

        # Set the id to the person we want to update
        update.id = update_director.id

        # merge the new object into the old and commit it to the db
        db.session.merge(update)
        db.session.commit()

        # return updated person in the response
        data = schema.dump(update_director)

        return data, 200

    # Otherwise, nope, didn't find that person
    else:
        abort(404, f"Director not found for Id: {id}")


def delete(id):
    """
    This function responds to a request for /api/director/{id}
    deleteting director by id

    :param id:  id of director
    :return:    inform deleting success
    """

    # Get the person requested
    director = Director.query.filter(Director.id == id).one_or_none()

    # Did we find a person?
    if director is not None:
        db.session.delete(director)
        db.session.commit()
        return make_response(f"Director {id} deleted", 200)

    # Otherwise, nope, didn't find that person
    else:
        abort(404, f"Director not found for Id: {id}")

