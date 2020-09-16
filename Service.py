from flask import Flask, request
import time
import sys
import base64

sys.path.insert(1, '/ImageHandler/')
from yolo_opencv import objectDetect

# Create instance of class containing object detection methods
image = objectDetect()

app = Flask(__name__)


@app.route('/')
def hello_world():
    return "<h1>hello world iseek.</h1>"


@app.route('/time')
def send_time():
    print('hello world')
    return {'time': time.time()}


@app.route('/image', methods=['POST', 'GET'])
def receivePic():
   print('endpoint reachde')
   if request.method == 'POST':
       print("hello world")
       data = request.json
       pic_as_base64 = data['pictureString']

       with open("imageToDetect.png",'wb') as fh:
           fh.write(base64.b64decode(pic_as_base64))


       imagePath = "./imageToDetect.png"

       return {
           "pictureResponse": image.processImage(imagePath)
       }
   if request.method == 'GET':
       return "<h1>Hello world iSeek</h1>"
