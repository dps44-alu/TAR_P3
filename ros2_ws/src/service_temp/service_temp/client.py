#!/usr/bin/env python3
import sys
import rclpy
from rclpy.node import Node
from service_temp.srv import ConvertTemp

def main():
    if len(sys.argv)!=3:
        print("Uso: ros2 run service_temp client.py <valor> <Cel_to_Far|Far_to_Cel>")
        return
    rclpy.init()
    node = Node('temp_client')
    cli = node.create_client(ConvertTemp, 'convert_temp')
    while not cli.wait_for_service(1.0):
        node.get_logger().info('Esperando servicio...')
    req = ConvertTemp.Request()
    req.input_temp = float(sys.argv[1])
    req.conversion_type = sys.argv[2]
    fut = cli.call_async(req)
    rclpy.spin_until_future_complete(node, fut)
    node.get_logger().info(f"Resultado: {fut.result().converted_temp}")
    rclpy.shutdown()

if __name__=='__main__':
    main()
