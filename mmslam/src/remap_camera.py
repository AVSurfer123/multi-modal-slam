#!/usr/bin/env python3

import rospy
from sensor_msgs.msg import CompressedImage, CameraInfo

class Remap:

    def __init__(self):
        self.image_pub = rospy.Publisher('/camera/image/compressed', CompressedImage, queue_size=5)
        self.info_pub = rospy.Publisher('/camera/camera_info', CameraInfo, queue_size=5)
        self.image_sub = rospy.Subscriber('/raspicam_node/image/compressed', CompressedImage, self.image_cb)
        self.info_sub = rospy.Subscriber('/raspicam_node/camera_info', CameraInfo, self.info_cb)
        
    def image_cb(self, msg):
        self.image_pub.publish(msg)

    def info_cb(self, msg):
        self.info_pub.publish(msg)

def main():
    rospy.init_node('remap_camera')
    remap = Remap()
    rospy.spin()

if __name__ == '__main__':
    main()
