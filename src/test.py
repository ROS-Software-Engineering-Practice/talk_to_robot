#!/usr/bin/env python
from flask import Flask
import time
from flask import render_template
from flask import request
import base64
from io import StringIO, BytesIO
import numpy as np
import rospy
from std_msgs.msg import String

app = Flask(__name__)
rospy.init_node('talker', anonymous=True)

@app.route('/')
def simpleRos():
	return render_template('index.html')

@app.route('/upload', methods = ['POST', 'GET'])
def upload():
    print('getting message from the web')
    if request.method == 'POST':
        message = request.form['parameter']

    print(message)
    pub = rospy.Publisher('message', String, queue_size=10)
    #rospy.init_node('talker', anonymous=True)
    if not rospy.is_shutdown():    
        pub.publish(message)
    return "successful"


if __name__ == '__main__':
    #app.run(host='0.0.0.0', port=7777, ssl_context='adhoc')
    app.run(debug = True)
