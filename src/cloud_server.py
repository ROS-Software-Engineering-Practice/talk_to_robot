#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from geometry_msgs.msg import Twist


def callback(data):
     rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)
     message = data.data
     speed = Twist()
     if message == '1':
          speed.linear.x = 1
          speed.angular.z = 0.001

     if message == '2':
          speed.linear.x = -1
          speed.angular.z = 0.001

     if message == '3':
          speed.linear.x = 0.001
          speed.angular.z = 1

     if message == '4':
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
