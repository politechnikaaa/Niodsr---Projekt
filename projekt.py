#!/usr/bin/env python3
import rclpy # Python Client Library for ROS 2
from rclpy.node import Node # Handles the creation of nodes
import cv2 # Python OpenCV library
import numpy as np
from geometry_msgs.msg import Twist

class MinimalPublisher(Node):
    def __init__(self):
        super().__init__('minimal_publisher')
        self.publisher_ = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)
        self.point = None
        self.window_name = "Black"
        timer_period = 0.5  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)

    def timer_callback(self):
        black_screen = np.zeros((500, 500, 3), dtype=np.uint8)
        cv2.imshow(self.window_name, black_screen)
        cv2.waitKey(25)
        cv2.setMouseCallback(self.window_name, self.draw_rectangle)
        
        if self.point != None:
        	if self.point[1] < 250:
		        twist_msg = Twist()
		        twist_msg.linear.x = 1.0
		        self.publisher_.publish(twist_msg)
       		else:
		        twist_msg = Twist()
		        twist_msg.linear.x = -1.0
		        self.publisher_.publish(twist_msg)

    def draw_rectangle(self, event, x, y, flags, param):
        if event == cv2.EVENT_LBUTTONDOWN:
            self.point = (x, y)



def main(args=None):
    rclpy.init(args=args)
    minimal_publisher = MinimalPublisher()
    rclpy.spin(minimal_publisher)
    minimal_publisher.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
