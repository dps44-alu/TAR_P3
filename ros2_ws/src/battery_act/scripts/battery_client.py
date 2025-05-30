#!/usr/bin/env python3
import sys
import rclpy
from rclpy.node import Node
from rclpy.action import ActionClient
from battery_act.action import Battery

class BatteryClient(Node):
    def __init__(self):
        super().__init__('battery_client')
        self._client = ActionClient(self, Battery, 'battery_warning')

    def send_goal(self, target):
        self._client.wait_for_server()
        goal = Battery.Goal()
        goal.target_percentage = target
        goal_handle_future = self._client.send_goal_async(
            goal, feedback_callback=self.feedback_callback)
        goal_handle_future.add_done_callback(self.goal_response_callback)

    def goal_response_callback(self, future):
        goal_handle = future.result()
        if not goal_handle.accepted:
            self.get_logger().info('¡Goal rechazado!')
            rclpy.shutdown()
            return
        result_future = goal_handle.get_result_async()
        result_future.add_done_callback(self.get_result_callback)

    def feedback_callback(self, feedback_msg):
        self.get_logger().info(f"Feedback: {feedback_msg.feedback.current_percentage}%")

    def get_result_callback(self, future):
        result = future.result().result
        self.get_logger().info(f"Resultado: {result.warning}")
        rclpy.shutdown()

def main():
    if len(sys.argv) != 2:
        print("Uso: battery_client.py <target_percentage>")
        sys.exit(1)
    rclpy.init()
    node = BatteryClient()
    node.send_goal(int(sys.argv[1]))
    rclpy.spin(node)

if __name__ == '__main__':
    main()
