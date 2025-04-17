
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import CompressedImage
import cv2

class CameraNode(Node):
    def __init__(self):
        super().__init__('camera_node')
        self.pub = self.create_publisher(CompressedImage, '/cam/compressed', 10)
        self.cap = cv2.VideoCapture(0)
        self.timer = self.create_timer(1/30, self.grab)

    def grab(self):
        ret, frame = self.cap.read()
        if not ret:
            self.get_logger().warning('Camera frame drop')
            return
        msg = CompressedImage()
        msg.format = 'jpeg'
        msg.data = cv2.imencode('.jpg', frame)[1].tobytes()
        self.pub.publish(msg)

def main():
    rclpy.init()
    CameraNode()
    rclpy.spin()
