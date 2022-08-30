import rclpy
from rclpy.node import Node

from sensor_msgs.msg import Image


class ImageSubscriber(Node):

    def __init__(self):
        super().__init__('camera_subscriber_node')
        self.img_topic = "/camera/rgb/image_raw"
        self.subscription = self.create_subscription(Image, self.img_topic, self.listener_callback, 10)
        self.subscription  # prevent unused variable warning

    def listener_callback(self, msg):
        self.get_logger().info('I heard: "%s"' % msg.data)


def main(args=None):
    rclpy.init(args=args)

    img_subscriber = ImageSubscriber()

    rclpy.spin(img_subscriber)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    img_subscriber.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()