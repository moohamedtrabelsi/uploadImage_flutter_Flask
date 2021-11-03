from flask import Flask, render_template, request,flash, redirect, url_for
from http.server import HTTPServer, BaseHTTPRequestHandler 
from werkzeug.utils import secure_filename
from http import HTTPStatus 
import os
from flask_cors import CORS
import db as d

app = Flask(__name__)
CORS(app)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

APP_ROOT = os.path.dirname(os.path.abspath(__file__))

@app.route("/")
def helloWorld():
  return "Hello, M-Vision!"


@app.route('/api/upload', methods=['POST'])
def face_upload():
    target = os.path.join(APP_ROOT, 'images/') 
    if not os.path.isdir(target):
            os.mkdir(target)    
    face_db_table = d.mongo.db.images  
    if request.method == 'POST':
        for upload in request.files.getlist("file"): 
            filename = secure_filename(upload.filename)
            destination = "/".join([target, filename])
            upload.save(destination)
            face_db_table.insert({'file': filename})   

        return 'Image Upload Successfully'



if __name__ == '__main__':
    app.run(port=5001)
