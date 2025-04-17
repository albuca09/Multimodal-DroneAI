
import rclpy, sounddevice as sd
from rclpy.node import Node
from audio_common_msgs.msg import AudioData
import numpy as np

class AudioNode(Node):
    def __init__(self):
        super().__init__('audio_node')
        self.pub = self.create_publisher(AudioData, '/mic/audio', 10)
        self.stream = sd.InputStream(channels=1, samplerate=48000, callback=self.audio_cb)
        self.stream.start()

    def audio_cb(self, indata, frames, time, status):
        msg = AudioData()
        msg.data = indata.astype(np.int16).tobytes()
        self.pub.publish(msg)
