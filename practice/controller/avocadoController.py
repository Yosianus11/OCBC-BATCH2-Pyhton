
from flask import make_response, abort
from config import db
from models.avocado import Avocado, AvocadoSchema


def read_all():
    # Create the list of people from our data
    avocados = Avocado.query.all()

    # Serialize the data for the response
    Avotype_schema = AvocadoSchema(many=True)
    return Avotype_schema.dump(avocados)



def read_one(totalvol):
    # Get the person requested
    avocados = Avocado.query.filter(Avocado.totalvol == totalvol)

    # Did we find a person?
    if avocados is not None:

        # Serialize the data for the response
        Avocado_schema = AvocadoSchema()
        return Avocado_schema.dump(avocados)

    # Otherwise, nope, didn't find that person
    else:
        abort(
            404,
            "Person not found for Id: {totalvol}".format(totalvol=totalvol),
        )

def create(avocado):
    # Create a person instance using the schema and the passed in person
    schema = AvocadoSchema()
    new_avocado = schema.load(avocado, session=db.session)

    # Add the person to the database
    db.session.add(new_avocado)
    db.session.commit()

    # Serialize and return the newly created person in the response
    data = schema.dump(new_avocado)

    return data, 201