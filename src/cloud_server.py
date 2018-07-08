#!/usr/bin/env python
#coding=utf-8
import rospy
from std_msgs.msg import String
from geometry_msgs.msg import Twist
import urllib2
import time
import urllib
import json
import hashlib
import base64

def callback(data):
     message = data.data
     
     for i in range(len(message)):
          if message[i] == ':':
               message = message[:i] + '_' + message[i+1:]

     rospy.loginfo(rospy.get_caller_id() + "I heard %s", message)
     time.sleep(1)
     f = open("/home/abc/Downloads/"+message, 'rb')
     file_content = f.read()
     base64_audio = base64.b64encode(file_content)
     body = urllib.urlencode({'audio': base64_audio})

     url = 'http://api.xfyun.cn/v1/service/v1/iat'
     api_key = '4596b3b86a5f15020d5b70475aacfa64'
     param = {"engine_type": "sms16k", "aue": "raw"}

     x_appid = '5b3f45de'
     x_param = base64.b64encode(json.dumps(param).replace(' ', ''))
     x_time = int(int(round(time.time() * 1000)) / 1000)
     x_checksum = hashlib.md5(api_key + str(x_time) + x_param).hexdigest()
     x_header = {'X-Appid': x_appid,
                 'X-CurTime': x_time,
                 'X-Param': x_param,
                 'X-CheckSum': x_checksum}
     req = urllib2.Request(url, body, x_header)
     result = urllib2.urlopen(req)
     result = result.read()

  
     print result
     choose = result.form['data']

     speed = Twist()
     if choose == '前进。':
          speed.linear.x = 1
          speed.angular.z = 0.001

     if choose == '后退。':
          speed.linear.x = -1
          speed.angular.z = 0.001

     if choose == '左转。':
          speed.linear.x = 0.001
          speed.angular.z = 1

     if choose == '右转。':
          speed.linear.x = 0.001
          speed.angular.z = -1

          

     pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
     pub.publish(speed)
     
     

def listener():

     # In ROS, nodes are uniquely named. If two nodes with the same
     # node are launched, the previous one is kicked off. The
     # anonymous=True flag means that rospy will choose a unique
     # name for our 'listener' node so that multiple listeners can
     # run simultaneously.
     rospy.init_node('cloud_server', anonymous=True)

     rospy.Subscriber("message", String, callback)

     # spin() simply keeps python from exiting until this node is stopped
     rospy.spin()

if __name__ == '__main__':
     listener()
