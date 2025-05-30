#!/usr/bin/env python3
import rclpy
from rclpy.node import Node

class MinimalTalker(Node):
    def __init__(self):
        super().__init__('minimal_talker')
        self.get_logger().info('¡Nodo talker de ROS 2 Humble arrancado!')

def main(args=None):
    rclpy.init(args=args)
    node = MinimalTalker()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
