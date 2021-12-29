from flask import make_response, abort
from config import db
from app.models.avocado import Avocado, AvocadoSchema


def read_all():

    # Create the list of people from our data
    avocado = Avocado.query.all()

    # Serialize the data for the response
    avocado_schema = AvocadoSchema(many=True)
    data = avocado_schema.dump(avocado)
    return avocado_schema.dump(avocado)


