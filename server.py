from flask import Flask, request, jsonify
from flask_restful import Api
from flask_cors import CORS

import cloudinary
from cloudinary.uploader import upload
from cloudinary.utils import cloudinary_url

from config.config import *

app = Flask(__name__)
api = Api(app)

cloudinary.config(
    cloud_name = CLOUDINARY_CLOUD_NAME,
    api_key = CLOUDINARY_API_KEY,
    api_secret = CLOUDINARY_API_SECRET
)

from controllers.calls import *

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=False, port=3000)
