from flask import Flask, request
import flask
import werkzeug
import random
import os
import time

# Initialize the Flask application
app = Flask(__name__)

# route http posts to this method
@app.route('/api/test', methods=['POST'])
def test():
    imagefile = request.files['image']
    filename = werkzeug.utils.secure_filename(imagefile.filename)
    filename_to_save = str(time.time()) + filename
    imagefile.save(filename_to_save)
    time.sleep(2)

    """
    ML Stuff use image name `imagefile` and return the result map as shown below:
    "0" -> Rock
    "1" -> Paper
    "2" -> Scissor 
    """

    os.remove(filename_to_save)
    return str(random.randint(0,2))

# start flask app
app.run(host="0.0.0.0", port=5000)
