import requests as fetch
from server import app, request, jsonify, upload, cloudinary_url, cloudinary
from config.config import *

@app.route('/files', methods=['GET'])
def GetAllFiles():
    fileslist = cloudinary.api.resources()['resources']
    return jsonify(fileslist)

@app.route('/faces', methods=['POST'])
def DetectionAPI():

    file = request.files['file']

    if file:
        res = upload(file)

    body = {
        'url': res['secure_url']
    }

    response = fetch.post(AZURE_FACE_API_URL, params=AZURE_API_PARAMS,
                          headers=AZURE_API_HEADERS, json=body)

    faces = response.json()

    return jsonify(faces)
