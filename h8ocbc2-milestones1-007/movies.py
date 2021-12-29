from flask import make_response, abort
from config import db
from models import Director, Movie, MovieSchema


def read_all(order_by, sort, limit):
    """
    This function responds to a request for /api/movies
    with movie data associated with director_id and filter sort & order

    :param director id  & movie id:  id of director
    :return:    show 1 data of movie table
    """
    
    if sort[0] == "desc" :
        # Query the database for all the notes
        movies = Movie.query.order_by(db.desc(order_by[0])).limit(limit)
    else :
        movies = Movie.query.order_by(db.asc(order_by[0])).limit(limit)

    # Serialize the list of notes from our data
    movie_schema = MovieSchema(many=True)
    data = movie_schema.dump(movies)
    return data


def read_one(directors_id, movie_id):
    """
    This function responds to a request for /api/director/{director_id}/movie/{movie_id}
    with movie data associated with director_id

    :param director id  & movie id:  id of director
    :return:    show 1 data of movie table
    """
    # Query the database for the note
    movie = (
        Movie.query.join(Director, Director.id == Movie.director_id)
        .filter(Director.id == directors_id)
        .filter(Movie.id == movie_id)
        .one_or_none()
    )

    # Was a note found?
    if movie is not None:
        note_schema = MovieSchema()
        data = note_schema.dump(movie)
        return data

    # Otherwise, nope, didn't find that note
    else:
        abort(404, f"Movie not found for Id: {movie_id}")


def create(director_id, movie):
    """
    This function responds to a request for /api/director/{director_id}/movie/{movie_id}
    created movie data associated with director_id

    :param director id  & movie id:  id of director
    :return:    data create success full
    """

    # get the parent person
    director = Director.query.filter(Director.id == director_id).one_or_none()

    # Was a person found?
    if director is None:
        abort(404, f"Person not found for Id: {director_id}")

    # Create a note schema instance
    schema = MovieSchema()
    new_movie = schema.load(movie, session=db.session)

    # Add the note to the person and database
    director.movies.append(new_movie)
    db.session.commit()

    # Serialize and return the newly created note in the response
    data = schema.dump(new_movie)

    return data, 201


def update(directors_id, movie_id, movie):
    """
    This function responds to a request for /api/director/{director_id}/movie/{movie_id}
    Updating data  movie associated with movie_id

    :param director id  & movie id:  id of director
    :return:    data update success full
    """

    update_movie = (
        Movie.query.filter(Director.id == directors_id)
        .filter(Movie.id == movie_id)
        .one_or_none()
    )

    # Did we find an existing note?
    if update_movie is not None:

        # turn the passed in note into a db object
        schema = MovieSchema()
        update = schema.load(movie, session=db.session)

        # Set the id's to the note we want to update
        update.id = update_movie.id
        update.id = update_movie.id

        # merge the new object into the old and commit it to the db
        db.session.merge(update)
        db.session.commit()

        # return updated note in the response
        data = schema.dump(update_movie)

        return data, 200

    # Otherwise, nope, didn't find that note
    else:
        abort(404, f"Note not found for Id: {movie_id}")


def delete(directors_id, movie_id):
    """
    This function responds to a request for /api/director/{director_id}/movie/{movie_id}
    deleteting director by id

    :param director id  & movie id:  id of director
    :return:    inform deleting success
    """

    # Get the note requested
    movie = (
        Movie.query.filter(Director.id == directors_id)
        .filter(Movie.id == movie_id)
        .one_or_none()
    )

    # did we find a note?
    if movie is not None:
        db.session.delete(movie)
        db.session.commit()
        return make_response(
            "Movie {movie_id} deleted".format(movie_id=movie_id), 200
        )

    # Otherwise, nope, didn't find that note
    else:
        abort(404, f"Movie not found for Id: {movie_id}")


