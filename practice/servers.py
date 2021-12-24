# 3rd party moudles
from flask import render_template

# local modules
import config


# Get the application instance
connex_app = config.connex_app

app = connex_app.app

# Read the swagger.yml file to configure the endpoints
connex_app.add_api("swagger.yml")


# create a URL route in our application for "/"

if __name__ == "__main__":
    connex_app.run(host='localhost', port=5300, debug=True)