#!/usr/bin/env python3

import rospy
import cv2
from cv_bridge import CvBridge
from sensor_msgs.msg import CompressedImage, CameraInfo

class Remap:

    def __init__(self):
        self.image_pub = rospy.Publisher('/camera/image/compressed', CompressedImage, queue_size=5)
        self.info_pub = rospy.Publisher('/camera/camera_info', CameraInfo, queue_size=5)
        self.bridge = CvBridge()
        self.image_sub = rospy.Subscriber('/raspicam_node/image/compressed', CompressedImage, self.image_cb)
        self.info_sub = rospy.Subscriber('/raspicam_node/camera_info', CameraInfo, self.info_cb)

        
    def image_cb(self, msg):
        img = self.bridge.compressed_imgmsg_to_cv2(msg)
        rot = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
        img_msg = self.bridge.cv2_to_compressed_imgmsg(rot)
        self.image_pub.publish(img_msg)

    def info_cb(self, msg):
        self.info_pub.publish(msg)

def main():
    rospy.init_node('remap_camera')
    remap = Remap()
    rospy.spin()

if __name__ == '__main__':
    main()
