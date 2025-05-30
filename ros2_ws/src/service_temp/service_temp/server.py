#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from service_temp.srv import ConvertTemp

class TempServer(Node):
    def __init__(self):
        super().__init__('temp_server')
        self.srv = self.create_service(ConvertTemp, 'convert_temp', self.cb)

    def cb(self, req, res):
        if req.conversion_type == 'Cel_to_Far':
            res.converted_temp = req.input_temp * 9.0/5.0 + 32.0
        else:
            res.converted_temp = (req.input_temp - 32.0) * 5.0/9.0
        self.get_logger().info(f"{req.input_temp} → {res.converted_temp}")
        return res

def main():
    rclpy.init()
    node = TempServer()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__=='__main__':
    main()
