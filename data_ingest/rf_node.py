
import rclpy, numpy as np
from rclpy.node import Node
from custom_msgs.msg import IqFrame   # crie msg contendo float32[] iq
import bladerf

class RFNode(Node):
    def __init__(self):
        super().__init__('rf_node')
        self.pub = self.create_publisher(IqFrame, '/sdr/iq', 10)
        self.dev = bladerf.Device()
        self.dev.set_frequency(bladerf.RX, 0, 2.4e9)  # 2.4 GHz
        self.dev.set_sample_rate(bladerf.RX, 0, 10e6)
        self.dev.enable_module(bladerf.RX, 0, True)
        self.timer = self.create_timer(0.03, self.grab)

    def grab(self):
        iq = self.dev.receive(10_000)  # 1 ms @10 MSps
        msg = IqFrame()
        msg.samples = iq.astype(np.float32).tobytes()
        self.pub.publish(msg)
